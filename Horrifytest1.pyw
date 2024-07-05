import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame

def display_images_and_play_sound(image_path1, image_path2, audio_path):
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user if they want to proceed
    proceed = messagebox.askyesno("Confirmation", "Run malware? (Made by VScriptz)")
    if not proceed:
        root.destroy()
        return

    # Show the main window
    root.deiconify()

    # Hide window borders and title bar
    root.overrideredirect(True)

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window size and position
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    # Load the images
    try:
        image1 = Image.open(image_path1)
        image2 = Image.open(image_path2)
    except Exception as e:
        print(f"Error loading images: {e}")
        return
    
    photo1 = ImageTk.PhotoImage(image1)
    photo2 = ImageTk.PhotoImage(image2)

    # Create a label to display the image
    label = tk.Label(root, image=photo1)
    label.pack(fill=tk.BOTH, expand=True)

    # Function to play sound and switch the image on click
    def on_click(event):
        # Disable further clicks
        label.unbind("<Button-1>")
        
        # Play the audio using Pygame mixer
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        # Switch the image
        current_image = label.cget('image')
        new_image = photo2 if current_image == str(photo1) else photo1
        label.config(image=new_image)
        label.image = new_image  # Keep a reference to avoid garbage collection

        # Close the window after 6 seconds
        root.after(6000, root.destroy)

    # Bind the click event to the on_click function
    label.bind("<Button-1>", on_click)

    # Function to disable all keys
    def disable_keys(event):
        return "break"

    # Bind all key events to disable_keys function
    root.bind_all("<KeyPress>", disable_keys)
    root.bind_all("<KeyRelease>", disable_keys)

    # Start the Tkinter event loop
    root.mainloop()

# Replace 'path/to/image1.jpg', 'path/to/image2.jpg', and 'path/to/audio.mp3' with the paths to your image and audio files
display_images_and_play_sound('horror.jpg', 'horror2.png', 'jumpscare.mp3')
