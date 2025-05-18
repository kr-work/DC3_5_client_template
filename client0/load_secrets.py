import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("MATCH_USER_NAME0")
password = os.getenv("PASS_WORD0")

if __name__ == "__main__":
    print(f"Username: {username}")
    print(f"Password: {password}")