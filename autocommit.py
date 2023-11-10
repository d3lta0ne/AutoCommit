# pylint: disable=unspecified-encoding
from dotenv import load_dotenv
import datetime
import os
import subprocess

load_dotenv()

print("****Script started****")
file_path = os.getenv('FILE_PATH', 'file.txt')

# Set the file path and name

# Create or update the file with the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("****File opened****")
with open(file_path, "w") as file:
    file.write(current_date)
    print("File closed")

# Commit the file to the GitHub repository
commit_message = f"Auto commit: Updated date to {current_date}"

# Github Commit Messages
subprocess.run(['git', 'add', file_path], check=True)
print("****Git Add****")

subprocess.run(['git', 'commit', '-m', commit_message], check=True)
print("****Git Commit****")

subprocess.run(['git', 'push'], check=True)
print("****Git Pushed****")
print("****Script ended****")
