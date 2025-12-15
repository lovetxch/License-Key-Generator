from customtkinter import CTkFrame, CTkButton, CTkEntry, CTkTextbox, CTk, CTkSwitch, CTkOptionMenu

app = CTk()

#Class to create Frames
class FrameGui(CTkFrame):
    def __init__(self,
                master=app,
                width=500, height=40,
                fill="both",
                anchor="center",
                padx=5, pady=5,
                fg_color="",
                side=None,
                border_width=1):
        super().__init__(master=master,
                        fg_color=fg_color,
                        width=width, height=height,
                        border_width=border_width)
        
        self.pack(fill=fill, side=side, pady=pady, padx=padx, anchor=anchor)

#Class to create Buttons
class ButtonGui(CTkButton):
    def __init__(self, master,
                  width, 
                  anchor=None,
                  padx=5, pady=5,
                  side="",
                  text="",
                  border_color="",
                  state="normal",
                  fill=None,
                  corner_radius=5,
                  fg_color="transparent",
                  border_width=1,
                  hover_color="#555555",
                  command=None):
        super().__init__(master=master,
                         width=width,
                        border_color=border_color,
                        text=text,
                        state=state,
                        corner_radius=corner_radius,
                        fg_color=fg_color,
                        border_width=border_width,
                        hover_color=hover_color,
                        command=command)

        self.pack(pady=pady, padx=padx, anchor=anchor, side=side, fill=fill)

#Class to create Entrys
class EntryGui(CTkEntry):
    def __init__(self,
                master,
                width, height,
                fill=None,
                anchor=None,
                padx=5, pady=5,
                side="",
                placeholder_text="",
                border_width=1):
        super().__init__(master=master,
                        width=width, height=height,
                        placeholder_text=placeholder_text,
                        border_width=border_width)
        
        self.pack(pady=pady, padx=padx, anchor=anchor, side=side, fill=fill)

#Class to create TextBoxes
class TextBoxGui(CTkTextbox):
    def __init__(self,
                master,
                width, height,
                anchor="center",
                side="top",
                padx=5, pady=5,
                state="disabled",
                fill=None):
        super().__init__(master=master,
                        width=width, height=height,
                        state=state,
                        border_width=1)
        
        self.pack(anchor=anchor, side=side, padx=padx, pady=pady, fill=fill)

#Class to create Switches
class SwitchGui(CTkSwitch):
    def __init__(self,
                master,
                text="",
                width=20, height=20,
                anchor="center",
                side="top",
                padx=5, pady=5,
                onvalue=True, offvalue=False):
        super().__init__(master=master,
                        text=text,
                        width=width, height=height,
                        onvalue=onvalue, offvalue=offvalue)
        
        self.pack(anchor=anchor, side=side, padx=padx, pady=pady)        

class OptionMenuGui(CTkOptionMenu):
    def __init__(self,
                master,
                values=[],
                width=40, height=25,
                anchor="center",
                side="left",
                pady=5, padx=5,
                fg_color="#343738",
                button_color="#3F3F3F", button_hover_color="#525252"):
        super().__init__(master=master,
                        values=values,
                        width=width, height=height,
                        fg_color=fg_color,
                        button_color=button_color, button_hover_color=button_hover_color)
        
        self.pack(anchor=anchor, side=side, pady=pady, padx=padx)
