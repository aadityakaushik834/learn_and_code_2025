import urllib.request
import urllib.parse
import json

class GeocodingException(Exception):
    pass

def get_coordinates(location, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': location,
        'key': api_key
    }
    query_string = urllib.parse.urlencode(params)
    url = f"{base_url}?{query_string}"
    
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.status != 200:
                raise GeocodingException(f"HTTP Error: {response.status}")
                
            data = json.loads(response.read().decode('utf-8'))
            
            status = data.get('status')
            if status == 'OK':
                results = []
                for result in data['results']:
                    formatted_address = result.get('formatted_address', 'Unknown Address')
                    location_data = result.get('geometry', {}).get('location', {})
                    lat = location_data.get('lat')
                    lng = location_data.get('lng')
                    if lat is not None and lng is not None:
                        results.append({
                            'address': formatted_address,
                            'lat': lat,
                            'lng': lng
                        })
                return results
            elif status == 'ZERO_RESULTS':
                return []
            elif status == 'REQUEST_DENIED':
                error_msg = data.get('error_message', 'Request was denied by Google API.')
                raise GeocodingException(f"API Error - Request Denied: {error_msg}")
            else:
                error_msg = data.get('error_message', status)
                raise GeocodingException(f"API Error ({status}): {error_msg}")
                
    except urllib.error.URLError as e:
        raise GeocodingException(f"Network error: {str(e)}")
    except json.JSONDecodeError:
        raise GeocodingException("Failed to parse response from Google Geocoding API.")
