import sys
from config_manager import get_api_key
from validator import validate_location
from geocoding_service import get_coordinates, GeocodingException

def main():
    print("=== Google Geocoding API Utility ===")
    
    api_key = get_api_key('config.ini')
    
    while True:
        try:
            raw_input = input("\nEnter a location name (or type 'quit' to exit): ")
            if raw_input.strip().lower() in ('quit', 'q', 'exit'):
                print("Exiting application...")
                break
                
            try:
                location = validate_location(raw_input)
            except ValueError as ve:
                print(f"Input Error: {ve}", file=sys.stderr)
                continue
            
            print(f"Fetching coordinates for '{location}'...")
            results = get_coordinates(location, api_key)
            
            if not results:
                print("No results found for that location. Please try a different name.")
                continue
                
            print(f"\nFound {len(results)} result(s):")
            print("-" * 40)
            for i, result in enumerate(results, 1):
                print(f"Result #{i}")
                print(f"  Address  : {result['address']}")
                print(f"  Latitude : {result['lat']}")
                print(f"  Longitude: {result['lng']}")
                print("-" * 40)
                
        except GeocodingException as ge:
            print(f"Error fetching data: {ge}", file=sys.stderr)
        except KeyboardInterrupt:
            print("\nExiting application...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
