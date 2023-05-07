# Import the time and tkinter modules
import time
import tkinter as tk

# Define a function to display the timer
def display_timer(seconds):
    # Convert seconds to hours, minutes and seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    # Format the timer as hh:mm:ss
    timer = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    # Update the label text with the timer
    label.config(text=timer)
    # Change the label color and font depending on the time left
    if seconds <= 10:
        label.config(fg="red", font=("Arial", 40, "bold"))
    elif seconds <= 30:
        label.config(fg="orange", font=("Arial", 30, "italic"))
    else:
        label.config(fg="green", font=("Arial", 20))
    # Check if the timer is done
    if seconds == 0 and minutes == 0 and hours == 0:
        # Display a timeout message
        label.config(text="Time's up!", fg="black", font=("Arial", 20))
    else:
        # Schedule the function to run again after one second
        root.after(1000, display_timer, seconds-1)

# Create a tkinter root window
root = tk.Tk()
# Set the window title and size
root.title("Digital Timer")
root.geometry("200x100")
# Create a label to display the timer
label = tk.Label(root)
# Pack the label in the window
label.pack()
# Ask the user to enter the duration of the timer in seconds
duration = int(input("Enter the duration of the timer in seconds: "))
# Display the timer
display_timer(duration)
# Start the main loop of the window
root.mainloop()
