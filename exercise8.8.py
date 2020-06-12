def make_album(artist_name,album_name,num_tracks=''):
    album = {'Artist name':artist_name,'Album name': album_name}
    if num_tracks:
        album['songs'] = num_tracks
    return album

while True:
    print("\nPlease enter your favourite artist and your favourite album: ")
    print("\nenter 'q' at the time to quit")

    ar_name = input("Artist name: ")
    if ar_name == 'q':
        break

    al_name = input("Album name: ")
    if al_name == 'q':
        break

    format_album = make_album(ar_name.title(), al_name.title())
    print(format_album)
