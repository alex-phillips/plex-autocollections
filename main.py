#!/usr/bin/env python
import re, sys, getpass
import plexapi.utils
from retry import retry
from plexapi.server import PlexServer, CONFIG
from plexapi.myplex import MyPlexAccount
from plexapi.exceptions import BadRequest
import yaml

## Edit ##
PLEX_URL = ''
PLEX_TOKEN = ''

try:
    PLEX_URL = CONFIG.data['auth'].get('server_baseurl', PLEX_URL)
    PLEX_TOKEN = CONFIG.data['auth'].get('server_token', PLEX_TOKEN)
except:
    print("Failed loading in config file.")

class Plex():
    def __init__(self):
        if PLEX_URL and PLEX_TOKEN:
            self.server = PlexServer(PLEX_URL, PLEX_TOKEN)
        else:
            self.account = self.get_account()
            self.server = self.get_account_server(self.account)

        self.section = self.get_server_section(self.server)
        self.media = self.get_flat_media(self.section)

    @retry(BadRequest)
    def get_account(self):
        username = input("Plex Username: ")
        password = getpass.getpass()

        return MyPlexAccount(username, password)

    def get_account_server(self, account):
        servers = [ _ for _ in account.resources() if _.product == 'Plex Media Server' ]
        if not servers:
            print('No available servers.')
            sys.exit()

        return plexapi.utils.choose('Select server index', servers, 'name').connect()

    def get_server_section(self, server):
        sections = [ _ for _ in server.library.sections() if _.type in {'movie'} ]
        if not sections:
            print('No available sections.')
            sys.exit()

        return plexapi.utils.choose('Select section index', sections, 'title')

    def get_flat_media(self, section):
        # Movie sections are already flat
        if section.type == 'movie':
            return self.section.all()
        else:
            episodes = []
            for show in self.section.all():
                episodes += show.episodes()
            return episodes

def process_movies(movies, medium, collection):
    matches = []
    for movie in movies:
        if isinstance(movie, list):
            process_movies(movie, medium, collection)
        else:
            year_regex = None
            for match in re.findall(r"\{\{((?:\d+\|?)+)\}\}", movie):
                year_regex = match
                movie = re.sub(r"\s+\{\{((\d+\|?)+)\}\}", "", movie)

            regex = re.compile(movie, re.IGNORECASE)
            if re.search(regex, medium.title):
                if year_regex and re.search(year_regex, str(medium.year)):
                    print("Adding", medium.title, "to collection", collection)
                    matches.append(medium)
                elif year_regex is None:
                    print("Adding", medium.title, "to collection", collection)
                    matches.append(medium)

    if matches:
        for movie in matches:
            movie.addCollection(collection)

with (open("collections.yml", "r")) as stream:
    collections = yaml.load(stream, Loader=yaml.SafeLoader)

if __name__ == "__main__":
    plex = Plex()
    keyword_matches = []

    for medium in plex.media:
        for collection, movies in collections.items():
            process_movies(movies, medium, collection)
