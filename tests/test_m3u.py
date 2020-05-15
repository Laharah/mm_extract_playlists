import pytest
from mm_extract_playlist import m3u
from mm_extract_playlist.playlist import Playlist
from mm_extract_playlist.track import Track
from pathlib import Path, PureWindowsPath


@pytest.fixture
def pl():
    tracks = [
        Track('Moonscape', ':\\Users\\testuser\\Desktop\\songs\\08 Moonscape.mp3', 1, 0),
        Track('Mountains', ':\\Users\\testuser\\Desktop\\songs\\08 Mountains.mp3', 1, 1),
        Track('Outlands', ':\\Users\\testuser\\Desktop\\songs\\09 Outlands.mp3', 1, 2),
        Track('Crush', ':\\Users\\testuser\\Desktop\\songs\\10 Crush.mp3', 1, 3),
    ]
    return Playlist(1, 'TEST PLAYLIST', tracks=tracks)


def test_write(tmp_path, pl):
    path = tmp_path / 'test_pl.m3u'
    m3u.write(pl, path)
    expected = '\n'.join(str(t.path) for t in pl.tracks)
    assert path.read_text().strip() == expected


def test_no_overwrite(tmp_path, pl):
    path = tmp_path / 'test_pl.m3u'
    path.write_text("don't erase me")
    with pytest.raises(FileExistsError):
        m3u.write(pl, path)
    assert path.read_text() == "don't erase me"
    m3u.write(pl, path, overwrite=True)
    assert path.read_text() != "don't erase me"


def test_replace_music_folder(tmp_path, pl):
    replacement = (PureWindowsPath(':/Users/testuser/Desktop/songs'),
                   Path('/pool/Media/Music'))
    expected = ("/pool/Media/Music/08 Moonscape.mp3\n"
                "/pool/Media/Music/08 Mountains.mp3\n"
                "/pool/Media/Music/09 Outlands.mp3\n"
                "/pool/Media/Music/10 Crush.mp3\n")
    path = tmp_path / 'test'
    m3u.write(pl, path, replace=replacement)
    assert path.read_text() == expected


def test_write_all(pl, tmp_path):
    pl2 = Playlist(2, 'pl2', tracks=pl.tracks[:])
    m3u.write_all([pl, pl2], tmp_path)
    m1 = tmp_path / 'TEST PLAYLIST.m3u'
    m2 = tmp_path / 'pl2.m3u'
    assert m2.exists()
    assert m1.exists()
    expected = '\n'.join(str(t.path) for t in pl.tracks)
    assert m1.read_text().strip() == expected
    assert m2.read_text().strip() == expected


def test_all_overwrite(pl, tmp_path, capfd):
    pl2 = Playlist(2, 'pl2', tracks=pl.tracks[:])
    prev = tmp_path / 'pl2.m3u'
    prev.write_text('pls no delete')
    m3u.write_all((pl, pl2), tmp_path)
    assert capfd.readouterr().err == f"'{prev}' already exists, skipping.\n"
    assert prev.read_text() == 'pls no delete'
    m3u.write_all((pl, pl2), tmp_path, overwrite=True)
    assert prev.read_text() != 'pls no delete'


def test_all_replace(pl, tmp_path):
    pl2 = Playlist(2, 'pl2', tracks=pl.tracks[:])
    replacement = (PureWindowsPath(':/Users/testuser/Desktop/songs'),
                   Path('/pool/Media/Music'))
    expected = ("/pool/Media/Music/08 Moonscape.mp3\n"
                "/pool/Media/Music/08 Mountains.mp3\n"
                "/pool/Media/Music/09 Outlands.mp3\n"
                "/pool/Media/Music/10 Crush.mp3\n")
    m3u.write_all([pl, pl2], tmp_path, replace=replacement)
    for p in (pl, pl2):
        path = tmp_path / f'{p.name}.m3u'
        assert path.read_text() == expected
