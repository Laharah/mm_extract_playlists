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
    pass


if __name__ == '__main__':
    entry_point()
