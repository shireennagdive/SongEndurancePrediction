import billboard
# import spotipy.util
# chart = billboard.ChartData('hot-100', date='1950-05-10')
# print(chart) #title artist rank weeks
import json
import requests
import base64
import urllib
from flask import request

CLIENT_ID  = 'f7cdf4a9bdf34bca9dabb6c25047a1d9'
CLIENT_SECRET = '2eb71b5485554e9b8f5376d880c09eb8'

#Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8080
REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URL, PORT)
SCOPE = "user-library-read"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

def user_Authorization():
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }
    base64encoded = base64.b64encode("{}:{}".format(CLIENT_ID, CLIENT_SECRET))
    headers = {"Authorization": "Basic {}".format(base64encoded)}
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)

    # Tokens are Returned to Application
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

    # Use the access token to access Spotify API
    authorization_header = {"Authorization":"Bearer {}".format(access_token)}
    return authorization_header

#Gathering of profile information
def Profile_Data(header):
    # Get user profile data
    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=header)
    profile_data = json.loads(profile_response.text)
    return profile_data

# SPOTIFY_USERNAME  = 'nsln2o9qyw0jbqx007ndlz6qw'
# SPOTIFY_REDIRECT_URI  = 'https://www.shireennagdive.com'
# SPOTIFY_SCOPE  = 'playlist-modify-public'
#
# token = spotipy.util.prompt_for_user_token(
#    SPOTIFY_USERNAME,
#    scope=SPOTIFY_SCOPE,
#    client_id=SPOTIFY_CLIENT_ID,
#    client_secret=SPOTIFY_CLIENT_SECRET,
#    redirect_uri=SPOTIFY_REDIRECT_URI)
#
# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
#
# print(token)
# if token:
#     spotify = spotipy.Spotify(auth=token)
#     results = spotify.artist_albums(birdy_uri, album_type='album')
#     albums = results['items']
#     while results['next']:
#        results = spotify.next(results)
#        albums.extend(results['items'])
#
# for album in albums:
#    print(album['name'])

