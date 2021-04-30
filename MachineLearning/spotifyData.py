import spotipy as sp
import pandas as pd
import numpy as np

from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

SPOTIPY_CLIENT_ID= 'f792fe7782384f54879ed2ae80538895'
SPOTIPY_CLIENT_SECRET = '11d8603456734c3db24cfc54eaa1bd63'

playlistLink = 'https://open.spotify.com/playlist/7uzmW6AP48YD006g3YGVEo?si=0260ea551a2a4804'

apiLink = sp.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = SPOTIPY_CLIENT_ID,client_secret = SPOTIPY_CLIENT_SECRET))

playlistInfo = apiLink.playlist(playlistLink)
trackInfo = playlistInfo['tracks']

totalTracks = trackInfo['total']

trackName = []
trackArtist = []
genreTags = []

audioFeatures = []
audioAnalysis = []

pitchValue = []

for i in range(0,totalTracks):
    trackName.append(trackInfo['items'][i]['track']['name'])
    trackArtist.append(trackInfo['items'][i]['track']['artists'][0]['name'])
    genreTags.append(np.array(apiLink.artist(trackInfo['items'][i]['track']['artists'][0]['uri'])['genres']))

    audioFeatures.append(apiLink.audio_features(trackInfo['items'][i]['track']['uri']))


trackMetaDict = {'name':trackName,'artist':trackArtist, 'genre': genreTags}
trackMetaDF = pd.DataFrame(trackMetaDict)
audioFeaturesDF = pd.DataFrame(audioFeatures)

trackMetaDF.to_csv(r'C:\Users\enigm\Documents\School\FourthYear\Spring21\ECE196\machineLearning\trackInfo2.csv')
audioFeaturesDF.to_csv(r'C:\Users\enigm\Documents\School\FourthYear\Spring21\ECE196\machineLearning\audioFeatures2.csv')