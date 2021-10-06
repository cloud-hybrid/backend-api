from base64 import b64encode

class Card(object):
    def __init__(self, data: dict):
        self.name = data.get("Display-Name", "N/A")
        self.phone = data.get("Phone", "N/A")
        self.bio = data.get("Biography", "N/A")
        self.joindate = data.get("Joined", "N/A")
        self.avatar = b64encode(data.get(bytes("Image".encode("UTF-8")), bytes("N/A".encode("UTF-8")))).decode("UTF-8")