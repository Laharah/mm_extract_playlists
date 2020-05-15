import pytest

from mm_extract_playlist import database
from mm_extract_playlist.playlist import Playlist


@pytest.fixture(scope="module")
def db():
    con = database.connect('tests/testdb.db')
    yield con
    con.close()


def test_connect():
    con = database.connect('tests/testdb.db')
    cur = con.cursor()
    cur.execute("select idplaylist, PlaylistName from playlists")
    first = cur.fetchone()
    assert first == (1, 'Favorites - Top 50')


def test_get_all_playlists(db):
    playlists = database.get_all_playlists(db)
    assert all(isinstance(p, Playlist) for p in playlists)
    assert playlists[0].tracks == []
    ksp = [p for p in playlists if p.name == 'KSP'][0]
    assert len(ksp.tracks) == 51
    # Must be in order
    assert [t.index for t in ksp.tracks] == list(range(51))


def test_get_all_playlist_tracks(db):
    tracks = database.get_all_playlist_tracks(db)
    assert len(tracks) == 2
    assert len(tracks[16]) == 25
    assert len(tracks[14]) == 51
    # Must be in order
    assert [t.index for t in tracks[16]] == list(range(25))
    assert [t.index for t in tracks[14]] == list(range(51))
