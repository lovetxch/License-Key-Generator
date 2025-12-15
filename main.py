from customtkinter import CTk
from PIL import Image
import pyperclip

from GUI.gui_place import PlaceGUI
from functions import reset_textbox, text_box_input, random_key, file_location, copy_keys, resource_path, on_close
from data import state


#Set this to true for extra features space in the header
more_features = False


app = CTk()

#Set the protocol for window closing
app.protocol("WM_DELETE_WINDOW", on_close)

#App dimensions
app_height = "404"
app_width = "600"
app.geometry(f"{app_width}x{app_height}")
app.resizable(False, False)

#App Title and Icon
app.title("License Key Generator | By Lovex")
app.iconbitmap(resource_path("exe_icon.ico"))

#Place all GUI elements
PlaceGUI(random_key=random_key,
         copy_keys=copy_keys,
         reset_textbox=reset_textbox,
         file_location=file_location,
         more_features=more_features,
         app_width=app_width,
         app = app)



app.mainloop()
 