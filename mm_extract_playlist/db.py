import sqlite3
from . import utils

def connect(path=None):
    return sqlite3.connect(path)

def get_all_playlists(db):
    "get a list of playlist objects with their songs"

def get_all_playlist_tracks(db):
    "Get dict of tracks grouped by playlist id"
