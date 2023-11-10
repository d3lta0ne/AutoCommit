# pylint: disable=unspecified-encoding

import os
import datetime
from dotenv import load_dotenv
load_dotenv()


file_path = os.getenv('FILE_PATH', 'file.txt')
# Set the file path and name


# Create or update the file with the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(file_path, "w") as file:
    file.write(current_date)
    file.close()

# Commit the file to the GitHub repository
commit_message = f"Auto commit: Updated date to {current_date}"

# Github Commit Messages
os.system('git add "{}"'.format(file_path))
os.system('git commit -m "{}"'.format(commit_message))
os.system('git push')
