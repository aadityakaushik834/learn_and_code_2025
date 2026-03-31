def validate_location(location):
    
    if not isinstance(location, str):
        raise ValueError("Location must be a string.")
        
    location = location.strip()
    
    if not location:
        raise ValueError("Location name cannot be empty.")
        
    # Basic sanity check on length, though some locations might be short
    if len(location) < 2:
        raise ValueError("Location name is too short to be valid.")
        
    if len(location) > 100:
        raise ValueError("Location name is too long.")
        
    return location
