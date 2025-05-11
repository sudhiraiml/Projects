import random
from datetime import datetime, timedelta
import string

# List of 10 user names
users = ["Ashish", "Komal", "Rahul", "Priya", "Vikas", "Sneha", "Ankit", "Neha", "Rohit", "Divya"]

# Sample message templates
message_templates = [
    "Thanks {}! Can you explain the first task more?",
    "Hey {}, can we discuss the project timeline?",
    "Hi {}, I need help with the code review.",
    "Great job, {}! What's the next step?",
    "Hello {}, can you share the meeting notes?",
    "Thanks for the update, {}! Any issues?",
    "Hey {}, let's finalize the design today.",
    "Hi {}, can you check the bug I reported?",
    "Good work, {}! Can we schedule a call?",
    "Hello {}, do you have the latest report?"
]

# Function to generate random date between two dates
def random_date(start_date, end_date):
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    return start_date + timedelta(days=random_days)

# Function to generate random time
def random_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    return f"{hour:02}:{minute:02}"

# Function to generate a random message
def random_message(sender):
    receiver = random.choice([u for u in users if u != sender])  # Ensure receiver is not sender
    template = random.choice(message_templates)
    return template.format(receiver)

# Generate 1000 entries
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 5, 11)
entries = []

for _ in range(1000):
    date = random_date(start_date, end_date).strftime("%d/%m/%Y")
    time = random_time()
    user = random.choice(users)
    message = random_message(user)
    entry = f"{date}, {time} - {user}: {message}"
    entries.append(entry)

# Write to a text file
with open("chat_log.txt", "w", encoding="utf-8") as file:
    for entry in entries:
        file.write(entry + "\n")

print("Text file 'chat_log.txt' with 1000 entries has been created.")