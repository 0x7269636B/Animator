import openai
import io
from PIL import Image
import requests

#API : Application Programming Interface
openai.api_key = "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"

#data input
query = "Starry night animation"
image_name = "stars.jpg"
number_of_images = 1
size1 = "256x256"
size2 = "512x512"
size3 = "1024x1024"

# create the image sending http post request and get the response
response = openai.Image.create(
  prompt=query,
  n=number_of_images,
  size=size1
)

#get the image url
image_url = response['data'][0]['url']

print(image_url)

################################################

# Download the image from the URL
image_data = requests.get(image_url).content

# Open the image using PIL
image = Image.open(io.BytesIO(image_data))

# Save the image as a JPEG file
image.save(image_name)

print("Image saved as "+ image_name)