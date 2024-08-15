from tkinter import *
from tkinter import messagebox


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Habit Tracker")
        self.window.config(pady=20, padx=20)

        self.canvas = Canvas(height=250, width=250)

        logo_img = PhotoImage(file="logo2.jpg")
        self.logo = self.canvas.create_image(image=logo_img)
        self.logo.grid(row=0, column=1)

        dropdown_frame = Frame(self.window)
        dropdown_frame.grid(row=1, column=0, columnspan=2)

        name_entry_frame = Frame(self.window)
        name_entry_frame.grid_forget()  # Initially hidden

        self.name_label = Label(dropdown_frame, text="Habit:")
        self.name_label.grid(row=1, column=0, pady=5, padx=5, sticky="ew")

        self.dropdown = OptionMenu(dropdown_frame)
        self.dropdown.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        self.name_entry_label = Label(name_entry_frame, text="New Habit:")
        self.name_entry_label.grid(row=1, column=0, pady=5, padx=5, sticky="ew")

        self.name_entry = Entry(name_entry_frame, placeholder_text="reading, cooking etc.")
        self.name_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        self.name_entry.bind("<KeyRelease>", self.on_entry_change)

        self.add_new_button = Button(self.window, text="New", command=self.show_add_new_mode)
        self.add_new_button.grid(row=1, column=2, pady=5, padx=5, sticky="ew", ipadx=5)

        self.duration_label = Label(self.window, text="Duration:")
        self.duration_label.grid(row=2, column=0, pady=20, padx=30, sticky="ew")

        self.duration_entry = Entry(self.window, placeholder_text="in minutes")
        self.duration_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

        self.submit_button = Button(self.window, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, column=1, pady=5, padx=5, sticky="ew")

        self.window.mainloop()

        def submit(self):
            name = self.name_entry.get()
            duration = self.duration_entry.get()

            if name == "" or duration == "":
                messagebox.showwarning("Input Error", "Please fill in all fields.")
                return

            global habits_df
            new_entry = pd.DataFrame({'Datetime': datetime.now(),
                                      'Name': [name],
                                      'Duration': [duration]
                                      })
            habits_df = pd.concat([habits_df, new_entry], ignore_index=True)

            self.update_dropdown()

            # Clear the fields after submission
            self.name_entry.delete(0, END)
            self.duration_entry.delete(0, END)

            messagebox.showinfo("Submission", "Habit submitted successfully!")

        def update_dropdown(self):
            habits = habits_df["Name"].tolist()
            self.dropdown.configure(values=habits)
            if habits:
                self.dropdown.set(habits[0])
            else:
                self.dropdown.set("")

        # def on_entry_change(event):
        #     # Filter the habits based on the entry field
        #     habits = habits_df["Name"].tolist()
        #     typed_value = self.name_entry.get().lower()
        #     filtered_habits = [habit for habit in habits if typed_value in habit.lower()]
        #     dropdown.configure(values=filtered_habits)
        #     if filtered_habits:
        #         self.dropdown.set(filtered_habits[0])
        #     else:
        #         self.dropdown.set("")
        def show_add_new_mode(self):
            # Hide the dropdown and show the name entry field
            self.dropdown_frame.pack_forget()
            self.name_entry_frame.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        def show_dropdown_mode():
            # Hide the name entry field and show the dropdown
            self.name_entry_frame.grid_forget()
            self.dropdown_frame.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

