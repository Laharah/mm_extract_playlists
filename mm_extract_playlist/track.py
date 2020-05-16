from pathlib import PureWindowsPath


class Track:
    def __init__(self, title, path, playlist_id, index):
        self.title, self.path = title, PureWindowsPath(path)
        self.playlist_id, self.index = playlist_id, index

    def __repr__(self):
        return f'Track("{self.title}", {self.index=})'


def common_base(tracks):
    "Find the 'Music' folder"
    tracks = iter(tracks)
    base = next(tracks).path.parts
    base_index = 0
    for t in tracks:
        t = t.path
        for i, (p1, p2) in enumerate(zip(base, t.parts)):
            if p1 != p2:
                base_index = i
                break
    return PureWindowsPath().joinpath(*base[:i])
