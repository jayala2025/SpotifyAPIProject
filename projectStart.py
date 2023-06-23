import requests
import os
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials 

# client_id = '7d90581a1f7e4320b41671ac9deab569'
# client_secret = 'a0e800ffe62b4b79b51e2b8da0ae6bfc'
url = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(url, {
'grant_type': 'client_credentials',
'client_id': '7d90581a1f7e4320b41671ac9deab569',
'client_secret': 'a0e800ffe62b4b79b51e2b8da0ae6bfc',
})

auth_response_data = auth_response.json()
# print(auth_response_data)

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
baseURL = 'https://api.spotify.com/v1/'
track_id = input('Enter track id: ')
trackInfo = requests.get(baseURL + 'tracks/' + track_id, headers=headers)

trackName = trackInfo.json()['name']
trackArtists = trackInfo.json()['artists'][0]['name']

print(f"{trackName} by {trackArtists}")



