from PIL import Image, ImageDraw, ImageFont, ImageOps, UnidentifiedImageError
from tkinter import filedialog

class WatermarkAPP:
    #The watermark app's funcationality is enclosed in this class.
    def __init__(self):
        self.original_image = None
        self.watermarkTEXT = None
        self.watermarkLOCATION = None
        self.watermark_submitted = False
        self.watermark_color = None

    
    def photoUPLOAD(self):
        #Tkinter is used so the user may choose the photo they wish to upload.
        #If the file is not an image file, then an exception will be raised.

        f = filedialog.askopenfilename()
        try:
            img = Image.open(f).convert("RGBA")
            self.original_image = ImageOps.exif_transpose(img)
        except UnidentifiedImageError:
            raise Exception("Error! The file you have chosen is not an image file. Please try again.")
        
    
    def watermark(self, text):
        self.watermarkTEXT = text
        self.watermark_submitted = True


    def watermark_location(self, location):
        self.watermarkLOCATION = location


    def place_watermark_location(self, img_width, img_height, watermark_width, watermark_height,):
        #Uses the original image's height and width, and the watermark's height and width as arguements.
        #The watermark location attribute is returned to (x) and (y) for locating the placement of the watermark.

        margin = 20

        if self.watermarkLOCATION == "Center":
            x = (img_width / 2) - (watermark_width / 2)
            y = (img_height / 2) - (watermark_height / 2)

        elif self.watermarkLOCATION == "Upper-Left":
            x = margin
            y = margin
        
        elif self.watermarkLOCATION == "Bottom-Left":
            x = margin
            y = img_height - watermark_height - margin

        elif self.watermarkLOCATION == "Upper-Right":
            x = img_width - watermark_width - margin
            y = margin

        elif self.watermarkLOCATION == "Bottom-Right":
            x = img_width - watermark_width - margin
            y = img_height - watermark_height - margin
        
        else:
            raise Exception("Sorry! Something went wrong. Restart the application and try again.")
        
        return int(x), int(y)
    

    def select_watermark_color(self, color):
        #Uses a string as an argument to set the color of the watermark using RGBA values.
        #The alpha is set to 128 for 50% opacity
        
        if color == "Black":
            self.watermark_color = (0, 0, 0, 128)
        elif color == "Azure":
            self.watermark_color = (240, 255, 255, 128)
        elif color == "Blue":
            self.watermark_color =  (0, 0, 255, 128)
        elif color == "Chartreuse Green":
            self.watermark_color = (127, 255, 0, 128)
        elif color == "Cyan":
            self.watermark_color = (0, 255, 255, 128)
        elif color == "Green":
            self.watermark_color = (0, 128, 0, 128)
        elif color == "Magenta":
            self.watermark_color = (255, 0, 255, 128)
        elif color == "Orange":
            self.watermark_color = (255, 165, 0, 128)
        elif color == "Red":
            self.watermark_color = (255, 0, 0, 128)
        elif color == "Rose":
            self.watermark_color = (255, 0, 127, 128)
        elif color == "Spring Green":
            self.watermark_color = (0, 255, 127, 128)
        elif color == "Violet":
            self.watermark_color = (238, 130, 238, 128)
        elif color == "White":
            self.watermark_color = (255, 255, 255, 128)
        elif color == "Yellow":
            self.watermark_color = (255, 255, 0, 128)


    def set_watermark(self):
        #The Pillow library is used here to create the watermark.
        
        img_width, img_height = self.original_image.size

        if self.watermark_submitted:
            img_overlay = Image.new("RGBA", (img_width, img_height), (255, 255, 255, 0))
            write = ImageDraw.Draw(img_overlay)
            text = self.watermarkTEXT
            text_size = int(((img_width + img_height) / 2) // 12)
            text_font = ImageFont.truetype("Palatino.ttc", text_size)
            watermark_width, watermark_height = write.textsize(text, text_font)
            x, y = self.place_watermark_location(img_width, img_height, watermark_width, watermark_height)
            write.text((x, y), text, font=text_font, fill=self.watermark_color)
            watermarked_img = Image.alpha_composite(self.original_image, img_overlay)
        
        else:
            raise Exception("Sorry! Something went wrong. Restart the application and try again.")
        

        #The user is shown the watermark image and it is saved in the current directory.
        
        watermarked_img.show()
        watermarked_img.save("watermarked_img.png")
        




        

        
        
        
        


        


