from mm_extract_playlist import db

def test_connect():
    con = db.connect('tests/testdb.db')
    cur = con.cursor()
    cur.execute("select idplaylist, PlaylistName from playlists")
    first = cur.fetchone()
    assert first == (1, 'Favorites - Top 50')
    

