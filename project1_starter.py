"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Ameir/AJ Dawson
Date: 10.25.2025

AI Usage: I used AI help me with specific values like character stats 
Example: AI helped with file I/O error handling logic in save_character function
"""

import os


def create_character(name, character_class):
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100 # Starting gold
    }
    return character

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns: tuple of (strength, magic, health)
    
    Formulas designed to meet class archetypes:
    - Warrior: High strength, low magic, high health
    - Mage: Low strength, high magic, medium health  
    - Rogue: Medium strength, medium magic, low health
    - Cleric: Medium strength, high magic, high health
    """
    level_multiplier = level
    
    if character_class == "Warrior":
        strength = 15 + (level_multiplier * 5)
        magic = 5 + (level_multiplier * 1)
        health = 100 + (level_multiplier * 15)

    elif character_class == "Mage":
        strength = 5 + (level_multiplier * 1)
        magic = 15 + (level_multiplier * 5)
        health = 80 + (level_multiplier * 10)

    elif character_class == "Rogue":
        strength = 10 + (level_multiplier * 3)
        magic = 10 + (level_multiplier * 3)
        health = 70 + (level_multiplier * 8)

    elif character_class == "Cleric":
        strength = 10 + (level_multiplier * 2)
        magic = 15 + (level_multiplier * 4)
        health = 90 + (level_multiplier * 12)
    else:
        # Default stats
        strength = 10 + (level_multiplier * 2)
        magic = 10 + (level_multiplier * 2)
        health = 80 + (level_multiplier * 10)
        
    return (strength, magic, health)

def save_character(character, filename):
    """
    Saves character to text file in specific format.
    Returns: True if successful, False if error occurred.
    
    Note: Without 'try/except', this function cannot gracefully handle errors
    like permission denied or invalid path. It assumes success on execution.
    """
    save_format = [
        f"Character Name: {character['name']}",
        f"Class: {character['class']}",
        f"Level: {character['level']}",
        f"Strength: {character['strength']}",
        f"Magic: {character['magic']}",
        f"Health: {character['health']}",
        f"Gold: {character['gold']}",
    ]
    
    f = open(filename, 'w')
    f.write('\n'.join(save_format))
    f.close()
    return True

def load_character(filename):
    if not os.path.exists(filename):
        return None

    f = open(filename, 'r')
    lines = f.read().splitlines()
    f.close()

    if len(line) < 7:
        return None

    char_data = {}
    key_mapping = {
        "Character Name": "name", "Class": "class", "Level": "level",
        "Strength": "strength", "Magic": "magic", "Health": "health", "Gold": "gold"
    }

    for line in line:
        if ":" in line:
            key_label, value = line.split(":", 1)
            key_label = key_label.strip()
            value = value.strip()
            
            if key_label in key_mapping:
                dict_key = key_mapping[key_label]
                
                # Numeric conversion will crash if data is corrupted (e.g., 'Level: five')
                if dict_key in ["level", "strength", "magic", "health", "gold"]:
                    char_data[dict_key] = int(value) 
                else:
                    char_data[dict_key] = value
    
    required_keys = ["name", "class", "level", "strength", "magic", "health", "gold"]
    if all(k in char_data for k in required_keys):
        return char_data
    else:
        return None

def display_character(character):
    """
    Prints formatted character sheet.
    Returns: None (prints to console)
    """
    if not character:
        print("Error: No character data to display.")
        return

    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character.get('name', 'N/A')}")
    print(f"Class: {character.get('class', 'N/A')}")
    print(f"Level: {character.get('level', 'N/A')}")
    print(f"Strength: {character.get('strength', 'N/A')}")
    print(f"Magic: {character.get('magic', 'N/A')}")
    print(f"Health: {character.get('health', 'N/A')}")
    print(f"Gold: {character.get('gold', 'N/A')}")
    print("=======================\n")
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character['level'] += 1
    
    strength, magic, health = calculate_stats(character['class'], character['level'])
    
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health
    character['gold'] += 50 

# Main program area (optional - for testing your functions
if __name__ == "__main__":
        test_filename = "my_character.txt"
        print("=== CHARACTER CREATOR ===")
        print("Test your functions here!")
    
    # Example usage:
        char = create_character("TestHero", "Warrior")
        display_character(char)
    
        print(f"Attempting to save character to {test_filename} (No error handling for OS errors)...")
        save_character(char, test_filename)
    
        print(f"\nAttempting to load character from {test_filename}...")
        loaded = load_character(test_filename)
    
if loaded:
    print("Load successful. Displaying loaded character:")
    display_character(loaded)
        
    level_up(loaded)
    print("Character leveled up:")
    display_character(loaded)
        
        # Clean up the test file
    if  os.path.exists(test_filename):
        os.remove(test_filename)
        print(f"\nCleaned up test file: {test_filename}")
else:
    print("Load failed (File not found).")
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
