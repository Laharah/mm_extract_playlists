import argparse
import itertools
from pathlib import Path

from . import database
from . import m3u
from . import track


def main(db, output_dir, music_folder=None, overwrite=False):
    db = database.connect(db)
    playlists = database.get_all_playlists(db)
    if music_folder:
        music_folder = Path(music_folder)
        orig_music_folder = track.common_base(
            itertools.chain(*[p.tracks for p in playlists.values()]))
        print(f"Calculated original music folder to be '{orig_music_folder}'")
        replacement = (orig_music_folder, music_folder)
        print(f"Re-routing to '{music_folder}'")
    else:
        replacement = None
    m3u.write_all(playlists, output_dir, replace=replacement, overwrite=overwrite)
    db.close()


def entry_point():
    parser = argparse.ArgumentParser('extractPlaylists')
    parser.add_argument('db',
                        metavar='database',
                        help="MediaMonkey database to extract playlists from.")
    parser.add_argument('output_dir',
                        nargs='?',
                        metavar='output_dir',
                        default=Path(),
                        type=Path,
                        help="Location to save playlists.")
    parser.add_argument('-f', '--overwrite',
                        help="Overwrite existing files.",
                        dest='overwrite',
                        action='store_true')
    parser.add_argument('--music-folder',
                        help='Re-route tracks to local music folder.',
                        dest='music_folder',
                        type=Path)
    options = parser.parse_args()
    options = vars(options)
    main(**options)


if __name__ == '__main__':
    entry_point()
