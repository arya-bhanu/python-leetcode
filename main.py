import base64


class Codec:

    def __init__(self):
        self.dict = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        encoded = base64.b64encode(longUrl.encode("ascii")).decode("ascii")
        self.dict[encoded] = longUrl
        return encoded

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        if shortUrl in self.dict:
            return self.dict[shortUrl]

        return base64.b64decode(shortUrl.encode("ascii")).decode("ascii")


# Your Codec object will be instantiated and called as such:
url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
encoded = codec.encode(url)
print(encoded)
print(codec.decode(encoded))
