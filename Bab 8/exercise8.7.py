def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('oasis', 'wonderwall')
print(album)

album = make_album('tulus', 'monokrom')
print(album)

album = make_album('fstvlst', 'jefferson')
print(album)

#num_songs

def make_album(artist, title, num_songs=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if num_songs:
        album_dict['num_songs'] = num_songs
    return album_dict

album = make_album('oasis', 'wonderwall')
print(album)

album = make_album('tulus', 'monokrom')
print(album)

album = make_album('fstvlst', 'jefferson')
print(album)

album = make_album('the jeblogs', 'sekian, terima kasih', num_songs=8)
print(album)