
class Track:
    def __init__(self, title, path, playlist_id, index):
        self.title, self.path = title, path
        self.playlist_id, self.index= playlist_id, index

    def __repr__(self):
        return f'Track("{self.title}", {self.index=})'
