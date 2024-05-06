import melodicious

client = melodicious.APIClient(base_url='', username='', usertoken='', callEndpoint='', configs='')

response = client.playing()

print(response)
