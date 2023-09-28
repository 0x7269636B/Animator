import pytesseract
from PIL import Image

# Open the image using PIL
image = Image.open('book.jpeg')

# Convert the image to grayscale
image = image.convert('L')

# Use pytesseract to get the text from the image
text = pytesseract.image_to_string(image)

# Print the text
print(text)