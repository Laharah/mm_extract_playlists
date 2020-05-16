from . import database
from . import m3u


def main(db, output_dir):
    db = database.connect(db)
    playlists = database.get_all_playlists(db)
    m3u.write_all(playlists, output_dir)


def entry_point():
    pass


if __name__ == '__main__':
    entry_point()
