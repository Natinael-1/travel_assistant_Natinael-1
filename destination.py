import requests
import os

url_autocomplete = "https://apidojo-booking-v1.p.rapidapi.com/locations/auto-complete"
RAPID_BOOKING_API_KEY = os.getenv("RAPID_BOOKING_API_KEY")

def displayCityInfo():
    city = input("🏢 City you want to travel to: ")

    query_dic = {
        "text": city,
        "languagecode": "en-us"
    }

    headers = {
        "x-rapidapi-key": RAPID_BOOKING_API_KEY,
        "x-rapidapi-host": "apidojo-booking-v1.p.rapidapi.com"
    }

    response = requests.get(url_autocomplete, headers=headers, params=query_dic)

    if response.status_code == 200:
        response_list = response.json()

        # Find the first CITY result
        city_item = None
        for item in response_list:
            if item["dest_type"] == "city":
                city_item = item
                break

        if city_item is None:
            print("❌ No city result found.")
            return
        print(f"\n================== Details about \"{city}\" ====================")
        print(f"Destination Found: {city_item['label']}")
        print(f"Country: {city_item['country']}")
        print(f"Region: {city_item['region']}")
        print(f"Timezone: {city_item['timezone']}")
        print(f"Hotels Available: {city_item['nr_hotels']}")
        print(f"Destination ID: {city_item['dest_id']}")
        print("=============================================================\n")

    elif response.status_code == 204:
        print("Missing or invalid parameters.")
    elif response.status_code == 302:
        print("Reached page but response is empty or redirected.")
    elif response.status_code == 400:
        print("Bad input parameter.")
    elif response.status_code == 403:
        print("Access denied due to bot protection on server.")

displayCityInfo()


