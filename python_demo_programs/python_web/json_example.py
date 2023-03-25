import json
from io import BytesIO
import requests
from PIL import Image

response = requests.get("https://dog.ceo/api/breeds/image/random")
if response.ok:
    data = response.json()

response = requests.get(data["message"])
f = BytesIO(response.content)
im = Image.open(f)
im.show()