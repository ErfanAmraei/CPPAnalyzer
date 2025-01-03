# Importing tkinter for GUI, filedialog for file selection dialogs, and messagebox for pop-up messages
import tkinter as tk
from tkinter import filedialog, messagebox

# Importing subprocess for running external commands and scripts
import subprocess

# Importing Path from pathlib for file path manipulation and os for directory handling
from pathlib import Path
import os

# Importing the sys module to check if the script is running as a standalone executable 
# (frozen) or as a regular Python script. This helps determine the correct path to resources.
import sys

#Importing strings used in gui
from strings import GUI_STRINGS

# Function to browse and select the source code directory
def browse_source():
    # Open a directory selection dialog and set the chosen path to source_path
    source_path.set(filedialog.askdirectory(title=GUI_STRINGS['select_source_label']))

# Function to browse and select the destination directory for reports
def browse_destination():
    # Open a directory selection dialog and set the chosen path to destination_path
    destination_path.set(filedialog.askdirectory(title=GUI_STRINGS['select_destination_label']))

# Function to check if the given directory contains at least one C, C++, or header file
def contains_c_cpp_h_files(directory_path):
    """
    Checks if the provided directory contains files with extensions .c, .cpp, or .h.
    Displays an error message if no such files are found.
    """
    # List all files in the directory
    for file_name in os.listdir(directory_path):
        # Check if the file has a .c, .cpp, or .h extension
        if file_name.endswith(('.c', '.cpp', '.h')):
            return True  # Return True if a matching file is found

    # Display an error message if no C/C++ files are found
    messagebox.showerror(GUI_STRINGS['show_err_title'], GUI_STRINGS['error_no_files_message'])
    return False  # Return False if no matching files are found

# Function to execute the static code analyzer using Cppcheck
def run_cppcheck():
    """
    Runs the Cppcheck analysis tool on the selected source directory.
    Ensures that source and destination paths are valid and invokes a batch script.
    """
    # Get the source directory path, replacing forward slashes with backslashes
    source = source_path.get().replace("/", "\\")
      
    # Get the destination directory path, replacing forward slashes with backslashes
    destination = destination_path.get().replace("/", "\\")
    
    # Determine the directory containing the executable or script
    if getattr(sys, 'frozen', False):
       # If the script is running as a bundled executable
       script_dir = Path(sys.executable).parent
    else:
       # If running as a Python script
       script_dir = Path(__file__).resolve().parent

    # Construct the full path to the batch file
    batch_file = script_dir / "Run_CPPCheck.bat"
    
    # Validate that both source and destination paths are provided
    if not source or not destination:
        messagebox.showerror(GUI_STRINGS['show_err_title'], GUI_STRINGS['empty_fields'])
        return

    try:
        # Check if the source directory contains at least one C/C++ file
        if contains_c_cpp_h_files(source):
            # Execute the batch file with the source and destination paths as arguments
            subprocess.run([str(batch_file), source, destination], check=True, shell=True)
            # Display a success message if the batch file runs successfully
            messagebox.showinfo(
            GUI_STRINGS['success_title'], 
            GUI_STRINGS['success_message'].format(destination=destination)
)
    except subprocess.CalledProcessError as e:
        # Display an error message if the batch file execution fails
        messagebox.showerror(GUI_STRINGS['show_err_title'], GUI_STRINGS['batch_execution_err'].format(e=e))

# Create the main application window
root = tk.Tk()
# Set the window title
root.title(GUI_STRINGS['title'])

# Variables to store the selected source and destination paths
source_path = tk.StringVar()
destination_path = tk.StringVar()

# Layout for the GUI components
# Label and entry for the source code directory
tk.Label(root, text=GUI_STRINGS['source_label']).grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=source_path, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text=GUI_STRINGS['browse_button'], command=browse_source).grid(row=0, column=2, padx=10, pady=5)

# Label and entry for the destination directory
tk.Label(root, text=GUI_STRINGS['destination_label']).grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=destination_path, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text=GUI_STRINGS['browse_button'], command=browse_destination).grid(row=1, column=2, padx=10, pady=5)

# Button to trigger the Cppcheck analysis
tk.Button(root, text=GUI_STRINGS['run_button'], command=run_cppcheck).grid(row=2, column=1, pady=10)

# Start the GUI event loop
root.mainloop()
