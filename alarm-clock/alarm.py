#!/usr/bin/python3
import playsound
from tkinter import *
import datetime
import time
from tkinter import messagebox, font
from tkinter import ttk


class Alarm:
    def __init__(self):
        self.tool = Tk()
        self.s = ttk.Style()
        self.s.configure('Asheuh.TFrame', background='#E3F0F0')
        self.tool.config(background='#E3F0F0')
        self.frame1 = ttk.Frame(self.tool, style='Asheuh.TFrame')
        self.frame1.grid(row=0, column=1)
        self.frame1.config(height=100, width=100)
        self.main_labl = ttk.Label(self.frame1, justify='center')
        self.main_labl.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        self.input1 = ttk.Entry(self.frame1, width=20)
        self.input1.grid(row=2, column=1, padx=50, pady=50)
        self.input2 = ttk.Entry(self.frame1, width=50)
        self.input2.grid(row=3, column=1, padx=50, pady=50)
        self.main_label()
        self.entry()

    def titlebar(self):
        self.tool.title('ASHEUH ALARM CLOCK')

    def main_label(self):
        t = time.strftime('%I:%M:%S', time.localtime())
        if t != '':
            self.main_labl.config(text=t, font='times 40')
        self.tool.after(1000, self.main_label)
        f = font.Font(self.main_labl, self.main_labl.cget('font'))
        # f.configure(underline=True)
        self.main_labl.configure(font=f, background='#E3F0F0')
        return self.main_labl

    def lableone(self):
        labe1 = ttk.Label(self.frame1, text='ENTER TIME IN THE RIGHT FORMAT:')
        labe1.grid(row=2, column=0, padx=100, pady=40)
        labe1.configure(background='#E3F0F0')
        return labe1

    def entry(self):
        self.input1.insert(3, 'example(06:30)')
        return self.input1

    def labletwo(self):
        labe2 = ttk.Label(self.frame1, text='SET REMINDER HERE:')
        labe2.grid(row=3, column=0, padx=10, pady=40)
        labe2.configure(background='#E3F0F0')
        return labe2

    def entry2(self):
        return self.input2

    def buttons(self):
        self.s.configure("Asheuh.TButton", background='skyblue')
        button1 = ttk.Button(self.frame1, style='Asheuh.TButton', text='Exit', command=self.tool.destroy)
        button1.grid(row=4, column=0, padx=10, pady=20)
        button2 = ttk.Button(self.frame1, style='Asheuh.TButton', text='Set alarm', command=self.set_alarm)
        button2.grid(row=4, column=1, padx=50, pady=20)
        return

    def set_alarm(self):
        alarm_time = self.input1.get()
        self.message()
        current_time = time.strftime("%H:%M")
        while alarm_time != current_time:
            current_time = time.strftime("%H:%M")
            time.sleep(1)

        if alarm_time == current_time:
            playsound.playsound('alarm-music.mp3', True)
            labe3 = ttk.Label(self.frame1, text='Alarm is on and music is fucking loud', font='times 20')
            labe3.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
            labe3.configure(background='#E3F0F0')
            messagebox.showinfo(title='REMINDER', message='{}'.format(self.input2.get()))

    def message(self):
        mssge = self.input1.get()
        messagebox.showinfo(title='Alarm clock', message='Alarm will wake you up at {}'.format(mssge))

    def display(self):
        self.titlebar()
        self.main_label()
        self.lableone()
        self.labletwo()
        self.buttons()
        self.tool.mainloop()


def main():
    ab = Alarm()
    ab.display()


if __name__ == '__main__':
    main()
