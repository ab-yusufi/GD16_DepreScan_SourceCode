import tkinter
import tkinter.messagebox
import customtkinter
import time
import numpy as np

import cv2
from pygame import mixer
import random
import math
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc

# 
import database as db
import create_fpdf as pdf

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
is_on = True



class data_store:
    response1 = "0"
    response2 = "0"
    response3 = "0"
    enthu_val = 0
    opti_val = 0
    dep_anx_val = 0
    student_name = ""
    student_age = ""
    student_phone = ""
    student_gender = ""
    flag= 0
    admin_mail = "siddhantindave@icloud.com"
    student_mail = ""
    name_flag = 0
    phq_questions = [
        " Over the last 2 weeks, \nhow often have you been bothered \nby any of the following problems?\n 1. Little interest or pleasure in \ndoing things?",
        "2. Feeling down, depressed, or hopeless?",
        "3. Trouble falling or staying asleep, \nor sleeping too much?",
        "4. Feeling tired or having little energy?", 
        "5. Poor appetite or overeating?", 
        "6. Feeling bad about yourself or \nthat you are a failure\n or have let yourself or your family down?", 
        "7. Trouble concentrating on things, \nsuch as reading the newspaper or \nwatching television?", 
        "8. Moving or speaking so slowly \nthat other people could have noticed. \nOr the opposite being so fidgety \nor restless that you have been\n moving around a lot more than usual?",
        "9. Thoughts that you would be better off dead,\n or of hurting yourself?"
        ]
    phq_responses = []
    phq_score = 0

class App(customtkinter.CTk):

    #NOTE: Changed from 780 to 830
    WIDTH = 830
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Depression Detector")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        # self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        #NOTE:ADDED
        self.frame_left.grid_rowconfigure(9, minsize=200)  # empty row as spacing
        # self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        # self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="DepreScan Bot",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_left,
                                                        text="Patient Details",
                                                        text_font=("Poppins", -16))
        self.label_radio_group.grid(row=2, column=0, columnspan=1, pady=20, padx=10, sticky="")
        #NOTE:ADDED
        self.label_patient_name = customtkinter.CTkLabel(master=self.frame_left,
                                                        text="")
        self.label_patient_name.grid(row=3, column=0, columnspan=1, pady=0, padx=10, sticky="")
        self.label_patient_email = customtkinter.CTkLabel(master=self.frame_left,
                                                        text="")
        self.label_patient_email.grid(row=4, column=0, columnspan=1, pady=0, padx=10, sticky="")
        self.label_patient_age = customtkinter.CTkLabel(master=self.frame_left,
                                                        text="")
        self.label_patient_age.grid(row=5, column=0, columnspan=1, pady=0, padx=10, sticky="")
        self.label_patient_phone = customtkinter.CTkLabel(master=self.frame_left,
                                                        text="")
        self.label_patient_phone.grid(row=6, column=0, columnspan=1, pady=0, padx=10, sticky="")
        
        self.label_patient_gender = customtkinter.CTkLabel(master=self.frame_left,
                                                        text="")
        self.label_patient_gender.grid(row=7, column=0, columnspan=1, pady=0, padx=10, sticky="")

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=10, column=0, pady=0, padx=30, sticky="w")

        

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=11, column=0, pady=0, padx=30, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Please enter your name to begin",
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right ============

        # self.radio_var = tkinter.StringVar(value="Male")

        # self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
        #                                                 text="Patient Details")
        # self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=0, padx=10, sticky="")
        # self.label_patient_name = customtkinter.CTkLabel(master=self.frame_right,
        #                                                 text="Name: Abdurrahman Yusufi")
        # self.label_patient_name.grid(row=1, column=2, columnspan=1, pady=0, padx=10, sticky="")
        # self.label_patient_email = customtkinter.CTkLabel(master=self.frame_right,
        #                                                 text="Email: yabdurrahman478@gmail.com")
        # self.label_patient_email.grid(row=2, column=2, columnspan=1, pady=0, padx=10, sticky="")
        # self.label_patient_phone = customtkinter.CTkLabel(master=self.frame_right,
        #                                                 text="Phone Number: 1234567890")
        # self.label_patient_phone.grid(row=3, column=2, columnspan=1, pady=0, padx=10, sticky="")
        self.radio_var = tkinter.StringVar(value="")

        self.qOptions = tkinter.StringVar(value="")
       
        
        self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
                                                from_=0,
                                                to=1,
                                                number_of_steps=3,
                                                command=self.progressbar.set)

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_right,
                                                text="E-mail Report to me", command= studmail())
        self.switch_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120)
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.radiobutton_1 = customtkinter.CTkRadioButton(master=self.frame_right, text="Male",
                                             command=self.button_event, variable=self.radio_var, value="Male")
        self.radiobutton_2 = customtkinter.CTkRadioButton(master=self.frame_right, text="Female",
                                             command=self.button_event, variable= self.radio_var, value="Female")
        
        self.qOption1 = customtkinter.CTkRadioButton(master=self.frame_right, text="Not at all",
                                             command=self.button_event, variable= self.qOptions, value="Not at all")
        self.qOption2 = customtkinter.CTkRadioButton(master=self.frame_right, text="Several Days",
                                             command=self.button_event, variable= self.qOptions, value="Several Days")
        self.qOption3 = customtkinter.CTkRadioButton(master=self.frame_right, text="More than half the days",
                                             command=self.button_event, variable= self.qOptions, value="More than half the days")
        self.qOption4 = customtkinter.CTkRadioButton(master=self.frame_right, text="Nearly Everyday",
                                             command=self.button_event, variable= self.qOptions, value="Nearly Everyday")
        
        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Enter",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")
        self.entry.bind('<Return>',lambda event: self.button_event())
        # set default values
        self.optionmenu_1.set("Dark")

        self.progressbar.set(0.0)
        self.entry.focus()
