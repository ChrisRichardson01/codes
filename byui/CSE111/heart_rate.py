import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Radius:"
    lbl_radius = Label(frm_main, text="Radius:")

    # Create a float entry box where the user will enter the radius.
    ent_radius = IntEntry(frm_main, width=4)

    # Create a label that displays "Area:"
    lbl_area = Label(frm_main, text="Area:")

    # Create a label to display the calculated area.
    lbl_result = Label(frm_main, width=10)

    # Create the Calculate button.
    btn_calculate = Button(frm_main, text="Calculate")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Create a label to display the status message.
    lbl_status = Label(frm_main, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(row=0, column=0, padx=3, pady=3)
    ent_radius.grid(row=0, column=1, padx=3, pady=3)
    lbl_area.grid(row=1, column=0, padx=3, pady=3)
    lbl_result.grid(row=1, column=1, padx=3, pady=3)
    btn_calculate.grid(row=2, column=0, padx=3, pady=3, columnspan=2, sticky="w")
    btn_clear.grid(row=2, column=1, padx=3, pady=3, sticky="e")
    lbl_status.grid(row=3, column=0, padx=3, pady=3, columnspan=2, sticky="we")

    # This function will be called when the user clicks the "Calculate" button.
    def calculate_area():
        """Compute and display the area of a circle."""
        try:
            # Get the user's input for the radius.
            radius = ent_radius.get()

            # Check if the input is valid.
            if radius <= 0:
                raise ValueError("Invalid input. Radius must be a positive number.")

            # Calculate the area using the formula: A = π * r^2
            area = math.pi * radius**2

            # Display the calculated area.
            lbl_result.config(text=f"{area:.2f}")

            # Clear the status message.
            lbl_status.config(text="")
        except ValueError as e:
            # If the user enters invalid input, display the error message in the status bar.
            lbl_status.config(text=str(e))

    # This function will be called when the user clicks the "Clear" button.
    def clear_inputs():
        """Clear all inputs and outputs."""
        ent_radius.delete(0, tk.END)
        lbl_result.config(text="")
        lbl_status.config(text="")

    # Bind the calculate_area function to the button click event.
    btn_calculate.config(command=calculate_area)

    # Bind the clear_inputs function to the button click event.
    btn_clear.config(command=clear_inputs)

    # Give the keyboard focus to the radius entry box.
    ent_radius.focus()


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window.
    frm_main = Frame(root)
    frm_main.master.title("Circle Area Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function to add widgets.
    populate_main_window(frm_main)

    # Start the tkinter loop.
    root.mainloop()


if __name__ == "__main__":
    main()