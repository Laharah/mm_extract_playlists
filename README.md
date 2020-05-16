# extractPlaylists
Extract playlists from MediaMonkey database.

**NOTE: Does not currently support auto-playlists.**

```
usage: extractPlaylists [-h] [-f] [--music-folder MUSIC_FOLDER]
                        database [output_dir]

positional arguments:
  database              MediaMonkey database to extract playlists from.
  output_dir            Location to save playlists.

optional arguments:
  -h, --help            show this help message and exit
  -f, --overwrite       Overwrite existing files.
  --music-folder MUSIC_FOLDER
                        Re-route tracks to local music folder.
```
