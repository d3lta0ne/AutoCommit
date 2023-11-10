# pylint: disable=unspecified-encoding
from dotenv import load_dotenv
import datetime
import os
load_dotenv()

print("****Script started****")
file_path = os.getenv('FILE_PATH', 'file.txt')
# Set the file path and name


# Create or update the file with the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("****File opened****")
with open(file_path, "w") as file:
    file.write(current_date)
    file.close()
    print("File closed")

# Commit the file to the GitHub repository
commit_message = f"Auto commit: Updated date to {current_date}"

# Github Commit Messages
os.system('git add "{}"'.format(file_path))
print("****Git Add****")

os.system('git commit -m "{}"'.format(commit_message))
print("****Git Commit****")

os.system('git push')
print("****Git Pushed****")
print("****Script ended****")
