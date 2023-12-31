from PIL import Image, ImageTk
import tkinter as tk
import paths

edges = paths.edges

PRECISION = 10 # ADJUST AS NEEDED

count = 114
edge = edges[count]
mouse_pressed = False
prev_x, prev_y = None, None
all_paths = dict()
coordinates_list = []
i = 0
def get_cursor_location(event):
    global prev_x, prev_y, i
    if mouse_pressed:
        x, y = event.x, event.y
        if i % PRECISION == 0:
            coordinates_list.append((x, y))
        i += 1
        if prev_x is not None and prev_y is not None:
            canvas.create_line(prev_x, prev_y, x, y, fill='red', width=4)
        prev_x, prev_y = x, y

def draw_green_line(coordinates):
    if len(coordinates) >= 2:
        canvas.create_line(coordinates, fill='green', width=5)

def mouse_down(event):
    global mouse_pressed, coordinates_list, prev_x, prev_y
    mouse_pressed = True
    coordinates_list = []
    prev_x, prev_y = event.x, event.y

def mouse_up(event):
    global mouse_pressed, count, edge
    mouse_pressed = False
    all_paths[edge] = coordinates_list
    prev_x, prev_y = None, None
    draw_green_line(coordinates_list)
    count += 1
    if count < len(edges):
        edge = edges[count]
        print(str(count) + "/" + str(len(edges)) + ": " + edge)
    else:
        print("All edges are done.")

print(str(count) + "/" + str(len(edges)) + ": "+ edge)
# Create the main application window
root = tk.Tk()
root.title("Cursor Location on Image")

# Load the image and convert it to a Tkinter PhotoImage
pil_image = Image.open("Lekagul Roadways labeled v2.jpg")
image = ImageTk.PhotoImage(pil_image)

# Create a canvas to display the image
canvas = tk.Canvas(root, width=image.width(), height=image.height())
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=image)

# Bind mouse events
canvas.bind("<Button-1>", mouse_down)
canvas.bind("<ButtonRelease-1>", mouse_up)
canvas.bind("<Motion>", get_cursor_location)

# Run the Tkinter main loop
root.mainloop()

# Print the collected paths
# for item in all_paths:
#     print(item, all_paths[item])

output_file = "precision" + str(PRECISION )+ "paths.js"
js_code = "const pathCoordinates = " + str(all_paths) + ";\nexport default pathCoordinates;"

# Write to the JavaScript file
with open(output_file, "w") as js_file:
    js_file.write(js_code)

print("js file saved as: ", output_file)