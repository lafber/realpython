''' Real Python
    Script Python générique pour exécuter les exemples du cours    
'''

from tkinter import *

window = Tk()
window.geometry("300x200")


button1 = Button(window, text="I'm at offset (50, 60)")
button2 = Button(window, text="I'm at offset (0, 0)")

button1.pack()
button2.pack()

button1.place(height=200, width=200, x=50, y=65)
button2.place(height=150, width=150, x=0, y=0)

window.mainloop() # run the application
