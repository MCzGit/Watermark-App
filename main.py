from tkinter import ttk, StringVar
from ttkthemes import ThemedTk
from watermark_app import WatermarkAPP

#Global Variables are fonts and their color.

FONT = "Garamond"
BGCOLOR = "#EEEEEE"
FONTCOLOR = "#4B0082"
SELECTED_COLOR = "#F8485E"


def photoUPLOAD():
    #Calls the photoUPLOAD function from the WatermarkerAPP 
    #Directs the user to the next step by enabling or disabling the buttons on the GUI
    #Also changes the color of the font in the GUI to further direct the user

    WatermarkApp.photoUPLOAD()
    photo_upload_button.config(state='disabled')
    watermarkTEXT.config(state='!disabled')
    select_watermark_color.config(state='!disabled')
    watermark_confirm_button.config(state='!disbaled')
    stepONE.config(foreground=FONTCOLOR)
    stepTWO.config(foreground=SELECTED_COLOR)
    stepTHREE.config(foreground=FONTCOLOR)


def watermark():
    #This retrieves the text from the entry in the GUI, the text color, and passes it to the WatermarkAPP class.
    #Directs the user to the next step by enabling or disabling the buttons on the GUI
    #Also changes the color of the font in the GUI to further direct the user

    text = watermarkTEXT.get()
    if len(text) == 0:
        raise Exception("Please provide your text.")
    color = watermark_color.get()
    WatermarkApp.watermark(text)
    WatermarkApp.select_watermark_color(color)
    select_watermark_color.config(state='disabled')
    watermark_confirm_button.config(state='disbaled')
    watermarkTEXT.config(state='disabled')
    for radio_button in radio_buttons:
        radio_button.config(state='!disabled')
        radio_button.config(state='s.TRadiobutton')
    location_confirm_button.config(state='!disabled')
    stepTWO.config(foreground=FONTCOLOR)
    stepTHREE.config(foreground=SELECTED_COLOR)


def watermark_location():
    #This retrieves the location of where the user wants the Watermark placed.
    #Directs the user to the next step by enabling or disabling the buttons on the GUI
    #Also changes the color of the font in the GUI to further direct the user

    location = select_location.get()
    print(location)
    if location == "":
        raise Exception("Please choose a location for your watermark!")
    WatermarkApp.watermark_location(location)
    for radio_button in radio_buttons:
        radio_button.config(state='!disabled')
        radio_button.config(state='s.TRadiobutton')
    location_confirm_button.config(state='!disabled')
    confirm_watermark.config(state='!disabled')
    stepTHREE.config(foreground=FONTCOLOR)
    final_step.config(foreground=SELECTED_COLOR)


def set_watermark():
    #Calls the set_watermark function from the WATERMARKAPP class.
    #After the app is done running, the GUI window is closed.

    window.destroy()
    WatermarkApp.set_watermark()


#The main GUI Window is created using a TK Theme.

window = ThemedTk(theme='default')
window.title("The Watermark App")
window.config(padx=50, pady=50, bg=BGCOLOR)

#Enabling the WATERMARKAPP class

WatermarkApp = WatermarkAPP()


#Title heading for the app

app_title = ttk.Label(
    text="Watermark Your Photo",
    background=BGCOLOR,
    foreground=FONTCOLOR,
    font=("Verdana", 40)
)
app_title.grid(column=0, row=0, pady=(0,30))


#Step One, photo upload, label, and button

stepONE = ttk.Label(
    text="Step 1. Upload your photo",
    background=BGCOLOR,
    foreground=SELECTED_COLOR,
    font=(FONT, 14)
)
stepONE.grid(column=0, row=1, pady=10, sticky="w")
photo_upload_button = ttk.Button(text="Upload Photo", command=photoUPLOAD)
photo_upload_button.grid(column=0, row=2, sticky="w")


#Step Two, input text for watermark

