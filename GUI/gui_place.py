from GUI.gui import FrameGui, ButtonGui, TextBoxGui, EntryGui, SwitchGui, OptionMenuGui
import customtkinter as CTk




class PlaceGUI():
    def __init__(self, random_key, copy_keys, reset_textbox, file_location, more_features, app_width, app):
        #------Main Background Frame------
        main_background_frame = FrameGui(master=app, fg_color="#2E2E2E", fill="both")

        #------First Section Background Frames------
        first_section_frame = FrameGui(master=main_background_frame, fg_color="transparent", fill="x")
        key_setup_frame = FrameGui(master=first_section_frame, fg_color="transparent", fill="x", border_width=0, pady=5, padx=1)
        key_params_frame = FrameGui(master=first_section_frame, fg_color="transparent", fill="x", border_width=0, pady=5, padx=1, height=30)

        #-----Extra Features Frame------
        if more_features is True:
            first_section_more_features = FrameGui(master=first_section_frame, fg_color="transparent", fill="x", border_width=0, pady=5, padx=1, height=30)
            app.geometry(f"{app_width}x444")



        #------Second Section Background Frame------
        second_section_frame = FrameGui(master=main_background_frame, fg_color="transparent", fill="both", height=400, pady=0)

        #------Third Section Background Frame------
        third_section_frame = FrameGui(master=main_background_frame, fg_color="transparent", fill="both", height=35)
        gen_key_button_frame = FrameGui(master=third_section_frame, fg_color="transparent", fill="y", side="left", pady=2, padx=2, width=35, border_width=0)
        copy_key_button_frame = FrameGui(master=third_section_frame, fg_color="transparent", fill="y", side="left", pady=2, padx=2, width=120, border_width=0)
        clear_key_button_frame = FrameGui(master=third_section_frame, fg_color="transparent", fill="y", side="left", pady=2, padx=2, width=120, border_width=0)
        save_loc_button_frame = FrameGui(master=third_section_frame, fg_color="transparent", fill="y", side="left", pady=2, padx=2, width=50, border_width=0)


        #------Entries------
        first_entry = EntryGui(master=key_setup_frame, width=170, height=30, side="left", anchor="center", pady=2, placeholder_text="Prefix: Key's front text")
        second_entry = EntryGui(master=key_setup_frame, width=170, height=30, side="left", anchor="center", pady=2, placeholder_text="Suffix: Key's back text")
        third_entry = EntryGui(master=key_setup_frame, width=100, height=30, side="left", anchor="center", pady=2, placeholder_text="Key Length")
        five_entry = EntryGui(master=key_setup_frame, width=100, height=30, side="left", anchor="center", pady=2, placeholder_text="Key Amount")




        #------TextBox------
        text_box = TextBoxGui(master=second_section_frame, width=450, height=248, pady=5, fill="y")


        #----Switches----
        remove_dash_switch = SwitchGui(master=key_params_frame, text="Remove Dash", anchor="center", side="left", padx=17, pady=1)
        numbered_keys = SwitchGui(master=key_params_frame, text="Numbered Keys", anchor="center", side="left", padx=17, pady=1)

        #----Menu-----
        format_menu = OptionMenuGui(master=key_params_frame, values=["Uppercase", "Lowercase", "Random"], side="right", padx=5, pady=1)
        number_letter_menu = OptionMenuGui(master=key_params_frame, values=["Letters & Numbers", "Only Letters", "Only Numbers"], side="right", padx=5, pady=1)



        #------Generate Button------
        generate_key_button = ButtonGui(master=gen_key_button_frame,
                                        text="Generate Key",
                                        fill="y", width=180, 
                                        side="right", anchor="center", 
                                        pady=2, padx=2, 
                                        border_width=1, 
                                        command=lambda: random_key(text_box=text_box,
                                                                    quantity=five_entry.get(), 
                                                                    length=third_entry.get(), 
                                                                    format=format_menu.get(),
                                                                    prefix=first_entry.get(),
                                                                    suffix=second_entry.get(),
                                                                    remove_dash=remove_dash_switch.get(),
                                                                    numbered_keys=numbered_keys.get(),
                                                                    number_letter=number_letter_menu.get(),
                                                                    ))


        #------Copy, Clear, Save Location Buttons------
        copy_key_button = ButtonGui(master=copy_key_button_frame, text="Copy Keys", fill="y", width=155, side="right", anchor="center", pady=2, padx=2, border_width=1, command=lambda: copy_keys(text_box=text_box, button=generate_key_button))
        clear_key_button = ButtonGui(master=clear_key_button_frame, text="Clear Keys", fill="y", width=155, side="right", anchor="center", pady=2, padx=2, border_width=1, command=lambda: reset_textbox(text_box))
        save_location = ButtonGui(master=save_loc_button_frame, text="💾", fill="y", width=50, side="right", anchor="center", pady=2, padx=2, border_width=1, command=lambda: file_location(text_box=text_box, button=generate_key_button))


