from mm_extract_playlist import playlist as pl
from mm_extract_playlist.track import Track

pl_row = (14, 'KSP', 8, None, 0, None, 5,
          ':\\Users\\testuser\\Desktop\\Playlists\\KSP.m3u', None, '2020-05-15 00:30:34',
          None, '0e363e44-d27e-4269-8800-3e5cfda9824f', -1, None)


def test_create_playlist():
    p = pl.Playlist(14, 'KSP', parent=8)
    assert p.name == 'KSP'
    assert p.id == 14
    assert p.parent == 8
    assert p.auto is False
    assert p.tracks == []


def test_create_playlist_from_row():
    p = pl.Playlist.from_db_row(pl_row)
    assert p.name == 'KSP'
    assert p.id == 14
    assert p.parent == 8
    assert p.auto is False
    assert p.tracks == []

