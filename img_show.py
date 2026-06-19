# Personal Image Slideshow

import tkinter as tk
import time
from PIL import Image,ImageTk


## Main Window 
root=tk.Tk()
root.title("Image Slideshow")
root.geometry("500x500")

## State Management
is_playing = False  # Tracks if the slideshow loop is active


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

# If no images loaded at all, show a default message
if not images:
    image_label.config(text="No images found!\nPlease check your file paths.", font=("Arial", 14))

## Slideshow Function
def start_slideshow(index=0):
    global is_playing

    # Defensive check: if no images exist, exit function
    if not images:
        return
    
    # If we reach the end of the list, reset back to the first image
    if index >= len(images):
        index = 0
        
    # Update the label with the current image
    image_label.config(image=images[index])
    #image_label.image = final_images[index]
    
    # Correctly schedule the next image index update using lambda
    root.current_image = images[index]
    root.after(2000, lambda: start_slideshow(index + 1))

## Controller Function
def play_trigger():
    global is_playing
    # Only start the loop if it's not already running
    if not is_playing:
        is_playing = True
        start_slideshow(0)

## Button
play_button=tk.Button(
    root,
    text="Play Slideshow",
    command=play_trigger
)

play_button.pack(pady=40)

root.mainloop()