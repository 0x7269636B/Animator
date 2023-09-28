import openai
import nltk
import io
from PIL import Image
import requests
import pytesseract

#nltk.download('punkt')

#API : Application Programming Interface
openai.api_key = "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"

# Open the image using PIL
image = Image.open('book.jpeg')

# Convert the image to grayscale
image = image.convert('L')

# Use pytesseract to get the text from the image
paragraph = pytesseract.image_to_string(image)

#paragraph = "The story begins with the discovery of the One Ring by Bilbo Baggins, a hobbit who goes on an adventure in The Hobbit. Bilbo leaves the Ring to his nephew, Frodo Baggins, and instructs him to keep it safe. Gandalf the wizard becomes aware of the true nature of the Ring and urges Frodo to leave his home, the Shire, to protect it from falling into the hands of Sauron."

number_of_images = 1
size1 = "256x256"
size2 = "512x512"
size3 = "1024x1024"

sentences = nltk.sent_tokenize(paragraph)
i = 0

for sentence in sentences:
    i = i + 1
    image_name = "Harry_Potter_"+str(i)+".jpg"
    print(sentence)
    query = sentence
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