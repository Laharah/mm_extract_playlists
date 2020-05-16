from mm_extract_playlist import __main__ as m

def test_main(tmp_path):
    m.main('tests/testdb.db', tmp_path)
    listing = list(tmp_path.iterdir())
    print()
    for p in listing:
        print(p)
        print(p.read_text())
    assert len(listing) == 10 

