import customtkinter as ctk
from tkinter import filedialog, messagebox
from change_extension import convert_file_extension
import threading
import time

# Function to select a file
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file_path.delete(0, ctk.END)
        entry_file_path.insert(0, file_path)

# Function to update the progress bar
def update_progress_bar():
    for i in range(100):
        time.sleep(0.02)  # Simulate work being done
        progress_bar.set(i / 100)  # Update the progress bar value
    progress_bar.set(1)  # Ensure it reaches 100% at the end

# Function to convert the file extension
def convert_extension():
    file_path = entry_file_path.get()
    new_extension = entry_new_extension.get()
    if not file_path or not new_extension:
        messagebox.showerror("Error", "Please provide both file path and new extension.")
        return

    # Disable buttons while processing
    convert_button.configure(state="disabled")
    browse_button.configure(state="disabled")

    # Start the progress bar in a separate thread
    def process_conversion():
        progress_bar.set(0)  # Reset the progress bar
        threading.Thread(target=update_progress_bar).start()
        
        # Simulate conversion logic
        result = convert_file_extension(file_path, new_extension)
        progress_bar.set(1)  # Ensure progress bar is full at completion

        # Show the result and re-enable buttons
        if "Error" in result:
            messagebox.showerror("Error", result)
        else:
            messagebox.showinfo("Success", f"File converted to: {result}")

        # Re-enable buttons after completion
        convert_button.configure(state="normal")
        browse_button.configure(state="normal")

    threading.Thread(target=process_conversion).start()

# Set up the main application window
ctk.set_appearance_mode("System")  # Auto-adjust based on system theme
ctk.set_default_color_theme("blue")  # Material You style theme

root = ctk.CTk()  # Use customtkinter as the main window
root.title("File Extension Converter")
root.geometry("700x200")
root.resizable(False, False)

# Create and place the widgets
ctk.CTkLabel(root, text="File Path:", font=("Roboto", 14)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_file_path = ctk.CTkEntry(root, width=400, font=("Roboto", 12))
entry_file_path.grid(row=0, column=1, padx=10, pady=10, sticky="w")
browse_button = ctk.CTkButton(root, text="Browse", command=select_file, font=("Roboto", 12))
browse_button.grid(row=0, column=2, padx=10, pady=10)

ctk.CTkLabel(root, text="New Extension:", font=("Roboto", 14)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_new_extension = ctk.CTkEntry(root, width=200, font=("Roboto", 12))
entry_new_extension.grid(row=1, column=1, padx=10, pady=10, sticky="w")

convert_button = ctk.CTkButton(root, text="Convert", command=convert_extension, font=("Roboto", 14))
convert_button.grid(row=2, column=0, columnspan=3, pady=20)

# Add a progress bar
progress_bar = ctk.CTkProgressBar(root)
progress_bar.grid(row=3, column=0, columnspan=3, pady=10, sticky="ew")
progress_bar.set(0)  # Initialize to 0%

# Run the application
root.mainloop()
