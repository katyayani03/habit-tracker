from customtkinter import *
from tkinter import messagebox
from PIL import Image
import pandas as pd
from datetime import datetime


habits_df = pd.DataFrame(columns=['Datetime', 'Name', 'Duration'])



set_appearance_mode("system")
set_default_color_theme("green")


habits = []

def submit():
    name = name_entry.get()
    duration = duration_entry.get()

    if name == "" or duration == "":
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    if name not in habits:
        habits.append(name)
        update_dropdown()

    global habits_df
    new_entry = pd.DataFrame({'Datetime': datetime.now(),
                              'Habit Name': [name],
                              'Duration': [duration]
                              })
    habits_df = pd.concat([habits_df, new_entry], ignore_index=True)
    # Here you could add code to store the habit in a database or a file
    print(f"Habit: {name}, Duration: {duration}")

    # Clear the fields after submission
    name_entry.delete(0, END)
    duration_entry.delete(0, END)

    messagebox.showinfo("Submission", "Habit submitted successfully!")


def update_dropdown():
    dropdown.configure(values=habits)
    if habits:
        dropdown.set(habits[0])
    else:
        dropdown.set("")

def on_entry_change(event):
    # Filter the habits based on the entry field
    typed_value = name_entry.get().lower()
    filtered_habits = [habit for habit in habits if typed_value in habit.lower()]
    dropdown.configure(values=filtered_habits)
    if filtered_habits:
        dropdown.set(filtered_habits[0])
    else:
        dropdown.set("")
def show_add_new_mode():
    # Hide the dropdown and show the habit name entry field
    dropdown_frame.pack_forget()
    name_entry_frame.grid(row=1, column=1, pady=5, padx=5, sticky="ew")


def show_dropdown_mode():
    # Hide the habit name entry field and show the dropdown
    name_entry_frame.grid_forget()
    dropdown_frame.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
    update_dropdown()


# Create the main window
app = CTk()
app.title("Habit Tracker")
app.geometry("500x500")

logo = "logo3.webp"
img = Image.open(logo)
photo = CTkImage(light_image=img, dark_image=img, size=(250, 250))
img_label = CTkLabel(app, image=photo)
img_label.grid(row=0, column=1)


#frames
dropdown_frame = CTkFrame(app)
dropdown_frame.grid(row=1, column=0, columnspan=2, sticky="w")

name_entry_frame = CTkFrame(app)
name_entry_frame.grid_forget()  # Initially hidden


name_label = CTkLabel(dropdown_frame, text="Habit:")
name_label.grid(row=1, column=0, pady=5, padx=5, sticky="ew")

dropdown = CTkOptionMenu(dropdown_frame, values=habits)
dropdown.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

name_entry_label = CTkLabel(name_entry_frame, text="New Habit:")
name_entry_label.grid(row=1, column=0, pady=5, padx=5, sticky="ew")

name_entry = CTkEntry(name_entry_frame, placeholder_text="reading, cooking etc.")
name_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
name_entry.bind("<KeyRelease>", on_entry_change)

add_new_button = CTkButton(app, text="New", command=show_add_new_mode)
add_new_button.grid(row=1, column=2, pady=5, padx=5, sticky="ew", ipadx=5)


duration_label = CTkLabel(app, text="Duration:")
duration_label.grid(row=2, column=0, pady=20, padx=30, sticky="ew")

duration_entry = CTkEntry(app, placeholder_text="in minutes")
duration_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")


submit_button = CTkButton(app, text="Submit", command=submit)
submit_button.grid(row=3, column=1, pady=5, padx=5, sticky="ew")



# Start by showing the dropdown menu
show_dropdown_mode()


app.mainloop()
