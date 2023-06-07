import tkinter as tk
import os
import schedule as sc
import time


def GUI():


    #Making the window

    window = tk.Tk()

    window.title("          Update & Upgrade")
    window.geometry("400x190")

    label = tk.Label(window, text="Do you want to do the update & upgrade now?", font=("Consolas", 10))
    label.pack(padx=20, pady=20)

    frame=tk.Frame(window)
    frame.pack()


    #Defining what the buttons will do after interaction

    def button1():
        reply = tk.Label(window, text="As you wish!", font=("Consolas",11))
        reply.pack(pady=30)
    
        def UpdateUpgrade():
            os.system("sudo apt update ; sudo apt upgrade")
    
        window.after(1000, UpdateUpgrade)
        window.after(1000, window.destroy)

    def button2():
        answer = tk.Label(window, text="See you later!", font=("Consolas",11))
        answer.pack(pady=30)

        window.after(1000, window.destroy)

    button1 = tk.Button(frame, text="Yes sure", font=("Consolas", 10), command=button1)
    button1.pack(side=tk.LEFT, padx=15)

    button2 = tk.Button(frame, text="No thanks", font=("Consolas", 10), command=button2)
    button2.pack(side=tk.RIGHT, padx=15)


    window.mainloop()

    
#Creating a schedule (can be changed)

sc.every().week.do(GUI)

while True:
    sc.run_pending()
    time.sleep(1)

