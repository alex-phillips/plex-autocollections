# Plex Auto-Collections
This is a simple script to automatically create collections by matching the titles of movies in your library with movies in the `collections.yml` file.

This script was originally based off of an inspired by [this script](https://github.com/AustinHasten/PlexHolidays), so thanks to [AustinHasten](https://github.com/AustinHasten) for that!

**DISCLAIMER** although I'm a software developer, I have done very little python (this is my first real program). So please forgive the crudeness of some of my code or methods. PRs welcome!

## Installation
Simply use pip to install the requirements and run the software with python 3.

```python
pip install -r requirements.txt
...
python main.py
```

It will ask you for your Plex login and automatically find your servers. If it looks like more than one library may contain movies, it will ask you which one you want to create collections on.

## Usage
Since this was designed to run against any arbitrary Plex movie library (and some people may have different naming conventions for movies), I decided that regular expression matching would be best for most cases.

Example:
`^Star Wars(.*?A New Hope|.*?Episode (?:4|IV))?$` will match all of the following that could be the first (chronoligically) Star Wars movie (and more):
* Star Wars
* Star Wars: A New Hope
* Star Wars: Episode 4
* Star Wars: Episode IV

If you want to customize collection names or the names of movies found in your library, simply edit or replace the included `collections.yml` file.

## Posters

A great resource for posters can be found in this [reddit thread](https://www.reddit.com/r/PlexPosters/comments/8vny7j/an_index_of_utheo00s_473_collections_posters/).

## Contributing
I wrote this with the hope that the community would help expand and include more collections and help make any corrections in better matching movies in various libraries. Pull requests are very much welcome!
