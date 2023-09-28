import openai
import io
from PIL import Image
import requests
import pytesseract

#API : Application Programming Interface
openai.api_key = "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"

# Open the image using PIL
image = Image.open('image.png')

# Convert the image to grayscale
image = image.convert('L')

# Use pytesseract to get the text from the image
query = pytesseract.image_to_string(image)

print(query)

image_name = "coral.jpg"
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

# Download the image from the URL
image_data = requests.get(image_url).content

# Open the image using PIL
image = Image.open(io.BytesIO(image_data))

# Save the image as a JPEG file
image.save(image_name)

print("Image saved as "+ image_name)