from pathlib import PureWindowsPath
from mm_extract_playlist import track as tr

sample_row = ('Space Oddity', ':\\Users\\testuser\\Desktop\\songs\\01 Space Oddity.mp3',
              14, 2)
sample_row2 = ('Outlands', ':\\Users\\testuser\\Desktop\\songs\\09 Outlands.mp3', 14, 35)
sample_row3 = ('Crush', ':\\Users\\testuser\\Desktop\\10 Crush.mp3', 16, 19)


def test_create_track():
    t = tr.Track('Space Oddity',
                 ':\\Users\\testuser\\Desktop\\songs\\01 Space Oddity.mp3', 14, 2)
    assert t.title == 'Space Oddity'
    assert t.path == PureWindowsPath(
        ':\\Users\\testuser\\Desktop\\songs\\01 Space Oddity.mp3')
    assert t.playlist_id == 14
    assert t.index == 2
    assert repr(t) == 'Track("Space Oddity", self.index=2)'


def test_create_track_from_row():
    t = tr.Track(*sample_row)
    assert t.title == 'Space Oddity'
    assert t.path == PureWindowsPath(
        ':\\Users\\testuser\\Desktop\\songs\\01 Space Oddity.mp3')
    assert t.playlist_id == 14
    assert t.index == 2

def test_get_common_base():
    tracks = [tr.Track(*r) for r in [sample_row, sample_row2]]
    common = tr.common_base(tracks)
    assert common == PureWindowsPath(':\\Users\\testuser\\Desktop\\songs')
    tracks.append(tr.Track(*sample_row3))
    common = tr.common_base(tracks)
    assert common == PureWindowsPath(':\\Users\\testuser\\Desktop')
