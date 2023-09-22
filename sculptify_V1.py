import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"
client_id = '31a7d2fdc8d9494e8ad8890470143aab'
client_secret = '9d96beaa94e7428e964e95f80fa4db43'
redirect_uri = 'http://127.0.0.1:9090'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

playlist_ID_classic_rock = '1GnZRXMHYByIgvShVAdSAc'

#si=f3d46270e9044ae0

def returnPlaylist(playlist_ID):
    playlist = sp.playlist_tracks(playlist_ID)
    playlist_clean = []
    for track in playlist['items']:
        full_artists = []
        for artist in track['track']['artists']:
             full_artists.append(artist['name'])
        playlist_clean.append((track['track']['name'], ', '.join(full_artists), track['track']['album']['name'])) 
    #print(track['track']['album'])
    return playlist_clean


#output = returnPlaylist(playlist_ID_classic_rock)
#print(output)
playlist = sp.playlist_tracks(playlist_ID_classic_rock)
print(playlist['items'][0]['track']['external_ids'].keys())
