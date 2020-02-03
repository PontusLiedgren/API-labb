from PIL import Image
from io import BytesIO
import requests

response = requests.get(f'http://api.tronalddump.io/random/meme')
img = Image.open(BytesIO(response.content))
img.show()

if response:
    print('Success!')
else:
    print('An error has occurred.')