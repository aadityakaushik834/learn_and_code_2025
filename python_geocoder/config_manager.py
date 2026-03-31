import configparser
import os
import sys

def get_api_key(config_path='config.ini'):
    if not os.path.exists(config_path):
        print(f"Error: Configuration file '{config_path}' not found.", file=sys.stderr)
        sys.exit(1)
        
    config = configparser.ConfigParser()
    config.read(config_path)
    
    if 'API' not in config or 'KEY' not in config['API']:
        print("Error: Missing 'API' block or 'KEY' in configuration file.", file=sys.stderr)
        sys.exit(1)
        
    api_key = config['API']['KEY'].strip()
    if not api_key or api_key == 'YOUR_GOOGLE_MAPS_API_KEY_HERE':
        print("Error: Please replace the placeholder API key in config.ini with a valid Google Maps API Key.", file=sys.stderr)
        sys.exit(1)
        
    return api_key
