# Plex Auto-Collections
This is a simple script to automatically create collections by matching the titles of movies in your library with movies in the `collections.yml` file or a custom collections file.

This script was originally based off of an inspired by [this script](https://github.com/AustinHasten/PlexHolidays), so thanks to [AustinHasten](https://github.com/AustinHasten) for that!

## Installation
Simply use pip to install the requirements and run the software with python 3.

```python
pip install -r requirements.txt
```

## Usage
Simply run the script:
```
python3 main.py
```

It will ask you for your Plex login and automatically find your servers. If it looks like more than one library may contain movies, it will ask you which one you want to create collections on. This also uses the standard [PlexAPI](https://pypi.org/project/PlexAPI/) standard config options of reading authentication information from the plexapi config file.

You can also set the environment variables `PLEX_URL` and `PLEX_TOKEN` for authentication.

### Collection Files

Since this was designed to run against any arbitrary Plex movie library (and some people may have different naming conventions for movies), I decided that regular expression matching would be best for most cases.

Example:
`^Star Wars(.*?A New Hope|.*?Episode (?:4|IV))?$` will match all of the following that could be the first (chronoligically) Star Wars movie (and more):
* Star Wars
* Star Wars: A New Hope
* Star Wars: Episode 4
* Star Wars: Episode IV

If you want to customize collection names or the names of movies found in your library, simply edit or replace the included `collections.yml` file.

### Custom collections
An alternate method to add additional collections is via the `collections.d`
directory. Files contained within this directory, ending with the suffix `.yml`,
will automatically be loaded/processed after `collections.yml`. The format of
each `xxxxx.yml` file is identical to that of `collections.yml`. Additionally, one may
disable any custom collection by simply renaming the file (e.g. `xxxxx.yml.disabled`).

### Best practices
When determining whether to put a new collection in `collections.yml` or
`collections.d`, please keep the following best practices in mind:
* Any collection _may_ reside in a custom collection.
* A collection longer than about 10 lines in length _should_ be placed in its own
  custom collection.
* A collection longer than about 50 lines in length _should_ be placed in its own
  custom collection, and be _disabled_ by default (e.g.
  `my_collection.yml.disabled`).

### Examples
| Command                                                                         | Resulting action |
| ------------------------------------------------------------------------------- | ---------------- |
| `python main.py`                                                                | process `collections.yml` plus any custom collections named `collections.d/*.yml` |
| `./main.py`                                                                     | same as above |
| `DEBUG=1 ./main.py`                                                             | same as above & display debugging output |
| `./main.py --library 'Old Movies'`                                              | process above named collections without being prompted to select the library (useful within crontab) |
| `./main.py --help                                                               | show 'help' |
| `./main.py collections.yml`                                                     | process only `collections.yml` |
| `./main.py collections.yml collections.d/my_collection.yml`                     | process `collections.yml` & the custom collection `collections.d/my_collection.yml` |
| `./main.py collections.d/my_collection.yml collections.d/hallmark.yml.disabled` | process only the custom collections `collections.d/my_collection.yml` & `collections.d/hallmark.yml.disabled` |

**NOTE: when supplying custom collection filenames via the command
line, one may also include custom collections that have been _disabled_.**

## Posters

A great resource for posters can be found in this [reddit thread](https://www.reddit.com/r/PlexPosters/comments/8vny7j/an_index_of_utheo00s_473_collections_posters/).

## Contributing
I wrote this with the hope that the community would help expand and include more collections and help make any corrections in better matching movies in various libraries. Pull requests are very much welcome!
