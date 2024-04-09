# AIVOX

An easy-to-use API for generating music

# SETUP

pip install aivox

# EXAMPLE

import aivox

client = aivox.APIClient(base_url,username,usertoken)

client.login()   

response = client.playing(api_type,song_quality,song_singer,song_source)

print(response.text)

