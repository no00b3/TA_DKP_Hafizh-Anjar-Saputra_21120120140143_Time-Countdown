
#Import modul
import tkinter as tk
import datetime
from tkinter import ttk


# class countdown
class Countdown(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.membuat_widgets()
        self.memunculkan_widgets()
        self.waktu_tersisa=0
        self._waktu_menyala=False
    
    def memunculkan_widgets(self):
        self.label.pack()
        self.entry.pack()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

    def membuat_widgets(self):
        self.label=tk.Label(self, text="Masukkan waktu dalam detik")
        self.entry=tk.Entry(self, justify ="left", width = 30, borderwidth = 5)
        self.reset= tk.Button(self, text="Reset",padx=90,fg="white",bg="red",
                              command=self.tombol_reset)
        self.stop=tk.Button(self, text="Berhenti",
                            command=self.tombol_berhenti)
        self.start=tk.Button(self,text="Mulai",
                             command=self.tombol_mulai)

    def countdown(self):
        self.label["text"]=self.convert_waktu_tersisa()

        if self.waktu_tersisa:
            self.waktu_tersisa-=1
            self._waktu_menyala=self.after(1000, self.countdown)
     
    def tombol_reset(self):
        self.waktu_tersisa = 0
        self.stop_timer()
        self._waktu_menyala=False
        self.label["text"]="Masukkan waktu dalam detik"
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

    def tombol_berhenti(self):
        self.waktu_tersisa=int(self.entry.get())
        self.stop_timer()

    def tombol_mulai(self):
        self.waktu_tersisa= int(self.entry.get())
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

   
    def stop_timer(self):
        if self._waktu_menyala:
            self.after_cancel(self._waktu_menyala)
            self._waktu_menyala=False

    def convert_waktu_tersisa(self):
        while True:
            return datetime.timedelta(seconds=self.waktu_tersisa)

# main loop
if __name__=="__main__":
        root=tk.Tk()
        root.geometry("400x180")
        root.title("Timer App")
  
        root.iconbitmap('E:\TAAA\Radiation.ico')
        root.resizable(False,False)
        countdown=Countdown(root)
        countdown.pack()

        root.mainloop()
       
