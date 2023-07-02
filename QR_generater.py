import pyqrcode
from pyqrcode import QRCode

s = "https://www.youtube.com/channel/UCgUssfwWVUePPAcVRwe23nA"

url = pyqrcode.create(s)

url.svg("youtube.svg", scale = 8)
