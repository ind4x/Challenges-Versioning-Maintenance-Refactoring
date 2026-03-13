import logging
import logging
import os

def validate_config(file_path):
    if not os.path.exists(file_path):
        return "Error: config.txt not found."
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        if line.strip() and '=' not in line:
            return f"Invalid line found: {line.strip()}"
            
    return "Configuration is valid."

if __name__ == "__main__":
    print(validate_config("config.txt"))
