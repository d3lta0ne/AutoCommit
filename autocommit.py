# pylint: disable=unspecified-encoding

import os
import datetime

# Set the file path and name
file_path = "file.txt"

# Create or update the file with the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(file_path, "w") as file:
    file.write(current_date)

# Commit the file to the GitHub repository
commit_message = f"Auto commit: Updated date to {current_date}"

# Github Commit Messages
os.system('git add "{}"'.format(file_path))
os.system('git commit -m "{}"'.format(commit_message))

os.system('git push')
