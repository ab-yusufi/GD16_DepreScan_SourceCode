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

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
is_on = True

class data_store:
    enthu_val = 0
    opti_val = 0
    dep_anx_val = 0
    student_name = ""
    flag= 0
    admin_mail = "siddhantindave@icloud.com"
    student_mail = ""
    name_flag = 0

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Student Behavioral Analysis System")
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
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="SBA Bot",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)



        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

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

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Options:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

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

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Enter",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.optionmenu_1.set("Dark")

        self.progressbar.set(0.0)

########################################################################################################################

    def button_event(self):
        #print("Button pressed")
        data = self.entry.get()
        user = data.lower()

        if data_store.name_flag == 0:
            data_store.student_name = data
            print(data_store.student_name)
            data_store.name_flag += 1
            self.label_info_1.set_text("Please Enter E-mail ID")
            user = ""

        if ".com" in user:
            data_store.student_mail = user
            self.label_info_1.set_text("Welcome Student, "
                                       "\nplease follow the voice instructions ahead. "
                                       "\nType and enter OK to continue ")
            user = ""
            print(data_store.student_name + "'s Email: ", data_store.student_mail)


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
            import test_ser
            test_ser.main()
            greet_response = test_ser.main.result
            if vid2_reaction == 'happy':
                data_store.enthu_val += 1
            else:
                data_store.dep_anx_val += 1
            if greet_response == 'happy':
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
            self.label_info_1.set_text("Bot: Consider you're in a race. "
                                       "\nYou are told your opponent is faster than you. "
                                       "\nWould you still run the race?")
            data_store.opti_val += 1
            data_store.flag += 1
            playaudio("q11.mp3")
            user = ""

        elif ("yes" in user) and (data_store.flag == 10):
            self.label_info_1.set_text("Bot: Consider you're in a race. "
                                       "\nYou are told your opponent is faster than you. "
                                       "\nWould you still run the race?")

            data_store.flag += 1
            playaudio("q11.mp3")
            user = ""

        if ("yes" in user) and (data_store.flag == 11):
            self.label_info_1.set_text("Bot: Do you believe that you "
                                       "\nare in control of your life?")
            data_store.opti_val += 1
            data_store.flag += 1
            playaudio("q12.mp3")
            user = ""


        elif ("no" in user) and (data_store.flag == 11):
            self.label_info_1.set_text("Bot: Do you believe that you "
                                       "\nare in control of your life?")
            data_store.flag += 1
            playaudio("q12.mp3")
            user = ""

        if ("yes" in user) and (data_store.flag == 12):
            data_store.opti_val += 1
            studmail()
            self.exitfunc()
            self.label_info_1.set_text("Type and enter end to exit")

        elif ("no" in user) and (data_store.flag == 12):
            studmail()
            self.exitfunc()
            self.label_info_1.set_text("Type and enter end to exit")

        if ("end" in user) and (data_store.flag == 12):
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


def studmail():
    global is_on
    if data_store.flag == 14:
        if is_on:
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