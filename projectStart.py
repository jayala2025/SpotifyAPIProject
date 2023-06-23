import requests
import os
import spotipy
import json
import pandas as pd
import sqlalchemy as db
from spotipy.oauth2 import SpotifyClientCredentials 

# testTrackID: 48NXpYRuvv9izul4oXhqS9
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

# trackDataFrame = pd.DataFrame.from_dict(trackInfo.json())
# engine = db.create_engine('sqlite:///spotifyapiproject.db')
# trackDataFrame.to_sql('Track Information', con=engine, if_exists='replace', index=False)

# with engine.connect() as connection:
#    query_result = connection.execute(db.text("SELECT * FROM Track Information;")).fetchall()
#    print(pd.DataFrame(query_result))

trackName = trackInfo.json()['name']
trackArtists = trackInfo.json()['artists'][0]['name']

print(f"{trackName} by {trackArtists}")



