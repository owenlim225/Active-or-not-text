import tkinter as tk

class EntryActivity:
    def __init__(self):
        self.ent_text = None

        #Color malupet naiba iba
        self.colors = ["#FFD000",
                       "#FFC300",
                       "#FF9500",
                       "#FFA200",
                       "#FFAA00",
                       "#FF7B00",
                       "#FF8800",
                       "#FFB700"]  

    def entry_activity(self):

        # Window Config
        win = tk.Tk()
        win.title("J1S_MidLA1")
        win.geometry("400x200")
        win.resizable(False, False)



        # Set the background color of the window to black
        win.configure(bg="#11001c")

        # Create a frame
        frame = tk.Frame(win, bd=10, relief=tk.GROOVE, bg="black")  # Add border and relief
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=380, height=160)

        # Function to update background color
        def PailawNaMalupet(idx=0):
            frame.config(bg=self.colors[idx])
            idx = (idx + 1) % len(self.colors)
            win.after(1000, PailawNaMalupet, idx)

        # Pang pasko color
        PailawNaMalupet()

        # Win Objects
        lbl_entry_text = tk.Label(frame, text="Limosnero, Sherwin P.", font=("Helvetica", 14), bg="yellow", fg="black", bd=3)
        lbl_entry_text.pack(pady=(10, 0))

        self.ent_text = tk.Entry(frame, font=("Helvetica", 14))
        self.ent_text.pack(padx=(10, 10), pady=(10, 0))

        self.btn_enable = tk.Button(frame, text="Enable", font=("Helvetica", 12), width=10, command=self.enable, background="#39FF14", bd=3)
        self.btn_enable.place(x=50, y=100)
        self.btn_disable = tk.Button(frame, text="Disable", font=("Helvetica", 12), width=10, command=self.disable, background="#FF3131", bd=3)
        self.btn_disable.place(x=220, y=100)

        # Win Loop
        win.mainloop()

    def enable(self):
        self.ent_text.config(state=tk.NORMAL)
        self.btn_enable.config(bg="#39FF14")  # Set background color to green
        self.btn_disable.config(bg="#FF3131")  # Set background color to red

    def disable(self):
        self.ent_text.config(state=tk.DISABLED)
        self.btn_enable.config(bg="#FF3131")  # Set background color to red
        self.btn_disable.config(bg="#39FF14")  # Set background color to green

run = EntryActivity()
run.entry_activity()

