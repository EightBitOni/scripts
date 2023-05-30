import csv
import os
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Get the list of all browsers
browsers = ["Firefox", "Chrome", "Edge"]

# Create a new folder on the desktop named Backup
backup_folder = os.path.join(os.path.expanduser("~/Desktop"), "Backup " + now.strftime("%Y-%m-%d"))
os.mkdir(backup_folder)

# Get the list of all bookmarks for each browser
for browser in browsers:
  # Get the bookmarks file for the browser
  bookmarks_file = os.path.join(os.path.expanduser("~"), browser, "Bookmarks")

  # Create the bookmarks file if it does not exist
  if not os.path.exists(bookmarks_file):
    pass

  # Open the bookmarks file
  with open(bookmarks_file, "r") as f:
    bookmarks = f.readlines()

  # Write the bookmarks to a CSV file
  with open(os.path.join(backup_folder, browser + "_bookmarks.csv"), "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "URL"])
    for bookmark in bookmarks:
      title, url = bookmark.split(";")
      writer.writerow([title, url])

print("Backup complete!")