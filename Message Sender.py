import customtkinter as ctk
import pyautogui as me
import time

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Sender")
root.geometry("450x280")
def submit():
    limit = int(limit_entry.get())
    message = message_entry.get()

    time.sleep(15)
    for i in range(limit):
        me.typewrite(message)
        me.press("enter")



message_label = ctk.CTkLabel(master=root, text="Message:")
message_entry = ctk.CTkEntry(master=root, width=200,height=40,corner_radius=5)
limit_label = ctk.CTkLabel(master=root, text="Number of messages:")
limit_entry = ctk.CTkEntry(master=root, width=60,height=30,corner_radius=5)
submit_button = ctk.CTkButton(master=root, text="Send",width=100,height=30,corner_radius=5, command=submit)


message_label.pack(pady=10)
message_entry.pack()
limit_label.pack(pady=10)
limit_entry.pack()

submit_button.pack(pady=20)



root.mainloop()