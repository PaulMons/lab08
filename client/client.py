import urllib.request

test = urllib.request.urlopen("http://localhost:2288/")

encodedContent = test.read()
decodedContent = encodedContent.decode("utf8")

print(decodedContent)

test.close()
