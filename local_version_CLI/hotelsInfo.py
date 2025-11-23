#Importing requests and os libraries to make request and access env variable respectively
import requests
import os
import time
url_list = "https://apidojo-booking-v1.p.rapidapi.com/properties/v2/list"
url_getroom = "https://apidojo-booking-v1.p.rapidapi.com/properties/v2/get-rooms"
url_single_hotl = "https://apidojo-booking-v1.p.rapidapi.com/properties/detail"
url_filter = "https://apidojo-booking-v1.p.rapidapi.com/filters/list"
RAPID_BOOKING_API_KEY = os.getenv("RAPID_BOOKING_API_KEY")

def hotel_finder(search_type):
    querystring = {"offset":"0",
                   "guest_qty":"1", 
                   "dest_ids":"-3712125",
                   "room_qty":"1",
                   "search_type":"city",
                   "arrival_date": "2025-11-27", 
                   "departure_date": "2025-11-29"
                   }
    
    
    arrival_date = input("\t\tArrival date(yyyy-mm-dd): ")
    departure_date = input("\t\tDeparture date(yyyy-mm-dd):")

    offset = input("\t\tOffset(beginning page number): ")
    guest_qty = input("\t\tGuest quantity: ")
    dest_ids = input("\t\tDestination Id(id found in destination earlier): ")
    room_qty = input("\t\tRoom quantity: ")

    querystring.update({"offset": offset, 
                        "guest_qty": guest_qty, 
                        "dest_ids": dest_ids, 
                        "room_qty": room_qty, 
                        "arrival_date": arrival_date, 
                        "departure_date": departure_date})
    querystring["search_type"] = search_type.lower()


    headers = {
        "x-rapidapi-key": RAPID_BOOKING_API_KEY,
        "x-rapidapi-host": "apidojo-booking-v1.p.rapidapi.com"
    }
    response = requests.get(url_list, headers=headers, params=querystring)
    response_dic = response.json()
    hotels = response_dic.get("result", {})

    print(f"\n\t\t====Details of hotels in the \"{search_type}\"===")
    print('Finding hotel for you-----')
    time.sleep(4)
    if response.status_code == 200:
        if isinstance(response_dic, dict) and str(response_dic.get("code", "")) != "" and response_dic.get("code") != 200:
            print(f"\t\tAPI Error: {response_dic.get('message', 'Unknown error')}")
            return
        else:
            if hotels:
                for ciho in hotels:
                    if ciho.get("type") == "banner":
                        continue
                    else:
                        print(f"\t\tHotel Name: {ciho['hotel_name']}")
                        print(f"\t\tHotel Id: {ciho['hotel_id']}")
                        print(f"\t\tSearch Id: {ciho.get('search_ids', 'N/A')}")
                        print(f"\t\tAddress: {ciho.get('address','N/A')}")
                        print(f"\t\tRating: {ciho.get('review_score', 'N/A')}")
                        print(f"\t\tReview Count: {ciho.get('review_nr', 'N/A')}")
                        print(f"\t\tDistance to City center: {ciho.get('distance_to_city_center', 'N/A')}")
                        print(f"\t\tDistrict: {ciho.get('district', 'N/A')}")
                        price = ciho.get("composite_price_breakdown", {}).get("all_inclusive_amount", {})
                        print(f"\t\tPrice per night: {price.get('value', 'N/A')}")
                        print(f"\t\tCurrency: {price.get('currency', 'N/A')}")
                        print("=====================================================")
            else:
                print("\t\t❌ No hotels Found")
    else:
        print("\t\t❌ Request is not successful")