########################################################################################################################

    def button_event(self):
        myVal = self.radio_var.get()
        user=""
        # print("RADIO VAL")
        # print(myVal)
        print("SELF.ENTRY")
        print((type(self.entry)))
        #print("Button pressed")
        
        data = self.entry.get()
        user = data.lower()


        if data_store.name_flag == 0:
            # self.entry.destroy()
            data_store.student_name = data
            print(data_store.student_name)
            data_store.name_flag += 1
            self.label_info_1.set_text("Please Enter E-mail ID"
                                       "\nMake Sure you enter it"
                                       "\nCorrectly!")
            user = ""
            self.entry.delete(0,len(data))
            self.progressbar.set(0.1)
            self.label_patient_name.configure(text=f"Name: {data_store.student_name}")

        if ".com" in user:
            data_store.student_mail = user
            # self.label_info_1.set_text("Welcome Student, "
            #                            "\nplease follow the voice instructions ahead. "
            #                            "\nType and enter OK to continue ")
            self.label_info_1.set_text("Welcome Student, "
                                       "\Please Enter your age ")
            user = ""
            print(data_store.student_name + "'s Email: ", data_store.student_mail)
            # db.saveData({"patientName":data_store.student_name,"patientEmail":data_store.student_mail,"enthusiasm":90,"depression score":50,"optimisum":70})
            self.progressbar.set(0.2)
            self.entry.delete(0,len(data))
            self.label_patient_email.configure(text=f"Email: {data_store.student_mail}")
        
        if user.isnumeric() and len(user) <= 3:
            data = self.entry.get()
            user = data.lower()
            data_store.student_age = user
            self.label_info_1.set_text("Welcome Student, "
                                       "\nPlease Enter your phone number")
            user = ""
            self.progressbar.set(0.3)
            self.entry.delete(0,len(data))
            self.label_patient_age.configure(text=f"Age: {data_store.student_age}")

        if user.isnumeric() and len(user) == 10:
            data = self.entry.get()
            user = data.lower()
            #show radio buttons
            self.radiobutton_1.grid(row=6, column=0, columnspan=2, pady=20, padx=20, sticky="we")
            self.radiobutton_2.grid(row=6, column=1, columnspan=2, pady=20, padx=20, sticky="we")
            
            # disable input
            self.entry.configure(state="disabled")
            
            #delete input box
            # self.entry.destroy()
            data_store.student_phone = user
            self.label_info_1.set_text("Welcome Student, "
                                       "\nPlease Select Your Gender")
            user = ""
            
            self.progressbar.set(0.4)
            self.entry.delete(0,len(data))
            self.label_patient_phone.configure(text=f"Phone Number: {data_store.student_phone}")
        
        if ((self.radio_var.get() == "Male" or self.radio_var.get() == "Female") and ("ok" not in user) and (data_store.flag == 0)):
            
            #disable radio buttons
            time.sleep(1)
            self.radiobutton_1.destroy()
            self.radiobutton_2.destroy()

            

            #enable input box
            self.entry.configure(state="normal")
            
            #create input box
            # self.entry = customtkinter.CTkEntry(master=self.frame_right,
            #                                 width=120)
            # self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

            data_store.student_gender = self.radio_var.get()
            print("data_store.student_gender")
            print(data_store.student_gender)
            self.label_info_1.set_text("Welcome Student, "
                                       "\nplease follow the voice instructions ahead. "
                                       "\nType and enter OK to continue ")
            user=""
            self.progressbar.set(0.5)
            self.entry.delete(0,len(data))
            self.label_patient_gender.configure(text=f"Gender: {data_store.student_gender}")
        
        if ("ok" in user) and (data_store.flag == 0):
            data_store.flag += 1
            playaudio("intro.mp3")
            time.sleep(2)
            joke_list = ("Joke_1.mp3", "Joke_2.mp3", "Joke_3.mp3", "Joke_4.mp3")
            random_joke = random.randrange(0, 4)
            joke = (joke_list[random_joke])
            playaudio(joke)
            time.sleep(2)
            import img_capture as ic
            ic.main()
            import fer_img
            fer_img.main()
            joke_reaction = fer_img.main.emotion
            print("Reaction to joke:" + joke_reaction)
            if joke_reaction == 'happy':
                data_store.enthu_val += 1
            playaudio("processing.mp3")
            user = ""
            self.label_info_1.set_text("Type and enter OK to continue.")
            self.progressbar.set(0)

        if ("ok" in user) and (data_store.flag == 1):
            data_store.flag += 1
            import test_ser
            test_ser.main()
            self.label_info_1.set_text("Type and enter OK to continue.")
            greet_response = test_ser.main.result
            if greet_response == 'happy':
                data_store.enthu_val += 1
            playaudio("processing.mp3")   
            user = ""

        if ("ok" in user) and (data_store.flag == 2):
            self.label_info_1.set_text("You will now be taken"
                                       "through an audio and video"
                                       "exercise.")
            playaudio("begin.mp3")
            time.sleep(3)
            self.label_info_1.set_text("Displaying image")
            imgpath = 'img_samples/1.jpg'
            image = cv2.imread(imgpath)
            cv2.imshow('image', image)
            k = cv2.waitKey(0) & 0xFF
            if k == 27:
                import img_capture as ic
                import fer_img
                ic.main()
                fer_img.main()
                img1_reaction = fer_img.main.emotion
                if img1_reaction == 'happy':
                    data_store.enthu_val += 1
                else:
                    data_store.dep_anx_val += 1
                cv2.destroyAllWindows()
                data_store.flag += 1
                self.label_info_1.set_text("Type and enter OK to continue.")
            user = ""

        if ("ok" in user) and (data_store.flag == 3):
            self.label_info_1.set_text("Displaying image")
            imgpath = 'img_samples/2.jpg'
            image = cv2.imread(imgpath)
            cv2.imshow('image', image)
            k = cv2.waitKey(0) & 0xFF
            if k == 27:
                import img_capture as ic
                import fer_img
                ic.main()
                fer_img.main()
                img2_reaction = fer_img.main.emotion
                if img2_reaction == 'happy':
                    data_store.enthu_val += 1
                else:
                    data_store.dep_anx_val += 1
                cv2.destroyAllWindows()
                data_store.flag += 1
                self.label_info_1.set_text("Type and enter OK to continue.")
            user = ""

        if ("ok" in user) and (data_store.flag == 4):
            self.label_info_1.set_text("Displaying image")
            imgpath = 'img_samples/3.jpg'
            image = cv2.imread(imgpath)
            cv2.imshow('image', image)
            k = cv2.waitKey(0) & 0xFF
            if k == 27:
                import img_capture as ic
                import fer_img
                ic.main()
                fer_img.main()
                img3_reaction = fer_img.main.emotion
                if img3_reaction == 'happy':
                    data_store.enthu_val += 1
                else:
                    data_store.dep_anx_val += 1
                cv2.destroyAllWindows()
                data_store.flag += 1
                self.label_info_1.set_text("Type and enter OK to continue.")
            user = ""

        if ("ok" in user) and (data_store.flag == 5):
            self.label_info_1.set_text("Displaying image")
            imgpath = 'img_samples/4.jpg'
            image = cv2.imread(imgpath)
            cv2.imshow('image', image)
            k = cv2.waitKey(0) & 0xFF
            if k == 27:
                import img_capture as ic
                import fer_img
                ic.main()
                fer_img.main()
                img3_reaction = fer_img.main.emotion
                if img3_reaction == 'happy':
                    data_store.enthu_val += 1
                else:
                    data_store.dep_anx_val += 1
                cv2.destroyAllWindows()
                data_store.flag += 1
                self.label_info_1.set_text("Type and enter OK to continue.")
            user = ""

        if ("ok" in user) and (data_store.flag == 6):
            self.label_info_1.set_text("Playing Video")
            vid1 = vlc.MediaPlayer("vid_samples/1.mp4")
            vid1.play()
            time.sleep(32)
            vid1.stop()
            import img_capture as ic
            import fer_img
            ic.main()
            fer_img.main()
            vid2_reaction = fer_img.main.emotion
            if vid2_reaction == 'happy':
                data_store.enthu_val += 1
            else:
                data_store.dep_anx_val += 1
            data_store.flag += 1
            self.label_info_1.set_text("Type and enter OK to continue.")
            user = ""

        if ("ok" in user) and (data_store.flag == 7):
            self.label_info_1.set_text("Playing Video")
            vid1 = vlc.MediaPlayer("vid_samples/2.mp4")
            vid1.play()
            time.sleep(17)
            vid1.stop()
            import img_capture as ic
            import fer_img
            ic.main()
            fer_img.main()
            vid2_reaction = fer_img.main.emotion
            if vid2_reaction == 'happy':
                data_store.enthu_val += 1
            else:
                data_store.dep_anx_val += 1
            data_store.flag += 1
            self.label_info_1.set_text("Type and enter OK to continue.")
            user = ""

        if ("ok" in user) and (data_store.flag == 8):
            self.label_info_1.set_text("Playing Video")
            vid1 = vlc.MediaPlayer("vid_samples/3.mp4")
            vid1.play()
            time.sleep(59)
            vid1.stop()
            import img_capture as ic
            import fer_img
            ic.main()
            fer_img.main()
            vid2_reaction = fer_img.main.emotion
            if vid2_reaction == 'happy':
                data_store.enthu_val += 1
            self.label_info_1.set_text("Type and enter OK to continue.")
            data_store.flag += 1
            user = ""


        if ("ok" in user) and (data_store.flag == 9):
            self.label_info_1.set_text("Initiating Questionnaire")
            playaudio("questions_intro.mp3")
            self.label_info_1.set_text("Bot: Do you think major problems "
                                       "\nimpact your life greatly?")
            playaudio("q10.mp3")
            user = ""
            data_store.flag += 1

        if ("no" in user) and (data_store.flag == 10):
            data_store.response1 = "No"
            self.label_info_1.set_text("Bot: Consider you're in a race. "
                                       "\nYou are told your opponent is faster than you. "
                                       "\nWould you still run the race?")
            data_store.opti_val += 1
            data_store.flag += 1
            playaudio("q11.mp3")
            user = ""

        elif ("yes" in user) and (data_store.flag == 10):
            data_store.response1 = "Yes"
            self.label_info_1.set_text("Bot: Consider you're in a race. "
                                       "\nYou are told your opponent is faster than you. "
                                       "\nWould you still run the race?")

            data_store.flag += 1
            playaudio("q11.mp3")
            user = ""

        if ("yes" in user) and (data_store.flag == 11):
            data_store.response2 = "Yes"
            self.label_info_1.set_text("Bot: Do you believe that you "
                                       "\nare in control of your life?")
            data_store.opti_val += 1
            data_store.flag += 1
            playaudio("q12.mp3")
            user = ""


        elif ("no" in user) and (data_store.flag == 11):
            data_store.response2 = "No"
            self.label_info_1.set_text("Bot: Do you believe that you "
                                       "\nare in control of your life?")
            data_store.flag += 1
            playaudio("q12.mp3")
            user = ""

        if ("yes" in user) and (data_store.flag == 12):
            self.entry.configure(state="disabled")
            self.qOption1.grid(row=6, column=0, columnspan=2, pady=20, padx=20, sticky="we")
            self.qOption2.grid(row=6, column=1, columnspan=2, pady=20, padx=20, sticky="we")
            self.qOption3.grid(row=7, column=0, columnspan=2, pady=20, padx=20, sticky="we")
            self.qOption4.grid(row=7, column=1, columnspan=2, pady=20, padx=20, sticky="we")
            data_store.response3 = "Yes"
            data_store.opti_val += 1
            data_store.flag += 1
            self.label_info_1.set_text(data_store.phq_questions[data_store.flag - 13])
            playaudio("phq1.mp3")
            user=""
            self.qOptions.set("")

        elif ("no" in user) and (data_store.flag == 12):
            self.entry.configure(state="disabled")
            self.qOption1.grid(row=6, column=0, columnspan=2, pady=20, padx=20, sticky="we")
            self.qOption2.grid(row=6, column=1, columnspan=2, pady=20, padx=20, sticky="we")
            self.qOption3.grid(row=7, column=0, columnspan=2, pady=20, padx=20, sticky="we")
            self.qOption4.grid(row=7, column=1, columnspan=2, pady=20, padx=20, sticky="we")
            data_store.response3 = "No"
            data_store.flag += 1
            self.label_info_1.set_text(data_store.phq_questions[data_store.flag - 13])
            playaudio("phq1.mp3")
            user=""
            self.qOptions.set("")

        if (self.qOptions.get() in ["Not at all", "Nearly Everyday", "Several Days", "More than half the days"]) and (data_store.flag == 13):
            data_store.phq_responses.append(self.qOptions.get()) 
            data_store.flag += 1
            self.label_info_1.set_text(data_store.phq_questions[data_store.flag - 13])
            playaudio("phq2.mp3")
            user=""
            self.qOption1.deselect()
            self.qOption2.deselect()
            self.qOption3.deselect()
            self.qOption4.deselect()
            self.qOptions.set("")
        
        if (self.qOptions.get() in ["Not at all", "Nearly Everyday", "Several Days", "More than half the days"]) and (data_store.flag == 14):
            data_store.phq_responses.append(self.qOptions.get()) 
            data_store.flag += 1
            self.label_info_1.set_text(data_store.phq_questions[data_store.flag - 13])
            playaudio("phq3.mp3")
            user=""
            self.qOption1.deselect()
            self.qOption2.deselect()
            self.qOption3.deselect()
            self.qOption4.deselect()
            self.qOptions.set("")
        
        if (self.qOptions.get() in ["Not at all", "Nearly Everyday", "Several Days", "More than half the days"]) and (data_store.flag == 15):
            data_store.phq_responses.append(self.qOptions.get()) 
            data_store.flag += 1
            self.label_info_1.set_text(data_store.phq_questions[data_store.flag - 13])
            playaudio("phq4.mp3")
            user=""
            self.qOption1.deselect()
            self.qOption2.deselect()
            self.qOption3.deselect()
            self.qOption4.deselect()
            self.qOptions.set("")
        if (self.qOptions.get() in ["Not at all", "Nearly Everyday", "Several Days", "More than half the days"]) and (data_store.flag == 16):
            data_store.phq_responses.append(self.qOptions.get()) 
            data_store.flag += 1
            self.label_info_1.set_text(data_store.phq_questions[data_store.flag - 13])
            playaudio("phq5.mp3")
            user=""
            self.qOption1.deselect()
            self.qOption2.deselect()
            self.qOption3.deselect()
            self.qOption4.deselect()
            self.qOptions.set("")
        if (self.qOptions.get() in ["Not at all", "Nearly Everyday", "Several Days", "More than half the days"]) and (data_store.flag == 17):
            data_store.phq_responses.append(self.qOptions.get()) 
            data_store.flag += 1
            self.label_info_1.set_text(data_store.phq_questions[data_store.flag - 13])
            playaudio("phq6.mp3")
            user=""
            self.qOption1.deselect()
            self.qOption2.deselect()
            self.qOption3.deselect()
            self.qOption4.deselect()
            self.qOptions.set("")
        
        if (self.qOptions.get() in ["Not at all", "Nearly Everyday", "Several Days", "More than half the days"]) and (data_store.flag == 18):
            data_store.phq_responses.append(self.qOptions.get()) 
            data_store.flag += 1
            self.label_info_1.set_text(data_store.phq_questions[data_store.flag - 13])
            playaudio("phq7.mp3")
            user=""
            self.qOption1.deselect()
            self.qOption2.deselect()
            self.qOption3.deselect()
            self.qOption4.deselect()
            self.qOptions.set("")

        if (self.qOptions.get() in ["Not at all", "Nearly Everyday", "Several Days", "More than half the days"]) and (data_store.flag == 19):
            data_store.phq_responses.append(self.qOptions.get()) 
            data_store.flag += 1
            self.label_info_1.set_text(data_store.phq_questions[data_store.flag - 13])
            playaudio("phq8.mp3")
            user=""
            self.qOption1.deselect()
            self.qOption2.deselect()
            self.qOption3.deselect()
            self.qOption4.deselect()
            self.qOptions.set("")
        
        if (self.qOptions.get() in ["Not at all", "Nearly Everyday", "Several Days", "More than half the days"]) and (data_store.flag == 20):
            data_store.phq_responses.append(self.qOptions.get()) 
            data_store.flag += 1
            self.label_info_1.set_text(data_store.phq_questions[data_store.flag - 13])
            playaudio("phq9.mp3")
            user=""
            self.qOption1.deselect()
            self.qOption2.deselect()
            self.qOption3.deselect()
            self.qOption4.deselect()
            self.qOptions.set("")

        # elif ("no" in user) and (data_store.flag == 13):
        #     data_store.phq_responses.append(self.qOptions.get()) 
        #     data_store.flag += 1
        #     self.label_info_1.set_text(data_store.phq_questions[data_store.flag - 13])
        #     user=""
        #     self.qOption1.deselect()
        #     self.qOption2.deselect()
        #     self.qOption3.deselect()
        #     self.qOption4.deselect()
        #     self.qOptions.set("")
            

        if ("yes" in user) and (data_store.flag == 21):
            self.entry.configure(state="normal")
            data_store.phq_responses.append(self.qOptions.get()) 
            calculatePHQ9Score()
            studmail()
            self.exitfunc()
            self.label_info_1.set_text("Type and enter end to exit")

        elif ("no" in user) and (data_store.flag == 21):
            self.entry.configure(state="normal")
            data_store.phq_responses.append(self.qOptions.get())
            calculatePHQ9Score() 
            studmail()
            self.exitfunc()
            self.label_info_1.set_text("Type and enter end to exit")

        if ("end" in user) and (data_store.flag == 21):
            exit()

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def exitfunc(self):
        playaudio("end.mp3")
        dep_anx_score = str(math.floor(data_store.dep_anx_val / 0.08)) + "%"
        enthu_score = str(math.floor(data_store.enthu_val / 0.09)) + "%"
        opti_score = str(math.floor(data_store.opti_val / 0.03)) + "%"

        import csv
        headers = ["Student Name", "Anxiety / Depression Score", "Enthusiasm Score", "Optimism Score"]
        student_list = [[data_store.student_name, dep_anx_score, enthu_score, opti_score]]

        with open("student_record.csv", "w") as stud:
            student = csv.writer(stud)
            student.writerow(headers)
            student.writerows(student_list)

        self.label_info_1.set_text("Data Generated Successfully!")
        import mail
        mail.main(data_store.admin_mail)
        self.label_info_1.set_text("Data Mailed Successfully!")
        os.remove("student_record.csv")


