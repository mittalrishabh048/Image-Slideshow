# Personal Image Slideshow App

A desktop image slideshow application built with Python, Tkinter, and Pillow (PIL). The application allows users to browse images manually or play them automatically as a slideshow with adjustable speed controls.

This project was developed to strengthen my understanding of GUI development, file handling, event-driven programming, state management, and object-oriented programming in Python.

---

## Features

### Object-Oriented Design

* Refactored the application into a class-based architecture.
* Reduced dependency on global variables by managing application state through class attributes.

### Automatic Image Loading

* Loads images automatically from a local `Images` folder.
* Eliminates the need for hardcoded image paths.

### Image Validation

* Filters supported image formats before loading:

  * `.png`
  * `.jpg`
  * `.jpeg`
  * `.webp`
  * `.bmp`

### Error Handling

* Gracefully handles invalid files and loading errors.
* Prevents the application from crashing when problematic images are encountered.

### Image Counter

* Displays the current slideshow position.
* Example: `Image 2 of 4`.

### Manual Navigation

* Previous and Next buttons allow users to browse images manually.

### Play / Pause Functionality

* Supports automatic slideshow playback.
* Users can pause and resume the slideshow at any time.

### Adjustable Slideshow Speed

* Includes a slider for controlling the slideshow interval.
* Playback speed can be adjusted from 1 to 5 seconds.

---

## Technologies Used

* Python
* Tkinter
* Pillow (PIL)
* OS Module

---

## Project Structure

```text
IMAGE-SLIDESHOW/
│
├── Images/
│   ├── bleach.png
│   ├── demonslayer.png
│   ├── naruto.png
│   └── sololeveling.png
│
├── img_show.py
└── README.md
```

---

## Learning Outcomes

Through this project, I practiced:

* Object-Oriented Programming (OOP)
* GUI Development with Tkinter
* Event-Driven Programming
* File and Folder Handling
* State Management
* Error Handling and Defensive Programming
* Code Refactoring
* Project Organization and Documentation

---

## AI-Assisted Development

This project was developed with the assistance of AI tools as part of my learning journey.

AI was used for:

* Understanding Tkinter concepts and GUI design patterns
* Exploring different implementation approaches
* Reviewing code structure and design decisions
* Learning object-oriented programming practices
* Debugging issues and understanding errors
* Improving project documentation

The focus of this project was not only to build a working application but also to understand the underlying programming concepts and improve independent problem-solving skills.
