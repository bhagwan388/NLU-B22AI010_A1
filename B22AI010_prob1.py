"""
Course: CSL 7640 (Natural Language Understanding)
Assignment: 1 | Problem 1: REGGY++
Name: Bhagwan Arsewad | Roll Number: B22AI010
Description: A Regex-based chatbot that extracts surnames, parses 
             diverse date formats for age calculation, and handles 
             mood detection with typo tolerance.
"""

import re
from datetime import date

def extract_surname(name):
    """
    Uses regex to find the last word in a string, assuming it's the surname.
    The pattern \s(\w+)$ looks for a space followed by word characters 
    until the end of the line.
    """
    match = re.search(r'\s([A-Za-z]+)$', name.strip())
    if match:
        return match.group(1)
    return "Friend" # Fallback if only one name is provided

def get_age(birth_str):
    """
    Tries multiple regex patterns to extract day, month, and year.
    Calculates age based on the current system date.
    """
    today = date.today()
    d, m, y = None, None, None

    # Month mapping for text-based dates
    month_map = {
        'jan': 1, 'january': 1, 'feb': 2, 'february': 2, 'mar': 3, 'march': 3,
        'apr': 4, 'april': 4, 'may': 5, 'jun': 6, 'june': 6, 'jul': 7, 
        'july': 7, 'aug': 8, 'august': 8, 'sep': 9, 'september': 9,
        'oct': 10, 'october': 10, 'nov': 11, 'november': 11, 'dec': 12, 'december': 12
    }

    # Pattern 1: Numeric formats like 25-08-2004 or 08/25/04
    # We look for digits separated by - or /
    num_match = re.search(r'(\d{1,2})[-/](\d{1,2})[-/](\d{2,4})', birth_str)
    
    # Pattern 2: Text formats like "25 August 2004" or "Aug 25 2004"
    text_match = re.search(r'(\d{1,2})?\s*([A-Za-z]+)\s*(\d{1,2})?[\s,]*(\d{2,4})', birth_str)

    if num_match:
        # Assuming DD-MM-YYYY format for this specific capture
        d, m, y = int(num_match.group(1)), int(num_match.group(2)), int(num_match.group(3))
    elif text_match:
        # Extract components from groups
        # If group 1 is missing, it might be "Month DD YYYY"
        day_part = text_match.group(1) or text_match.group(3)
        month_part = text_match.group(2).lower()[:3] # Normalize to 3 chars
        year_part = text_match.group(4)
        
        if day_part and month_part in month_map:
            d = int(day_part)
            m = month_map[month_part]
            y = int(year_part)

    if d and m and y:
        # Handle 2-digit years (e.g., '04' -> 2004)
        if y < 100:
            y += 2000 if y < 30 else 1900
            
        # Calculation logic: Current year - birth year
        # Adjustment if current date is before the birthday in the current year
        current_age = today.year - y - ((today.month, today.day) < (m, d))
        return current_age
    
    return None

def handle_mood(user_text):
    """
    Detects mood using regex patterns with '+' to handle repeated 
    characters/typos common in chat.
    """
    text = user_text.lower()
    
    # Positive patterns (happy, good, fine, etc.)
    if re.search(r'h+a+p+y+|g+o+d+|f+i+n+e+|e+x+c+i+t+|a+m+a+z+', text):
        return "That's wonderful! Stay positive."
    
    # Negative patterns (sad, bad, tired, etc.)
    elif re.search(r's+a+d+|b+a+d+|t+i+r+e+d+|u+n+h+a+p+y+|o+f+u+l+', text):
        return "I'm sorry to hear that. I hope your day gets better."
    
    else:
        return "I see. It's always good to process your feelings."

def run_chatbot():
    print("--- Reggy++ Chatbot (CSL 7640) ---")
    
    # Get Name
    user_name = input("Reggy++: Hi there! What is your full name? \n>> ")
    surname = extract_surname(user_name)
    print(f"Reggy++: Nice to meet you, Mr./Ms. {surname}!")

    # Get Birthday
    bday_input = input(f"Reggy++: So {surname}, when is your birthday? (e.g., 25-08-2004 or 25 Aug 2004)\n>> ")
    age = get_age(bday_input)
    
    if age is not None:
        print(f"Reggy++: Wow, so you are {age} years old!")
    else:
        print("Reggy++: Hmm, that date format is a bit tricky for me, but I'll try to remember it.")

    # Get Mood
    mood_input = input("Reggy++: How are you feeling today?\n>> ")
    response = handle_mood(mood_input)
    print(f"Reggy++: {response}")
    
    print("\nReggy++: It was nice chatting with you! Goodbye.")

if __name__ == "__main__":
    run_chatbot()