import os

def validate_config(file_path):
    """
    Validates the configuration file format.
    Ensures each non-empty line contains an '=' character.
    """
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found."
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        if line.strip() and '=' not in line:
            return f"Invalid line found: {line.strip()}"
            
    return "Configuration is valid."

if __name__ == "__main__":
    config_file = "config.txt"
    print(validate_config(config_file))
