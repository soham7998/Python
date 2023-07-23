# import tkinter as tk
# import time
# import math

# def update_clock():
#     current_time = time.strftime("%H:%M:%S")
#     label.config(text=current_time)
#     root.after(1000, update_clock)

# # Create the main window
# root = tk.Tk()
# root.title("Digital Clock")

# # Create a label to display the current time
# label = tk.Label(root, font=("Helvetica", 48))
# label.pack(pady=20)

# # Start updating the clock
# update_clock()

# # Run the Tkinter main loop
# root.mainloop()
import tkinter as tk
import time
import math

def update_clock():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min

    hour_angle = (hour + minute / 60) * math.pi / 6 - math.pi / 2
    hour_x = WIDTH / 2 + 0.5 * WIDTH / 2 * math.cos(hour_angle)
    hour_y = HEIGHT / 2 + 0.5 * WIDTH / 2 * math.sin(hour_angle)

    canvas.delete("hour_hand")
    canvas.create_line(WIDTH / 2, HEIGHT / 2, hour_x, hour_y, fill="black", width=6, tags="hour_hand")

    root.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Analog Clock")

# Set the canvas dimensions
WIDTH, HEIGHT = 400, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Start updating the clock
update_clock()

# Run the Tkinter main loop
root.mainloop()

