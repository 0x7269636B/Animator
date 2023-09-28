import tkinter as tk
import cv2
from PIL import Image, ImageTk

class CameraApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Camera App")

        # Create a canvas for displaying the camera feed
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        # Create a button for taking pictures
        self.button = tk.Button(window, text="Take Picture", command=self.take_picture)
        self.button.pack()

        # Initialize the camera
        self.cap = cv2.VideoCapture(0)

        # Check if the camera is opened successfully
        if not self.cap.isOpened():
            print("Error opening camera")
            exit()


        # Start the camera feed
        self.update()

    def update(self):
        # Get a frame from the camera
        ret, frame = self.cap.read()

        if ret:
            # Convert the frame to an image that can be displayed on the canvas
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)

            # Update the canvas with the new image
            self.canvas.create_image(0, 0, anchor=tk.NW, image=image)
            self.canvas.image = image

        # Schedule the next update
        self.window.after(15, self.update)

    def take_picture(self):
        # Get a frame from the camera
        ret, frame = self.cap.read()

        if ret:
            # Save the frame as an image file
            cv2.imwrite("picture.jpg", frame)

# Create the main window
window = tk.Tk()

# Create the camera app
app = CameraApp(window)

# Start the main event loop
window.mainloop()