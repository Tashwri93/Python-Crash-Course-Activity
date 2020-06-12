def make_album(artist_name,album_name,num_tracks=''):
    album = {'artist name':artist_name,'album name': album_name}
    if num_tracks:
        album['songs'] = num_tracks
    return album
album_n = make_album('brandy','afrodisiac')
print(album_n)
album_n = make_album('mabel','ivy to roses')
print(album_n)
album_n = make_album('lloyd', 'lessons in love')
print(album_n)
album_n = make_album('mary j. bilge', 'growing pains', num_tracks = 16)
print(album_n)
