from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1279x941")
window.configure(bg = "#e0e6f6")
canvas = Canvas(
    window,
    bg = "#e0e6f6",
    height = 941,
    width = 1279,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    1272.0, 196.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    359.5, 468.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e0e6f6",
    highlightthickness = 0)

entry0.place(
    x = 140.0, y = 430,
    width = 439.0,
    height = 74)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    359.5, 607.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e0e6f6",
    highlightthickness = 0)

entry1.place(
    x = 140.0, y = 569,
    width = 439.0,
    height = 74)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 96, y = 708,
    width = 544,
    height = 118)

window.resizable(False, False)
window.mainloop()
