from mm_extract_playlist import track as tr

sample_row = ('Space Oddity', ':\\Users\\testuser\\Desktop\\songs\\01 Space Oddity.mp3', 14, 2)


def test_create_track():
    t = tr.Track('Space Oddity',
                 ':\\Users\\testuser\\Desktop\\songs\\01 Space Oddity.mp3', 14, 2)
    assert t.title == 'Space Oddity'
    assert t.path == ':\\Users\\testuser\\Desktop\\songs\\01 Space Oddity.mp3'
    assert t.playlist_id == 14
    assert t.index == 2

def test_create_track_from_row():
    t = tr.Track(*sample_row)
    assert t.title == 'Space Oddity'
    assert t.path == ':\\Users\\testuser\\Desktop\\songs\\01 Space Oddity.mp3'
    assert t.playlist_id == 14
    assert t.index == 2

