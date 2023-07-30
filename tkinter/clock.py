import tkinter as tk
import time
import math

WIDTH = 400
HEIGHT = 400

root = tk.Tk()
root.title("Analog Clock")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

def update_clock():
    canvas.delete("all")
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec

    # Draw clock face
    canvas.create_oval(2, 2, WIDTH, HEIGHT, outline="black", width=2)

    # Draw hour numbers
    for i in range(12):
        angle = i * math.pi / 6 - math.pi / 2
        x = WIDTH / 2 + 0.7 * WIDTH / 2 * math.cos(angle)
        y = HEIGHT / 2 + 0.7 * WIDTH / 2 * math.sin(angle)

        if i == 0:
            canvas.create_text(x, y - 10, text=str(i + 12), font=("Times new roman", 14))
        else:
            canvas.create_text(x, y, text=str(i), font=("Times new roman", 14))

    # Draw minutes line
    for i in range(60):
        angle = i * math.pi / 30 - math.pi / 2
        x1 = WIDTH / 2 + 0.8 * WIDTH * math.cos(angle)
        y1 = HEIGHT / 2 + 0.8 * WIDTH * math.sin(angle)
        x2 = WIDTH / 2 + 0.9 * WIDTH * math.cos(angle)
        y2 = HEIGHT / 2 + 0.9 * WIDTH * math.sin(angle)

        # draw lines every five seconds
        if i % 5 == 0:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=3)
        else:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=1)

    # Draw hour hand
    hour_angle = (hour + minute / 60) * math.pi / 6 - math.pi / 2
    hour_x = WIDTH / 2 + 0.5 * WIDTH / 2 * math.cos(hour_angle)
    hour_y = HEIGHT / 2 + 0.5 * WIDTH / 2 * math.sin(hour_angle)
    canvas.create_line(WIDTH / 2, HEIGHT / 2, hour_x, hour_y, fill="blue", width=6)

    # Draw minute hand
    minute_angle = (minute + second / 60) * math.pi / 30 - math.pi / 2
    minute_x = WIDTH / 2 + 0.7 * WIDTH / 2 * math.cos(minute_angle)
    minute_y = HEIGHT / 2 + 0.7 * WIDTH / 2 * math.sin(minute_angle)
    canvas.create_line(WIDTH / 2, HEIGHT / 2, minute_x, minute_y, fill="blue", width=4)

    # Draw now for second hand
    second_angle = second * math.pi / 30 - math.pi / 2
    second_x = WIDTH / 2 + 0.6 * WIDTH / 2 * math.cos(second_angle)
    second_y = WIDTH / 2 + 0.6 * WIDTH / 2 * math.sin(second_angle)
    canvas.create_line(WIDTH / 2, HEIGHT / 2, second_x, second_y, fill="red", width=2)

    canvas.after(1000, update_clock)

update_clock()
root.mainloop()
