import pygn
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import os
import urllib, base64, json, requests
import datetime

now=datetime.datetime.now()
sp_client_ID='9bdac330697c4972a4779af93656ea65'
sp_client_secret='d75bdac8511f4580858f7e4f7962008b'
host='http://127.0.0.1:5000/'
os.environ["SPOTIPY_CLIENT_ID"]=sp_client_ID
os.environ["SPOTIPY_CLIENT_SECRET"]=sp_client_secret
os.environ["SPOTIPY_REDIRECT_URI"]=host
username="manjogsingh+sp4"
scope = 'playlist-modify-public'
util.prompt_for_user_token(username=username,scope=scope,client_id = sp_client_ID,client_secret = sp_client_secret,redirect_uri = host)

token = util.prompt_for_user_token(username, scope)

client_ID='170259781-06F33892AE9B17F95EE25A24C4593C70'
user_ID= pygn.register(client_ID)
track_titles=[]
artist_list=[]

result=pygn.createRadio(client_ID,user_ID,mood='42947',popularity ='1000',similarity = '1000',count='10')

jsonData=json.dumps(result,sort_keys=True,indent=4)
jsonObject=json.loads(jsonData)

i=0
while(i<9):
    temp=jsonObject[i]["track_title"]
    temp1=jsonObject[i]["track_artist_name"]
    track_titles.append(temp)
    artist_list.append(temp1)
    i=i+1

if token:
    sp = spotipy.Spotify(auth=token)
    sp_playlist_name="New Playlist "+now.strftime("%Y-%m-%d %H:%M")
    sp.user_playlist_create(user=username,name=sp_playlist_name,public=True)
    playlist_raw=sp.current_user_playlists(limit=10,offset=0)
    playlist_jsonData=json.dumps(playlist_raw)
    playlist_jsonObject=json.loads(playlist_jsonData)
    
    tracks=[]
    for i in range(0,9):
        q="track:"+track_titles[i]
        sp_track=sp.search(q=q,limit=10,offset=0,type='track')
        sp_jsonData=json.dumps(sp_track,sort_keys=True,indent=4)
        sp_jsonObject=json.loads(sp_jsonData)
        print(playlist_jsonData)
    
        track_ID=sp_jsonObject["tracks"]["items"][0]["id"]
        print(track_ID)
    
        tracks.append(track_ID)
    x=0
    while x<9:
        if playlist_jsonObject["items"][x]["name"]==sp_playlist_name:
            playlist_ID=playlist_jsonObject["items"][x]["id"]
            sp.user_playlist_add_tracks(user=username,playlist_id=playlist_ID,tracks=tracks)
        else:
            pass
        x=x+1
else:
    print('lol')

print(track_titles)