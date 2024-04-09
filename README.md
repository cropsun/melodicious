# AVIOX

An easy-to-use API for generating music

# SETUP

pip install aivox

# EXAMPLE

client = APIClient(base_url="http://melodicious.com")
response = client.play("username", "password", "/endpoint", {"key": "value"})
print(response)
