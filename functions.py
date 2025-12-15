import secrets
import string
import data
from tkinter.filedialog import askopenfilename
import pyperclip
import os
import sys




#Function to handle app closing
def on_close():
    app.quit()
    app.destroy()
    sys.exit(0)



def resource_path(relative_path):
    """ Pfad für PyInstaller & normalen Start """
    try:
        base_path = sys._MEIPASS  # PyInstaller Temp-Ordner
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


from customtkinter import CTk

app = CTk()


#Global state and key list
state = data.state
key_list = data.key_list


#Function to reset TextBox
def reset_textbox(text_box):
    text_box.configure(state="normal")
    text_box.delete(1.0, "end")
    text_box.configure(state="disabled")
    

#Function to copy all generated keys to clipboard
def copy_keys(text_box, button):
   pyperclip.copy("\n".join(key_list))
   list_length = len(key_list)
   text_box_input(text_box=text_box, text=f"\n\nSuccessfully copied {list_length} keys!\n\n")
   text_box.see("end")
   

#Function to select file location to save keys
def file_location(text_box, button=None):
    
    path = askopenfilename(filetypes=[("Text Files", "*.txt")], title="Select a text file to save the keys")

    if path == "":
       path = "No Path selected"

    text_box_input(text_box=text_box, text=f"\nSelected File Path: {path}\n\n" )

    text_box.see("end")

    state["file_path"] = path
    if path != "":
      button.configure(text="Gen and save in File")


#Function to input text into TextBox   
def text_box_input(text, text_box):
     text_box.configure(state="normal")
     text_box.insert("end", text)
     text_box.configure(state="disabled")


#Random Key Generator function
def random_key(length=10, prefix="", suffix="", quantity=2, format="Upper", number_letter="Random", remove_dash=False, text_box=None, numbered_keys=False, file_path=None):
  key_list.clear()
  if file_path is None:
     file_path = state["file_path"]

     
  dash1 = ""
  dash2 = ""

  if quantity == "" or quantity == "0":
    quantity = 1
  elif int(quantity) > 999999:
     text_box_input(text="\nError: Highest Amount is 999999 Keys\n\n", text_box=text_box)
     return
  
  if length == "" or length == "0":
     length = 10
  elif int(length) > 100:
     text_box_input(text="\nError: Highest length for keys is 100\n\n", text_box=text_box)
     return
        
  for i in range(int(quantity)):
    random_license = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(int(length)))

    if number_letter == "Only Numbers":
      random_license = ''.join(secrets.choice(string.digits) for _ in range(int(length)))

    if number_letter == "Only Letters":
      random_license = ''.join(secrets.choice(string.ascii_letters) for _ in range(int(length)))

    if format == "Uppercase":
      random_license = random_license.upper()

    elif format == "Lowercase":
      random_license = random_license.lower()

    if prefix != "":
       dash1 = "-"
    if suffix != "":
       dash2 = "-"

    if remove_dash == True:
      dash1 = ""
      dash2 = ""
    
    i = i + 1

    if numbered_keys == True:
       random_key = f"{i}. " + prefix + dash1 + random_license + dash2 + suffix

    else:
        random_key = prefix + dash1 + random_license + dash2 + suffix

    key_list.append(random_key)

    text_box_input(text=f"{random_key}\n", text_box=text_box)

    text_box.see("end")

  if file_path != "":
    file = open(file_path, "a")
    #Write all keys to file
    for x in range(int(quantity)):
      file.write(f"{key_list[x]}\n")

    file.close()  
