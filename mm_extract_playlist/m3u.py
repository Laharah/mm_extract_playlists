import sys
from pathlib import Path
from .utils import sanitize


def write_all(playlists,
              dest_folder,
              overwrite=False,
              replace=None,
              prepend_parent=False,
              folders=False):
    """
    Write playlists to dest_folder.
        playlists: dictonary in the format {id:Playlist}
        dest_folder: folder to write playlists to
        overwrite: Overwrite conflicting playlists in dest_folder.
        replace: replace music folder `tuple(old/music/folder, local/music/folder)`.
    """
    for pl in playlists.values():
        if pl.auto:
            print(f'Skipping AutoPlaylist "{pl.name}".', file=sys.stderr)
            continue
        if not pl.tracks:
            print(f'Skipping empty playlist "{pl.name}"', file=sys.stderr)
            continue
        file = Path(f'{sanitize(pl.name)}.m3u')
        if (prepend_parent or folders) and pl.parent is not None:
            parents = [file.name]
            p = pl
            while (p := p.parent):
                p = playlists[p]
                parents.append(sanitize(p.name))
            if folders:
                file = file.parent.joinpath(*reversed(parents[1:])) / file.name
            if prepend_parent:
                file = file.parent / ' - '.join(reversed(parents))

        path = dest_folder / file
        if folders:
            path.parent.mkdir(parents=True, exist_ok=True)
        try:
            write(pl, path, overwrite=overwrite, replace=replace)
        except FileExistsError:
            print(f"'{path}' already exists, skipping.", file=sys.stderr)


def write(playlist, path, *, overwrite=False, replace=None):
    """
    Write playlist to path.
        playlist: Playlist object to write.
        path: Local path to write playlist.
        overwrite: Overwrite any exsisting file at path.
        replace: replace music folder `tuple(old/music/folder, local/music/folder)`.
    """
    mode = 'wb' if overwrite is True else 'xb'
    with open(path, mode) as fout:
        for track in playlist.tracks:
            path = track.path
            if replace:
                old, new = replace
                rel = path.relative_to(old)
                path = new / rel
            fout.write(bytes(str(path), 'utf8'))
            fout.write(b'\n')
