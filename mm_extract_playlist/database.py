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
    return {p.id: p for p in playlists}


def get_all_playlist_tracks(db):
    "Get dict of tracks grouped by playlist id"
    drive_map = get_drive_letters(db)
    cur = db.cursor()
    cur.execute('SELECT SongTitle, SongPath, IDPlaylist, SongOrder, IDMedia '
                'FROM PlaylistSongs INNER JOIN Songs '
                'ON PlaylistSongs.IDSong = Songs.ID '
                'ORDER BY SongOrder')
    pl_tracks = []
    for row in cur:
        # resolve drive letter and pre-pend to path
        path, media = row[1], row[-1]
        drive = drive_map[media]
        path = drive + path
        row = list(row[:-1])
        row[1] = path
        pl_tracks.append(Track(*row))
    return utils.groupby(pl_tracks, key=lambda t: t.playlist_id)


def get_drive_letters(db):
    cur = db.cursor()
    cur.execute('SELECT IDMedia, DriveLetter FROM Medias')
    return {id: chr(letter + 65) for id, letter in cur if letter}
