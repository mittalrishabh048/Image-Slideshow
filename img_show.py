# Personal Image Slideshow

import tkinter as tk
import time
from PIL import Image,ImageTk


## Main Window 
root=tk.Tk()
root.title("Image Slideshow")
root.geometry("500x500")

## List Of Image Paths
image_paths=[
    r"C:\Users\mitta\Downloads\sololeveling.png",
    r"C:\Users\mitta\Downloads\demonslayer.png",
    r"C:\Users\mitta\Downloads\bleach.png",
    r"C:\Users\mitta\Downloads\naruto.png"
]
image_size=(500,500)
images=[]
for each in image_paths:
    img=Image.open(each)
    img=img.resize(image_size)
    images.append(img)

## Convert PIL Images Into tkinter Compatible Images
final_images=[]
for each_img in images:
    photo=ImageTk.PhotoImage(each_img)
    final_images.append(photo)
#print(f"Total images successfully loaded: {len(final_images)}")


## Label Widget To Keep Photo
image_label=tk.Label(root)
image_label.pack(pady=20)


## Slideshow Function
def start_slideshow(index=0):
    # If we reach the end of the list, reset back to the first image
    if index >= len(final_images):
        index = 0
        
    # Update the label with the current image
    dbgimage_label.config(image=final_images[index])
    #image_label.image = final_images[index]
    
    # Correctly schedule the next image index update using lambda
    root.current_image = final_images[index]
    root.after(2000, lambda: start_slideshow(index + 1))


## Button
play_button=tk.Button(
    root,
    text="Play Slideshow",
    command=start_slideshow
)

play_button.pack(pady=40)

root.mainloop()