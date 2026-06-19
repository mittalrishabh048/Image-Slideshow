# Personal Image Slideshow

import tkinter as tk
import time
from PIL import Image,ImageTk


## Main Window 
root=tk.Tk()
root.title("Image Slideshow")
root.geometry("600x700") # Adjusted window 

## State Management Tracker
is_playing = False  # Tracks if the slideshow loop is active
current_index = 0       # Tracks which image is currently displayed
slideshow_timer = None  # Holds the reference ID for the root.after() loop

## List Of Image Paths
image_paths=[
    r"C:\Users\mitta\Downloads\sololeveling.png",
    r"C:\Users\mitta\Downloads\demonslayer.png",
    r"C:\Users\mitta\Downloads\bleach.png",
    r"C:\Users\mitta\Downloads\naruto.png"
]
image_size=(500,500)
images=[]
## Defensive Image Loading Loop
for each in image_paths:
    try:
        img = Image.open(each)
        img = img.resize(image_size)
        photo = ImageTk.PhotoImage(img)
        images.append(photo)
    except FileNotFoundError:
        print(f"Warning: Could not find image at {each}. Skipping.")
    except Exception as e:
        print(f"Error loading {each}: {e}. Skipping.")
# Print summary log to terminal
print(f"Total images successfully loaded: {len(images)}")

## Label Widget To Keep Photo
image_label=tk.Label(root)
image_label.pack(pady=20)

## Top-Right Corner Image Counter Overlay
# This label uses image_label as its parent so it sits directly on top of the graphics window
counter_label = tk.Label(
    image_label, 
    text="", 
    font=("Arial", 11, "bold"), 
    fg="white", 
    bg="#222222",  # Dark charcoal background box
    padx=8, 
    pady=4
)
# Position dynamically in the top-right corner (North-East) of the image frame
counter_label.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

# If no images loaded at all, show a default message
if not images:
    image_label.config(text="No images found!\nPlease check your file paths.", font=("Arial", 14))


## Core Display Update Function
def update_display():
    """Updates the UI label with the image at the current_index."""
    if not images:
        return
    image_label.config(image=images[current_index])
    root.current_image = images[current_index]

    # Update counter overlay text
    counter_label.config(text=f"Image {current_index + 1} of {len(images)}")

## Slideshow Engine
def auto_slideshow_loop():
    """Handles the automatic progression loop."""
    global current_index, slideshow_timer
    
    # Increment position and wrap around if at the end
    current_index = (current_index + 1) % len(images)
    update_display()
    
    # Read the slider value (seconds) and convert to milliseconds
    delay_ms = speed_slider.get() * 1000

    # Schedule the next slide based on the customized speed
    slideshow_timer = root.after(delay_ms, auto_slideshow_loop)

## Control Actions
def toggle_play():
    """Toggles between starting the auto-loop and canceling it."""
    global is_playing, slideshow_timer
    if not images:
        return

    if not is_playing:
        # Start playing
        is_playing = True
        play_button.config(text="Pause")
        # Queue up the next image after 2 seconds
        slideshow_timer = root.after(2000, auto_slideshow_loop)
    else:
        # Pause functionality
        is_playing = False
        play_button.config(text="Play")
        if slideshow_timer:
            root.after_cancel(slideshow_timer)  # Stops the scheduled loop cleanly
            slideshow_timer = None


def next_image():
    """Moves to the next image manually."""
    global current_index
    if not images:
        return
    current_index = (current_index + 1) % len(images)
    update_display()


def prev_image():
    """Moves to the previous image manually."""
    global current_index
    if not images:
        return
    current_index = (current_index - 1) % len(images)
    update_display()

## UI Controls Layout (Horizontal Frame Container)
controls_frame = tk.Frame(root)
controls_frame.pack(pady=20)

prev_button = tk.Button(
    controls_frame, 
    text="⏮ Previous", 
    command=prev_image, 
    width=10, 
    font=("Arial", 11)
)
prev_button.pack(side=tk.LEFT, padx=10)

play_button = tk.Button(
    controls_frame, 
    text="Play", 
    command=toggle_play, 
    width=10, 
    font=("Arial", 11, "bold")
)
play_button.pack(side=tk.LEFT, padx=10)

next_button = tk.Button(
    controls_frame, 
    text="Next ⏭", 
    command=next_image, 
    width=10, 
    font=("Arial", 11)
)
next_button.pack(side=tk.LEFT, padx=10)

## UI Speed Slider Layout Container
speed_frame = tk.Frame(root)
speed_frame.pack(pady=15)

speed_label = tk.Label(speed_frame, text="Interval Speed (seconds):", font=("Arial", 10))
speed_label.pack(side=tk.LEFT, padx=5)

speed_slider = tk.Scale(
    speed_frame, 
    from_=1, 
    to=5, 
    orient=tk.HORIZONTAL, 
    length=150,
    tickinterval=1
)
speed_slider.set(2)  # Default value initialized to 2 seconds
speed_slider.pack(side=tk.LEFT, padx=5)

root.mainloop()