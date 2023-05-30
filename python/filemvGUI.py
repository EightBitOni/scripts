import os
import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a label
label = tk.Label(root, text="Backup")

# Create a button
button = tk.Button(root, text="Run", command=backup)

# Place the label and button on the main window
label.pack()
button.pack()

# Start the main loop
root.mainloop()

def backup():
  # Get the current date and time
  now = str(datetime.datetime.now())

  # Create a new folder on the desktop named Backup
  backup_folder = os.path.join(os.path.expanduser("~/Desktop"), "Backup " + now)
  os.mkdir(backup_folder)

  # Get the list of all files in the Downloads, Documents, Pictures, Music, and Videos folders
  files = []
  for folder in ["Downloads", "Documents", "Pictures", "Music", "Videos"]:
    files.extend(os.listdir(os.path.join(os.path.expanduser("~"), folder)))

  # Copy all files to the Backup folder
  for file in files:
    shutil.copy(os.path.join(os.path.expanduser("~"), file), backup_folder)

  # Ask for confirmation
  confirmation = input("Are you sure you want to run the backup? (y/n): ")

  if confirmation == "y":
    # Run the backup
    backup()
  else:
    # Do nothing
    