def calculatePHQ9Score():
    for response in data_store.phq_responses:
        if(response == "Not at all"):
            data_store.phq_score += 0
        elif(response == "Several Days"):
            data_store.phq_score += 1
        elif(response == "More than half the days"):
            data_store.phq_score += 2
        elif(response == "Nearly Everyday"):
            data_store.phq_score += 3

def studmail():
    global is_on
    if data_store.flag == 21:
        if is_on:
            print("ENTERED")
            dep_anx_score = str(math.floor(data_store.dep_anx_val / 0.08)) + "%"
            enthu_score = str(math.floor(data_store.enthu_val / 0.09)) + "%"
            opti_score = str(math.floor(data_store.opti_val / 0.03)) + "%"
            dataToSave = {"patientName":data_store.student_name,
                          "patientEmail":data_store.student_mail,
                          "patientAge": data_store.student_age,
                          "patientGender": data_store.student_gender,
                          "patientPhone": data_store.student_phone,
                          "question1": "Do you think major problems impact your life greatly?",
                          "response1": data_store.response1,
                          "question2": "Consider you're in a race.You are told your opponent is faster than you. Would you still run the race?",
                          "response2": data_store.response2,
                          "question3": "Do you believe that you are in control of your life?",
                          "response3": data_store.response3,
                          "enthusiasm":dep_anx_score,
                          "depression score":enthu_score,
                          "optimisum":opti_score,
                          "phqQuestions": data_store.phq_questions,
                          "phqResponses": data_store.phq_responses,
                          "phqScore": data_store.phq_score
                          }
            db.saveData(dataToSave)

            pdf.create_pdf(data_store.student_name,data_store.student_mail,data_store.student_phone,data_store.student_age,data_store.student_gender,dep_anx_score,enthu_score,opti_score,str(data_store.phq_score))

            import csv
            headers = ["Student Name", "Anxiety / Depression Score", "Enthusiasm Score", "Optimism Score"]
            student_list = [[data_store.student_name, dep_anx_score, enthu_score, opti_score]]

            with open("student_record.csv", "w") as stud:
                student = csv.writer(stud)
                student.writerow(headers)
                student.writerows(student_list)
            import mail
            print("Sending report to Admin and Student")
            mail.main(data_store.student_mail)
            os.remove("student_record.csv")
            is_on = False
        else:
            print("Sending report to Admin")
            is_on = True

def playaudio(filemp3):
    mixer.init()
    mixer.music.load("samples/"+filemp3)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)


if __name__ == "__main__":
    app = App()
    app.mainloop()