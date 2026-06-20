# Personal Image Slideshow

import tkinter as tk
from PIL import Image, ImageTk
import os 

class ImageSlideshowApp:
    def __init__(self, root):
        """Initializes the main application window configurations and states."""
        self.root = root
        self.root.title("Image Slideshow")
        self.root.geometry("600x700") 

        # --- STATE MANAGEMENT TRACKERS ---
        self.is_playing = False      # Tracks if the slideshow loop is active
        self.current_index = 0       # Tracks which image is currently displayed
        self.slideshow_timer = None  # Holds the reference ID for the root.after() loop

        # --- DYNAMIC FOLDER CONFIGURATION ---
        self.target_folder = "./Images"
        self.valid_extensions = (".png", ".jpg", ".jpeg", ".webp", ".bmp")
        self.image_size = (500, 500)
        self.images = []

        # Run setup methods
        self.load_images()
        self.create_widgets()
        
        # Instantly show the first picture and counter on startup
        self.update_display()

    def load_images(self):
        """Scans the target directory and loads validated images into memory."""
        if os.path.exists(self.target_folder):
            for file_name in os.listdir(self.target_folder):
                if file_name.lower().endswith(self.valid_extensions):
                    try:
                        full_path = os.path.join(self.target_folder, file_name)
                        img = Image.open(full_path)
                        img = img.resize(self.image_size)
                        photo = ImageTk.PhotoImage(img)
                        self.images.append(photo)
                    except Exception as e:
                        print(f"Error loading {file_name}: {e}. Skipping.")
        else:
            print(f"Error: The directory '{self.target_folder}' does not exist.")

        print(f"Total images successfully loaded: {len(self.images)}")

    def create_widgets(self):
        """Creates and sets up all UI widgets and containers."""
        # Main Graphic Canvas Label
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=20)

        # Overlaid Counter Label
        self.counter_label = tk.Label(
            self.image_label, 
            text="", 
            font=("Arial", 11, "bold"), 
            fg="white", 
            bg="#222222",
            padx=8, 
            pady=4
        )
        self.counter_label.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

        # Media Control Buttons Frame
        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack(pady=20)

        self.prev_button = tk.Button(
            self.controls_frame, 
            text="⏮ Previous", 
            command=self.prev_image, 
            width=10, 
            font=("Arial", 11)
        )
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.play_button = tk.Button(
            self.controls_frame, 
            text="Play", 
            command=self.play_pause_button, 
            width=10, 
            font=("Arial", 11, "bold")
        )
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(
            self.controls_frame, 
            text="Next ⏭", 
            command=self.next_image, 
            width=10, 
            font=("Arial", 11)
        )
        self.next_button.pack(side=tk.LEFT, padx=10)

        # Interval Speed Slider Frame
        self.speed_frame = tk.Frame(self.root)
        self.speed_frame.pack(pady=15)

        self.speed_label = tk.Label(self.speed_frame, text="Interval Speed (seconds):", font=("Arial", 10))
        self.speed_label.pack(side=tk.LEFT, padx=5)

        self.speed_slider = tk.Scale(
            self.speed_frame, 
            from_=1, 
            to=5, 
            orient=tk.HORIZONTAL, 
            length=150,
            tickinterval=1
        )
        self.speed_slider.set(2)  
        self.speed_slider.pack(side=tk.LEFT, padx=5)

    def update_display(self):
        """Updates the image label canvas and corresponding index counters."""
        if not self.images:
            # Fallback message if folder is empty
            self.image_label.config(text="No images found!\nPlease check your folder configuration.", font=("Arial", 14))
            self.counter_label.place_forget()
            return
        self.image_label.config(image=self.images[self.current_index])
        self.root.current_image = self.images[self.current_index]
        self.counter_label.config(text=f"Image {self.current_index + 1} of {len(self.images)}")

    def auto_slideshow_loop(self):
        """Triggers the index calculation and re-schedules the automatic execution loop."""
        self.current_index = (self.current_index + 1) % len(self.images)
        self.update_display()
        
        delay_ms = self.speed_slider.get() * 1000
        self.slideshow_timer = self.root.after(delay_ms, self.auto_slideshow_loop)

    def play_pause_button(self):
        """Manages state toggling transitions between playing and pausing."""
        if not self.images:
            return

        if not self.is_playing:
            self.is_playing = True
            self.play_button.config(text="Pause")
            delay_ms = self.speed_slider.get() * 1000
            self.slideshow_timer = self.root.after(delay_ms, self.auto_slideshow_loop)
        else:
            self.is_playing = False
            self.play_button.config(text="Play")
            if self.slideshow_timer:
                self.root.after_cancel(self.slideshow_timer)  
                self.slideshow_timer = None

    def next_image(self):
        """Increments index manually to advance a single picture forward."""
        if not self.images:
            return
        self.current_index = (self.current_index + 1) % len(self.images)
        self.update_display()

    def prev_image(self):
        """Decrements index manually to reverse a single picture backward."""
        if not self.images:
            return
        self.current_index = (self.current_index - 1) % len(self.images)
        self.update_display()


# Execution Entry Point
if __name__ == "__main__":
    main_window = tk.Tk()
    app = ImageSlideshowApp(main_window)
    main_window.mainloop()