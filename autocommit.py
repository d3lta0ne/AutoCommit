# pylint: disable=unspecified-encoding
import datetime
import os
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the file path and name
file_path = os.getenv('FILE_PATH', 'file.txt')

# Create or update the file with the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(file_path, "w") as file:
    file.write(current_date)

# Commit the file to the GitHub repository
commit_message = f"Auto commit: Updated date to {current_date}"

# Github Commit Messages
subprocess.run(['git', 'add', file_path], check=True)
subprocess.run(['git', 'commit', '-m', commit_message], check=True)
subprocess.run(['git', 'push'], check=True)
