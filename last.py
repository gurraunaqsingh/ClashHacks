import pylast

API_KEY='da55887adc0cfc0403f1695a734b7905'
API_SECRET='b8aadda8b55c0bf1ad2db1d4754a7348'

username="manjogsingh"
password_hash=pylast.md5("01.Hahaha")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,username=username, password_hash=password_hash)

track=network.get_track("opeth","deliverance")
# now_playing=network.update_now_playing('opeth','deliverance')
print(track.get_url)