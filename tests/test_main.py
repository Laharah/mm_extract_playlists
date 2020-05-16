import re
import os
from pathlib import Path
from mm_extract_playlist import __main__ as m


def test_main(tmp_path):
    m.main('tests/testdb.db', tmp_path)
    listing = list(tmp_path.iterdir())
    assert len(listing) == 2


def test_main_redirect(tmp_path, capfd):
    m.main('tests/testdb.db', tmp_path, music_folder='/pool/Media/Music')
    listing = list(tmp_path.iterdir())
    assert len(listing) == 2
    out = capfd.readouterr().out
    print(out)
    assert re.search(r':\\Users\\testuser\\Desktop\\songs', out) is not None
    p = tmp_path / 'KSP.m3u'
    first = Path(p.read_text().splitlines()[0])
    assert first.parts == (os.path.sep, 'pool', 'Media', 'Music', '02 Gipsy Danger.mp3')
