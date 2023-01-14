from tkinter import *

# Window
window = Tk()
# window.minsize(width="400", height="200")
window.title("Mile to Kilometer Convertor")
window.config(padx=20, pady=20)

def calculate():
    mile = float(mile_input.get())

    kilo = mile * 1.609
    kilo_entry["text"] = kilo
# Entry
mile_input = Entry()
mile_input.grid(column=1, row=0)

# Label
mile_label = Label(text="Miles", font=("Arial", 10, "normal"))
mile_label.grid(column=2, row=0)

is_equal_to_kilo = Label(text="is equal to ", font=("Arial", 10, "normal"))
is_equal_to_kilo.grid(column=0, row=1)

kilo_entry = Label(text="0")
kilo_entry.grid(column=1, row=1)

kilo_label = Label(text="Km", font=("Arial", 10, "normal"))
kilo_label.grid(column=2, row=1)


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)





window.mainloop()