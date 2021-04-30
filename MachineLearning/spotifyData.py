import spotipy as sp
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

SPOTIPY_CLIENT_ID= 'f792fe7782384f54879ed2ae80538895'
SPOTIPY_CLIENT_SECRET = '11d8603456734c3db24cfc54eaa1bd63'

playlistLink = 'https://open.spotify.com/playlist/7uzmW6AP48YD006g3YGVEo?si=0260ea551a2a4804'

apiLink = sp.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = SPOTIPY_CLIENT_ID,client_secret = SPOTIPY_CLIENT_SECRET))

playlistInfo = apiLink.playlist(playlistLink)

tracks = playlistInfo['tracks']

totalTracks = tracks['total']


trackName = ['']*totalTracks
trackArtist = ['']*totalTracks
for i in range(0,totalTracks):
    trackName[i] = tracks['items'][i]['track']['name']
    trackArtist[i] = tracks['items'][i]['track']['artists'][0]['name']
    #print(trackName[i] + "  " + trackArtist[i])
   #print('track ' + str(i+1) +  ' : ' + tracks['items'][i]['track']['name'] + ' ARTIST: ' + tracks['items'][i]['track']['artists'][0]['name'])

trackInfo = np.concatenate((trackName, trackArtist))
pprint(trackName)




