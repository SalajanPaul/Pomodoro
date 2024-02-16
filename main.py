import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound
import time

class Pomodoro:
    def __init__(self, root):
        self.root = root
        self.timer_running = False

    def work_break(self, timer):
        minutes, seconds = divmod(timer, 60)
        self.min.set(f"{minutes:02d}")
        self.sec.set(f"{seconds:02d}")
        self.root.update()
        time.sleep(1)

    def work(self):
        timer = 25*60
        while timer >= 0:
            pomo.work_break(timer)
            if timer == 0:

                playsound("sound/start.wav")
                messagebox.showinfo("Good Job", "Take a break, \nClick Break Button")

            timer -= 1

    def break_(self):
        timer = 5*60
        while timer >= 0:
            pomo.work_break(timer)
            if timer == 0:

                playsound("sound/start.wav")
                messagebox.showinfo("Times Up", "Get back to work, \nClick Work Button")

            timer -= 1

    def main(self):

        self.root.geometry("450x455")
        self.root.resizable(False, False)
        self.root.title("Pomodoro Timer")

        self.min = tk.StringVar(self.root)
        self.min.set("25")
        self.sec = tk.StringVar(self.root)
        self.sec.set("00")

        self.min_label = tk.Label(self.root, textvariable=self.min, font=("arial", 22, "bold"), bg="red", fg="black")
        self.min_label.pack()

        self.sec_label = tk.Label(self.root, textvariable=self.sec, font=("arial", 22, "bold"), bg="black", fg="white")
        self.sec_label.pack()

        canvas = tk.Canvas(self.root)
        canvas.pack(expand=True, fill="both")
        img = Image.open("background/darth-vader.jpg")

        new_size = (280, 255)
        resize_img = img.resize(new_size)
        resize_img.save("resized_darth_vader.jpg")

        bg = ImageTk.PhotoImage(resize_img)
        canvas.create_image(90, 10, image=bg, anchor="nw")

        btn_work = tk.Button(self.root, text="Start", bd=5, command=self.work, bg="red", font=("arial", 15, "bold")).place(x=140, y=380)
        btn_break = tk.Button(self.root, text="Break", bd=5, command=self.break_, bg="red", font=("arial", 15, "bold")).place(x=240, y=380)

        self.root.mainloop()

if __name__ == "__main__":
    pomo = Pomodoro(tk.Tk())
    pomo.main()