stepTWO = ttk.Label(
    text="Step 2. Enter the text for your Watermark and choose the text color",
    background=BGCOLOR,
    foreground=FONTCOLOR,
    font=(FONT, 14)
)
stepTWO.grid(column=0, row=3, pady=(20,10), sticky="w")
watermarkTEXT = ttk.Entry(width=25)
watermarkTEXT.grid(column=0, row=4, sticky="w")
watermarkTEXT.config(state="disabled")
watermark_color = StringVar()
select_watermark_color = ttk.Combobox(window, textvariable=watermark_color)
select_watermark_color.config(values=("Black", "Azure", "Blue", "Chartreuse Green", 
                                      "Cyan", "Green", "Magenta", "Orange", "Red", 
                                      "Rose", "Spring Green", "Violet", "White", 
                                      "Yellow"), state="readonly")
select_watermark_color.config(state="disabled")
select_watermark_color.set("Black")
select_watermark_color.grid(column=0, row=4, sticky="e")
watermark_confirm_button = ttk.Button(text="Confirm Watermark Text", command=watermark)
watermark_confirm_button.grid(column=0, row=5, pady=(10,0), sticky="w")
watermark_confirm_button.config(state="disabled")


#Step three - The user will choose the location the watermark will be placed. 
#The possible options are provided by the Radio Buttons

stepTHREE = ttk.Label(
    text="Step 3. Where would you like to place your watermark?",
    background=BGCOLOR,
    foreground=FONTCOLOR,
    font=(FONT, 14)
)
stepTHREE.grid(column=0, row=6, pady=(20,10), sticky="w")
button_style = ttk.Style()
button_style.configure("u.TRadiobutton", background=BGCOLOR, foreground=FONTCOLOR)
button_style.configure("s.TRadiobutton", background=BGCOLOR, foreground=SELECTED_COLOR)
select_location = StringVar()

center = ttk.Radiobutton(
    window, 
    text="Center",
    variable=select_location,
    value="Center",
    style="u.TRadiobutton"
)
center.grid(column=0, row=7, sticky="w")
center.config(state="disabled")

upperLEFT = ttk.Radiobutton(
    window, 
    text="Upper-Left",
    variable=select_location,
    value="Upper-Left",
    style="u.TRadiobutton"

)
upperLEFT.grid(column=0, row=8, sticky="w")
upperLEFT.config(state="disabled")

bottomLEFT = ttk.Radiobutton(
    window, 
    text="Bottom-Left",
    variable=select_location,
    value="Bottom-Left",
    style="u.TRadiobutton"
)
bottomLEFT.grid(column=0, row=9, sticky="w")
bottomLEFT.config(state="disabled")

upperRIGHT = ttk.Radiobutton(
    window, 
    text="Upper-Right",
    variable=select_location,
    value="Upper-Right",
    style="u.TRadiobutton"
)
upperRIGHT.grid(column=0, row=10, sticky="w")
upperRIGHT.config(state="disabled")

bottomRIGHT = ttk.Radiobutton(
    window, 
    text="Bottom-Right",
    variable=select_location,
    value="Bottom-Right",
    style="u.TRadiobutton"
)
bottomRIGHT.grid(column=0, row=11, sticky="w")
bottomRIGHT.config(state="disabled")

radio_buttons = [
    center,
    upperLEFT,
    bottomLEFT,
    upperRIGHT,
    bottomRIGHT
]

location_confirm_button = ttk.Button(text="Confirm location of your watermark", command=watermark_location)
location_confirm_button.grid(column=0, row=12, pady=(10, 0), sticky="w")
location_confirm_button.config(state="disabled")


#The final step is to conclude the process by clicking the button to retrieve your watermarked image.
#The watermarked image is saved to your current directory as "watermarked_img.png"

final_step = ttk.Label(
    text="Step 4. Click the button below to retrieve and save your watermarked image!",
    background=BGCOLOR,
    foreground=FONTCOLOR,
    font=(FONT, 14)
)
final_step.grid(column=0, row=13, pady=(20,10), sticky="w")

confirm_watermark = ttk.Button(text="Watermark Your Image!", command=set_watermark)
confirm_watermark.grid(column=0, row=14, sticky="w")
confirm_watermark.config(state="disabled")

window.mainloop()
















    


