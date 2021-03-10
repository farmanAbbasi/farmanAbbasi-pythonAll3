'''

from PIL import Image
import urllib.request

URL = 'https://i.picsum.photos/id/200/300/300.jpg?hmac=aX7NyPgACwrm5XddShN5y4dyKI--2Wx_YFthk6YtBVc'

with urllib.request.urlopen(URL) as url:
    with open('temp.jpg', 'wb') as f:
        f.write(url.read())

img = Image.open('temp.jpg')

img.show()


'''
#create object in memory
from PIL import Image
import urllib.request
import io

URL = 'http://www.w3schools.com/css/trolltunga.jpg'

with urllib.request.urlopen(URL) as url:
    f = io.BytesIO(url.read())

img = Image.open(f)

img.show()
