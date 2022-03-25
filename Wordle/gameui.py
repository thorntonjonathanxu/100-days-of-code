from tkinter import Tk, Canvas

window = Tk()

c = Canvas(window, width=300, height=300)

def clear():
    canvas.delete(ALL)

def clicked(*args):
    print("You clicked play!")

def spawnbuttons():
    colors = ['red', 'green', 'blue', 'purple','yellow']
    for i,val in enumerate(colors):
        c.create_rectangle(50 * i + 50, 50 * i, 50 * i,  * i + 50, fill=val,tags="playbutton")
# playbutton = c.create_rectangle(75, 25, 25, 75, fill="red",tags="playbutton")
# playbutton = c.create_rectangle(150, 100, 100, 150, fill="blue",tags="playbutton")
# playbutton = c.create_rectangle(75, 25, 25, 75, fill="red",tags="playbutton")
# playbutton = c.create_rectangle(75, 25, 25, 75, fill="red",tags="playbutton")
# playbutton = c.create_rectangle(75, 25, 25, 75, fill="red",tags="playbutton")
# playbutton = c.create_rectangle(75, 25, 25, 75, fill="red",tags="playbutton")
playtext = c.create_text(150, 50, text="Play", font=("Papyrus", 26), fill='blue',tags="playbutton")
spawnbuttons()
c.tag_bind("playbutton","<Button-1>",clicked)

c.pack()

window.mainloop()

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()