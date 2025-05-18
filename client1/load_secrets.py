import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("MATCH_USER_NAME1")
password = os.getenv("PASS_WORD1")

if __name__ == "__main__":
    print(f"Username: {username}")
    print(f"Password: {password}")