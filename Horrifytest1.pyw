import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import requests
from io import BytesIO

def fetch_image_from_url(image_url):
    try:
        response = requests.get(image_url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        return image
    except Exception as e:
        print(f"Error fetching image from URL {image_url}: {e}")
        return None

def fetch_audio_from_url(audio_url):
    try:
        response = requests.get(audio_url)
        audio_data = response.content
        with open('temp_audio.mp3', 'wb') as f:
            f.write(audio_data)
        return 'temp_audio.mp3'  # Return the file path to the temporary audio file
    except Exception as e:
        print(f"Error fetching audio from URL {audio_url}: {e}")
        return None

def display_images_and_play_sound(image_url1, image_url2, audio_url):
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

    # Fetch the images from URLs
    image1 = fetch_image_from_url(image_url1)
    image2 = fetch_image_from_url(image_url2)

    if not image1 or not image2:
        root.destroy()
        return

    photo1 = ImageTk.PhotoImage(image1)
    photo2 = ImageTk.PhotoImage(image2)

    # Create a label to display the image
    label = tk.Label(root, image=photo1)
    label.pack(fill=tk.BOTH, expand=True)

    # Fetch the audio from URL
    audio_path = fetch_audio_from_url(audio_url)

    if not audio_path:
        root.destroy()
        return

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

# Replace 'https://example.com/image1.jpg', 'https://example.com/image2.jpg', and 'https://example.com/audio.mp3' with actual URLs
display_images_and_play_sound('https://i.ibb.co/ng1gTBQ/horror.jpg', 'https://i.ibb.co/dPmBDtP/horror2.png', 'https://s19.aconvert.com/convert/p3r68-cdx67/hiwfn-i6b6c.mp3')

