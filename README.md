# AIVOX

An easy-to-use API for generating music

# SETUP

pip install aivox

# EXAMPLE

client = aivox.APIClient(base_url="https://example.com")

response = client.playing("username", "password", "/endpoint", {"key": "value"})

