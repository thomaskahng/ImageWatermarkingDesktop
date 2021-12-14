from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

class Components:
    def __init__(self, window):
        # Set up window
        self.window = window
        self.set_window()

        # Set up image and watermark logo
        self.image = Image.open("download.jpg")
        self.image.save('download.jpg')
        self.image = self.image.resize((300, 300))
        self.set_watermark()

        # Display image
        self.tkimage = ImageTk.PhotoImage(self.image)
        self.display_image()

    def set_window(self):
        self.window.title("Image Watermarking Desktop")
        self.window.config(padx=100, pady=50)

    def set_watermark(self):
        # Image to draw, text to watermark, and dimensions of image
        draw = ImageDraw.Draw(self.image)
        text = "Puerto Rico"
        width, height = self.image.size

        # Get font and size of font
        font = ImageFont.truetype('arial.ttf', 12)
        textwidth, textheight = draw.textsize(text, font)

        # Calculate the x,y coordinates of the text
        x = width - textwidth - 10
        y = height - textheight - 10

        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font, fill="#e7305b")
        self.image.save('download.jpg')

    def display_image(self):
        label = Label(self.window, image=self.tkimage)
        label.pack()