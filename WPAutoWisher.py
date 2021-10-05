# importing_the_required_libraries
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
import pyautogui
import pywhatkit as wp
import time

# creating the GUI window
window = Tk()
window.title("WP Auto Wisher")
window.geometry("700x500+300+320")
no = StringVar()
txt = StringVar()


def wp_send(num, text):
    # function for sending whatsapp message
    num = str(num)
    text = str(text)
    wp.sendwhatmsg(num, text, 0, 0, 5)   # input time in 24 Hour format
    pyautogui.click(1050, 950)
    time.sleep(2)
    pyautogui.click(1866, 974)


def save():
    # functionality of 'submit' button
    no = wp_number.get()
    txt = wp_message.get()
    wp_send(no, txt)


# Heading part
header_font = Font(family="Helvetica", size=28, weight="bold")
Label(window, text="Auto wisher for Whatsapp", font=header_font).pack()

# image part
main_image = ImageTk.PhotoImage(Image.open("img.jpg"))
img_label = Label(image=main_image)
img_label.pack()

number = Label(window, text="Enter Number(WITH COUNTRY CODE)")
number.pack()
wp_number = Entry(window, textvariable=no, width=14)
wp_number.pack()

message = Label(window, text="Enter message")
message.pack()
wp_message = Entry(window, textvariable=txt, width=70)
wp_message.pack()

# buttons
submit = Button(window, text="Wish", command=save, padx=10, pady=10, bg='#4a7abc', fg='yellow', activebackground='green', activeforeground='white').pack()
exitButton = Button(window, text="Exit", command=window.destroy, padx=10, pady=10, bg="red", fg='black').pack()

# custom icon
window.iconbitmap(r'favicon.ico')
window.mainloop()