def get_rooms():
    room_querystring = {}
    headers = {
	"x-rapidapi-key": RAPID_BOOKING_API_KEY,
	"x-rapidapi-host": "apidojo-booking-v1.p.rapidapi.com"
    }

    hotel_id = input("\t\tHotel Id or check(224649): ")
    departure_date = input("\t\tDeparture date(yyyy-mm-dd): ")
    arrival_date = input("\t\tArrival date(yyyy-mm-dd): ")
    rec_guest_qty = input("\t\tGuest quantity: ")
    rec_room_qty = input("\t\tRoom quantity: ")
    room_querystring.update({"hotel_id": hotel_id, "departure_date": departure_date, "arrival_date": arrival_date, "rec_guest_qty":rec_guest_qty, "rec_room_qty":rec_room_qty})

    room_response = requests.get(url_getroom, headers=headers, params=room_querystring)
    if room_response.status_code == 200:
        room_response = room_response.json()
        if isinstance(room_response, dict) and str(room_response.get("code", "")) != "" and room_response.get("code") != 200:
            print(f"\t\tAPI Error: {room_response.get('message', 'Unknown error')}")
            return
        else:
            for room_deta in room_response:
                room = room_deta.get("rooms")
                if isinstance(room, dict):     
                    for room_type, room_details in room.items():
                        print("Finding your room detail-----")
                        time.sleep(3)
                        print("=========================================================")
                        print(f"\t\tRoom type Id: {room_type}")
                        room_details_value = room_details.get("facilities",[])
                        for facility in room_details_value:
                            print(f"\t\tRoom ID: {facility.get('id', 'N/A')}")
                            print(f"\t\tName: {facility.get('name', 'N/A')}")
                            print(f"\t\tFacility description: {facility.get('alt_facilitytype_name', 'N/A')}")
                            print(f"-------------------------------")                   
                        print(f"\t\tDescription: {room_details.get('description', 'N/A')}")
                        bed_desc = room_details.get("bed_configurations", [])
                        for bed in bed_desc:
                            bed_info = bed.get('bed_types', [])
                            for bed_detail in bed_info:
                                print(f"\t\tBed description: {bed_detail.get('description', 'N/A')}")
                                print(f"\t\tNumber of beds: {bed_detail.get('name_with_count', 'N/A')}")
                        image = room_details.get("photos", [])
                        for image_detail in image:
                            print(f"Photo_URL: {image_detail.get('url_original', 'N/A')}")

                        print("------------------------------------------")
                else:
                    print("\t\tOops! Couldn't find requested data")
    else:
        print("\t\t❌ Request is not successful")

def get_sing_hotl():
    querystring_hotel = {}
    headers = {
	"x-rapidapi-key": RAPID_BOOKING_API_KEY,
	"x-rapidapi-host": "apidojo-booking-v1.p.rapidapi.com"
    }
    arrival_date = input("\t\tArrival date(yyyy-mm-dd): ")
    departure_date = input("\t\tDeparture date(yyyy-mm-dd): ")
    hotel_id = input("\t\tHotel Id or check(224649): ")
    search_id = input("\t\tSearch Id or check(property_card_224649): ")
    rec_guest_qty = input("\t\tGuest number: ")
    rec_room_qty = input("\t\tRoom number: ")
    querystring_hotel.update({"arrival_date": arrival_date, 
                              "departure_date": departure_date,
                              "hotel_id": hotel_id,
                              "search_id": search_id,
                              "rec_guest_qty": rec_guest_qty,
                              "rec_room_qty": rec_room_qty})
    response = requests.get(url_single_hotl, headers=headers, params=querystring_hotel)
    if response.status_code == 200:
        response_list = response.json()
        # This line below handles server error
        if isinstance(response_list, dict) and str(response_list.get("code", "")) != "" and response_list.get("code") != 200:
            print(f"\t\tAPI Error: {response_list.get('message', 'Unknown error')}")
            return
        else:
            for hot_detail in response_list:
                time.sleep(3)
                print("Finding your hotel-----")
                print(f"==============Details of {hot_detail.get('hotel_name', 'N/A')}===========")

                print(f"\t\tHotel name: {hot_detail.get('hotel_name', 'N/A')}")
                print(f"\t\tCity: {hot_detail.get('city', 'N/A')}")
                print(f"\t\tDistrict: {hot_detail.get('district', 'N/A')}")
                print(f"\t\tAddress line: {hot_detail.get('hotel_address_line', 'N/A')}")
                print(f"\t\tAvailable rooms: {hot_detail.get('available_rooms', 'N/A')}")
                print(f"\t\tReserved rooms: {hot_detail.get('max_rooms_in_reservation', 'N/A')}")
                facilities = hot_detail.get('facilities_block', {})
                facility_list = facilities.get('facilities', [])
                # Error occured here 
                faci_name = [facility.get("name", "N/A") for facility in facility_list]
                print("\t\tFacilities:", ", ".join(faci_name))
    else:
        print("\t\t❌ Request is not successful.")



















    




        



    