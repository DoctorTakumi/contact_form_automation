import time

# function to change domain based on current time in seconds
# def get_next_email():
#     timestamp = int(time.time())  # Get current time in seconds
#     email = f"testnirachun1208+{timestamp}@gmail.com"
#     return email

# similar function to change local instead of domain
def get_next_email():
    timestamp = int(time.time())  # Get current time in seconds
    email = f"{timestamp}@gmail.com"
    return email
