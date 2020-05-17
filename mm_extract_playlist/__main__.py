__doc__ = "Extract playlists from MediaMonkey and save them as m3u files."
import argparse
import itertools
from pathlib import Path

from . import database
from . import m3u
from . import track


def main(db,
         output_dir,
         music_folder=None,
         overwrite=False,
         prepend_parent=False,
         folders=False):

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
    m3u.write_all(playlists,
                  output_dir,
                  replace=replacement,
                  overwrite=overwrite,
                  prepend_parent=prepend_parent,
                  folders=folders)
    db.close()


def entry_point():
    example = (r'Example usage: '
               r'extractPlaylists -d %APPDATA%\MediaMonkey\MM.DB %USERPROFILE%\Music')
    parser = argparse.ArgumentParser(
        'extractPlaylists',
        usage='extractPlaylists database [outputdir] [options]',
        description=__doc__,
        epilog=example)
    parser.add_argument('db',
                        metavar='database',
                        help="MediaMonkey database to extract playlists from.")
    parser.add_argument('output_dir',
                        nargs='?',
                        metavar='output_dir',
                        default=Path(),
                        type=Path,
                        help="Location to save playlists.")
    parser.add_argument('-f',
                        '--overwrite',
                        help="Overwrite existing files.",
                        dest='overwrite',
                        action='store_true')
    parser.add_argument('--music-folder',
                        help='Re-route tracks to local music folder.',
                        dest='music_folder',
                        type=Path)
    parser.add_argument('-p',
                        '--prepend-parent',
                        help="Place parent playlists name at front of child playlists.",
                        dest='prepend_parent',
                        action='store_true')
    parser.add_argument('-d',
                        '--folders',
                        help=('Place sub-playlists in their own folders, named after '
                              'parent playlist.'),
                        dest='folders',
                        action='store_true')
    options = parser.parse_args()
    options = vars(options)
    main(**options)


if __name__ == '__main__':
    entry_point()
