# AIVOX

An easy-to-use API for generating music

# SETUP

pip install melodicious

# EXAMPLE

import melodicious

client = melodicious.APIClient(base_url, username, usertoken, callEndpoint, data)

response = client.playing()

print(response)