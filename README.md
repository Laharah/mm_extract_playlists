# extractPlaylists
Extract playlists from MediaMonkey database from the command line.

**NOTE: Does not currently support auto-playlists.**

## Requirements
* Python 3.8+

## Installation
Pure python, can be installed with pip:

`pip install git+https://github.com/Laharah/mm_extract_playlists.git`

---

```
usage: extractPlaylists database [outputdir] [options]

Extract playlists from MediaMonkey and save them as m3u files.

positional arguments:
  database              MediaMonkey database to extract playlists from.
  output_dir            Location to save playlists.

optional arguments:
  -h, --help            show this help message and exit
  -f, --overwrite       Overwrite existing files.
  --music-folder MUSIC_FOLDER
                        Re-route tracks to local music folder.
  -p, --prepend-parent  Place parent playlists name at front of child
                        playlists.
  -d, --folders         Place sub-playlists in their own folders, named after
                        parent playlist.

Example usage: extractPlaylists -d %APPDATA%\MediaMonkey\MM.DB %USERPROFILE%\Music
```
