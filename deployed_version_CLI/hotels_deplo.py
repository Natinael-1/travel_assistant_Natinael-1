import requests
import os

url_list = "https://apidojo-booking-v1.p.rapidapi.com/properties/v2/list"
RAPID_BOOKING_API_KEY = os.getenv("RAPID_BOOKING_API_KEY")

# This block of code accepts arguements
def hotel_finder(search_type, dest_id, arrival, departure):
    querystring = {
        "offset":"0",
        "guest_qty":"1", 
        "dest_ids": dest_id,
        "room_qty":"1",
        "search_type": search_type.lower(),
        "arrival_date": arrival, 
        "departure_date": departure
    }
    
    headers = {
        "x-rapidapi-key": RAPID_BOOKING_API_KEY,
        "x-rapidapi-host": "apidojo-booking-v1.p.rapidapi.com"
    }
    
    print(f"\n\t\t====Details of hotels in \"{dest_id}\"===")
    response = requests.get(url_list, headers=headers, params=querystring)
    response_dic = response.json()
    hotels = response_dic.get("result", {})

    if response.status_code == 200:
        if hotels:
            for ciho in hotels:
                if ciho.get("type") == "banner": continue
                print(f"\t\tHotel Name: {ciho['hotel_name']}")
                print(f"\t\tHotel Id: {ciho['hotel_id']}")
                print(f"\t\tAddress: {ciho.get('address','N/A')}")
                print(f"\t\tRating: {ciho.get('review_score', 'N/A')}")
                price = ciho.get("composite_price_breakdown", {}).get("all_inclusive_amount", {})
                print(f"\t\tPrice: {price.get('value', 'N/A')} {price.get('currency', 'N/A')}")
                print("=====================================================")
        else:
            print("\t\t❌ No hotels Found")
    else:
        print(f"\t\t❌ Request failed: {response.text}")