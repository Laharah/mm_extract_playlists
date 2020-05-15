import sqlite3
from . import utils
from .playlist import Playlist
from .track import Track


def connect(path=None):
    return sqlite3.connect(path)


def get_all_playlists(db):
    "get a list of playlist objects with their songs"
    cur = db.cursor()
    cur.execute('SELECT * FROM Playlists')
    playlists = [Playlist.from_db_row(row) for row in cur]
    tracks = get_all_playlist_tracks(db)
    for p in playlists:
        p.tracks = tracks[p.id]
    return playlists


def get_all_playlist_tracks(db):
    "Get dict of tracks grouped by playlist id"
    cur = db.cursor()
    cur.execute('SELECT SongTitle, SongPath, IDPlaylist, SongOrder '
                'FROM PlaylistSongs INNER JOIN Songs '
                'ON PlaylistSongs.IDSong = Songs.ID '
                'ORDER BY SongOrder')
    pl_tracks = [Track(*row) for row in cur]
    return utils.groupby(pl_tracks, key=lambda t: t.playlist_id)
