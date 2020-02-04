from PIL import Image
from io import BytesIO
import requests

response = requests.get('http://api.tronalddump.io/random/meme')

if response.status_code == requests.codes.ok:
    img = Image.open(BytesIO(response.content))
    img.show()
    print("Success!")
else:
    print('An error has occurred.')