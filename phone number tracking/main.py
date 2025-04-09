import phonenumbers
from phonenumbers import geocoder, carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

def get_phone_number_info(phone_number):
    try:
        # Parse the phone number
        new_number = phonenumbers.parse(phone_number)

        # Get the location description
        location = geocoder.description_for_number(new_number, "en")
        print(f"Location: {location}")

        # Get the carrier name
        service_name = carrier.name_for_number(new_number, "en")
        print(f"Service: {service_name}")

        # Geocode location
        key = "your key"  # Replace with your OpenCage API key
        geocoder_service = OpenCageGeocode(key)
        query = str(location)
        result = geocoder_service.geocode(query)

        if not result:
            print("Could not find location coordinates.")
            return

        lat = result[0]['geometry']['lat']
        lng = result[0]['geometry']['lng']
        print(f"Latitude: {lat}, Longitude: {lng}")

        # Create map
        my_map = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(my_map)

        # Save the map to HTML
        my_map.save("location.html")
        print("Location tracking completed. Map saved as 'location.html'.")

    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error parsing phone number: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input phone number
number = input("Please provide your phone number (with country code): ")
get_phone_number_info(number)

print("Thank you!")
