# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 23:11:06 2025

@author: johnm
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import requests
import sys
from datetime import datetime, timedelta

OPENWEATHER_KEY = ""
currency_list = {
    'USD':"US Dollar",
    'ARS':"Argentine Peso",
    'BBD':"Barbados Dollar",
    'BSD':"Bahamian Dollar",
    'PYG':"Paraguat Guarani",
    'PAB':"Panamanian Balboa",
    'BRL':"Brazilian Real",
    "BMD": "Bermudian Dollar",
    "BOB": "Bolivian Boliviano",
    "BZD": "Belize Dollar",
    "XCD": "East Caribbean Dollar",
    "DOP": "Dominican Peso",
    "COP": "Colombian Peso",
    "CRC": "Costa Rican Colon",
    "CUP": "Cuban Peso",
    "HTG": "Haitian Gourde",
    "ANG": "Netherlands Antillian Guilder",
    "HNL": "Honduran Lempira",
    "CAD": "Canadian Dollar",
    "KYD": "Cayman Islands Dollar",
    "PEN": "Peruvian Sol",
    "MXN": "Mexican Peso",
    "NIO": "Nicaraguan Cordoba Oro",
    "TTD": "Trinidad and Tobago Dollar",
    "GTQ": "Guatemalan Quetzal",
    "VES": "Venezuelan Bolivar",
    "UYU": "Uruguay Peso",
    "JMD": "Jamaican Dollar",
    "CLP": "Chilean Peso",
    "AUD": "Australian Dollar",
    "MOP": "Macau Pataca",
    "PKR": "Pakistan Rupee",
    "PHP": "Philippine Peso",
    "FJD": "Fiji Dollar",
    "HKD": "Hong Kong Dollar",
    "KRW": "Korean Won",
    "KHR": "Cambodian Riel",
    "LAK": "Lao Kip",
    "MYR": "Malaysian Ringgit",
    "BDT": "Bangladeshi Taka",
    "MMK": "Myanmar Kyat",
    "NPR": "Nepalese Rupee",
    "CNY": "Chinese Yuan Renminbi",
    "JPY": "Japanese Yen",
    "SCR": "Seychelles Rupee",
    "LKR": "Sri Lanka Rupee",
    "XPF": "CFP Franc",
    "THB": "Thai Baht",
    "BND": "Brunei Dollar",
    "SGD": "Singapore Dollar",
    "TWD": "Taiwan Dollar",
    "NZD": "New Zealand Dollar",
    "INR": "Indian Rupee",
    "IDR": "Indonesian Rupiah",
    "VND": "Vietnamese Dong",
    "ALL": "Albanian Lek",
    "BYN": "Belarusian Ruble",
    "BGN": "Bulgarian Lev",
    "ISK": "Iceland Krona",
    "PLN": "Polish Zloty",
    "DKK": "Danish Krone",
    "RUB": "Russian Ruble",
    "CZK": "Czech Koruna",
    "HRK": "Croatian Kuna",
    "RON": "Romanian Leu",
    "MKD": "Macedonia Denar",
    "MDL": "Moldovan Leu",
    "NOK": "Norwegian Krone",
    "EUR": "Euro",
    "SEK": "Swedish Krona",
    "CHF": "Swiss Franc",
    "RSD": "Serbian Dinar",
    "UAH": "Ukraine Hryvnia",
    "HUF": "Hungarian Forint",
    "GBP": "British Pound",
    "AED": "United Arab Emirates Dirham",
    "OMR": "Omani Rial",
    "AZN": "Azerbaijani Manat",
    "BHD": "Bahraini Dinar",
    "GEL": "Georgian Lari",
    "KZT": "Kazakhstan Tenge",
    "KGS": "Kyrgyzstani Som",
    "QAR": "Qatari Rial",
    "KWD": "Kuwaiti Dinar",
    "LBP": "Lebanese Pound",
    "SAR": "Saudi Riyal",
    "TRY": "Turkish Lira",
    "TMT": "Turkmenistan Manat",
    "UZS": "Uzbekistan Som",
    "AMD": "Armenian Dram",
    "YER": "Yemeni Rial",
    "IQD": "Iraqi Dinar",
    "IRR": "Iranian Rial",
    "ILS": "Israeli New Shekel",
    "JOD": "Jordanian Dinar",
    "DZD": "Algerian Dinar",
    "EGP": "Egyptian Pound",
    "ETB": "Ethiopian Birr",
    "AOA": "Angolan Kwanza",
    "BWP": "Botswana Pula",
    "BIF": "Burundi Franc",
    "XOF": "CFA BCEAO Franc",
    "CVE": "Cape Verde Escudo",
    "GMD": "Gambian Dalasi",
    "DJF": "Djibouti Franc",
    "GNF": "Guinea Franc",
    "GHS": "Ghanaian Cedi",
    "KES": "Kenyan Shilling",
    "LSL": "Lesotho Loti",
    "LYD": "Libyan Dinar",
    "RWF": "Rwanda Franc",
    "MWK": "Malawi Kwacha",
    "MUR": "Mauritius Rupee",
    "MAD": "Moroccan Dirham",
    "NAD": "Namibian Dollar",
    "ZAR": "South African Rand",
    "NGN": "Nigerian Naira",
    "SZL": "Swaziland Lilangeni",
    "SDG": "Sudanese Pound",
    "SOS": "Somali Shilling",
    "TZS": "Tanzanian Shilling",
    "TND": "Tunisian Dinar",
    "UGX": "Uganda Shilling",
    "ZMW": "Zambian Kwacha",
    "XAF": "CFA BEAC Franc",
    "BAM": "Bosnia and Herzegovina Marka",
    "SYP": "Syrian Pound"
}

myDict = {
    "countries": {
        "Argentina": {"capital": " Buenos Aires","currency": "Argentine Peso (ARS)","vacation": "Tango in Buenos Aires and explore the stunning landscapes of Patagonia."},
        "Australia": {"capital": "Canberra","currency": "Australian Dollar (AUD)","vacation": "Visit the Great Barrier Reef"},
        "Brazil": {"capital": "Bras\u00edlia","currency": "Brazilian Real (BRL)","vacation": "Visit Rio de Janeiro"},
        "Canada": {"capital": "Ottawa","currency": "Canadian Dollar (CAD)","vacation": "Visit Niagara Falls"},
        "China": {"capital": "Beijing","currency": "Chinese Yuan (CNY)","vacation": " Explore the Great Wall of China and visit the Forbidden City."},
        "Egypt": {"capital": "Cairo","currency": "Egyptian Pound (EGP)","vacation": "Discover the ancient pyramids and the temples of Luxor."},
        "France": {"capital": "Paris","currency": "Euro (EUR)","vacation": "Visit the Eiffel Tower"},
        "Germany": {"capital": "Berlin","currency": "Euro (EUR)","vacation": "Visit the Reichstag"},
        "Greece": {"capital": "Athens","currency": "Euro (EUR)","vacation": "Visit the Acropolis in Athens and relax on the beautiful Greek islands."},
        "India": {"capital": "New Delhi","currency": "Indian Rupee (INR)","vacation": "Visit the Taj Mahal"},
        "Indonesia": {"capital": "Jakarta","currency": "Indonesian Rupiah (IDR)","vacation": "Visit Balis beaches and temples, explore the jungles of Sumatra, and see the ancient Borobudur Temple in Yogyakarta."},
        "Ireland": {"capital": "Dublin","currency": "Euro (EUR)","vacation": "Experience the vibrant pub culture and visit historic sites like the Cliffs of Moher."},
        "Italy": {"capital": "Rome","currency": "Euro (EUR)","vacation": "Explore historical sites like the Colosseum and taste authentic Italian cuisine."},
        "Japan": {"capital": "Tokyo","currency": "Japanese Yen (JPY)","vacation": "Visit Hiroshima and Nagasaki"},
        "Jordan": {"capital": "Amman","currency": "Jordanian Dinar (JOD)","vacation": "Visit the ancient city of Petra and explore the desert landscapes of Wadi Rum."},
        "Kenya": {"capital": "Nairobi","currency": "Kenyan Shilling (KES)","vacation": "Go on a safari in the Maasai Mara and visit the Great Rift Valley."},
        "Kuwait": {"capital": "Kuwait City","currency": "Kuwaiti Dinar (KWD)","vacation": "Visit the iconic Kuwait Towers and explore the modern architecture of Kuwait City."},
        "Malaysia": {"capital": " Kuala Lumpur","currency": "Malaysian Ringgit (MYR)Euro (EUR)","vacation": "Explore the vibrant street food culture, visit the Petronas Twin Towers, and enjoy the beautiful beaches in Langkawi."},
        "Maldives": {"capital": "Mal\u00e9","currency": "Maldivian Rufiyaa (MVR)","vacation": "Relax on stunning white-sand beaches, go snorkeling or scuba diving in the crystal-clear waters, and stay in overwater bungalows in luxurious resorts."},
        "Mexico": {"capital": "Mexico City","currency": " Mexican Peso (MXN)","vacation": "Enjoy the beaches in Canc\u00fan and explore ancient Mayan ruins."},
        "Morocco": {"capital": "Rabat","currency": "Moroccan Dirham (MAD)","vacation": "Visit the medinas of Marrakech and explore the Sahara Desert."},
        "Netherlands": {"capital": "Amsterdam","currency": "Euro (EUR)","vacation": "Visit the Netherlands in April to May to see the Tulips in bloom"},
        "New Zealand": {"capital": "Wellington","currency": "New Zealand Dollar (NZD)","vacation": "Experience the natural beauty of Milford Sound and go hiking in the Southern Alps."},
        "Oman": {"capital": "Muscat","currency": "Omani Rial (OMR)","vacation": "Visit the Sultan Qaboos Grand Mosque and explore the natural beauty of Wadi Shab."},
        "Peru": {"capital": "Lima","currency": "Peruvian Nuevo Sol (PEN)","vacation": "Discover the ancient city of Machu Picchu and explore the Amazon Rainforest."},
        "Philippines": {"capital": "Manila","currency": " Philippine Peso (PHP)","vacation": "Enjoy the pristine beaches in Palawan, visit the Chocolate Hills in Bohol, and explore the historic sites in Intramuros."},
        "Qatar": {"capital": " Doha","currency": "Qatari Riyal (QAR)","vacation": "Explore the modern skyline of Doha and visit the Museum of Islamic Art."},
        "Saudi Arabia": {"capital": "Riyadh","currency": "Saudi Riyal (SAR)","vacation": "Explore the ancient city of Petra in Jordan and the historic sites of Medina."},
        "Singapore": {"capital": "Singapore","currency": "Singapore Dollar (SGD)","vacation": "Explore the city state's many parks and gardens"},
        "South Africa": {"capital": "Pretoria (Administrative), Bloemfontein (Judicial), Cape Town (Legislative)","currency": "South African Rand (ZAR)","vacation": "Go on a safari in Kruger National Park and visit Table Mountain in Cape Town."},
        "South Korea": {"capital": "Seoul","currency": "South Korean Won (KRW)","vacation": "Explore the palaces and markets in Seoul and visit the Demilitarized Zone (DMZ)."},
        "Spain": {"capital": "Madrid","currency": "Euro (EUR)","vacation": "Experience the vibrant culture of Barcelona and relax on the beaches of Costa del Sol."},
        "Sweden": {"capital": "Stockholm","currency": "Swedish Krona (SEK)","vacation": " Explore the archipelago in Stockholm and experience the Northern Lights in Lapland."},
        "Switzerland": {"capital": "Bern","currency": "Swiss Franc (CHF)","vacation": "Enjoy the Swiss Alps and explore the charming cities like Zurich and Lucerne."},
        "Syria": {"capital": "Damascus","currency": "Syrian Pound (SYP)","vacation": "Explore the historic Old City of Damascus and visit the ancient ruins of Palmyra."},
        "Thailand": {"capital": "Bangkok","currency": "Thai Baht (THB)","vacation": "Experience the vibrant street food culture and visit the temples in Chiang Mai."},
        "Tunisia": {"capital": "Tunis","currency": "Tunisian Dinar (TND)","vacation": "Explore the historic sites in Carthage and relax on the beautiful Mediterranean beaches"},
        "Turkey": {"capital": "Ankara","currency": "Turkish Lira (TRY)","vacation": "Discover the historical sites of Istanbul and explore the unique landscapes of Cappadocia."},
        "United Arab Emirates": {"capital": "Abu Dhabi","currency": "UAE Dirham (AED)","vacation": "Enjoy luxury shopping in Dubai and visit the Sheikh Zayed Grand Mosque."},
        "United Kingdom": {"capital": "London","currency": "Pound Sterling (GBP)","vacation": "Visit Stonehenge"},
        "United States": {"capital": "Washington, D.C.","currency": "United States Dollar (USD)","vacation": "Visit the Grand Canyon"}
    }
}

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "no"):
            return answer
        print("Invalid input Please try again ")

def get_valid_currency(prompt):
    while True:
        curr = input(prompt).strip().upper()
        if curr not in currency_list:
            print("Currency not valid try again.\n")
            continue
        confirm = get_yes_no(f"You selected {curr} ({currency_list[curr]}). Is that correct? : ")
        print("")
        if confirm == "yes":
            return curr

def get_valid_amount(prompt):
    while True:
        try:
            amt = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.\n")
            continue
        confirm = get_yes_no(f"You entered {amt}. Is that correct?: ")
        if confirm == "yes":
            return amt
        print("Let's try again.\n")

while True:
    print("\nWelcome to the Currency Exchange Program!\n")
    print("1.) Convert Currency")
    print("2.) Find an interesting vacation spot")
    print("3.) Quit\n")

    choice = input("Please select an option: ")

    if choice == "3":
        print("Thank you for using the Currency Converter. Goodbye!")
        sys.exit()
       
    elif choice == "1":
        base = get_valid_currency("Enter your native currency (EX: USD, CAD, EUR): ")
        target = get_valid_currency("Enter the currency you want to convert to: ")
        amount = get_valid_amount(f"How much {base} would you like to convert to {target}?: ")

        querystring = {"base": base, "target": target, "amount": amount}
        url = "https://exchange-rates7.p.rapidapi.com/convert"
        headers = {
            "x-rapidapi-key": "1fbd89b6admsh452592d91c1e41cp1ac476jsn4233e9f07bea",
            "x-rapidapi-host": "exchange-rates7.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        results = response.json()

        rate = float(results["convert_result"]["rate"])
        converted = amount * rate

        print("\n-------------------------------------------------------")
        print(f"Base Currency:   {base} ({currency_list[base]})")
        print(f"Target Currency: {target} ({currency_list[target]})")
        print(f"Conversion Rate: {rate}")
        print(f"{amount} {base} = {converted} {target}")
        print("-------------------------------------------------------\n")
       
    elif choice == "2":
        randomCountries = [random.choice(list(myDict["countries"].keys())) for _ in range(5)]
       
        while True:
            print("\nYour random countries are:")
            for i, country in enumerate(randomCountries, 1):
                print(f"{i}. {country}")

            countryChoice = input(
                "\nSelect a country by number. "
                "Type 'new' for a new set of random countries, or 'done' to exit: "
            ).strip()

            if countryChoice.lower() == "done":
                print("\nThank you for using this program.")
                break
            elif countryChoice.lower() == "new":
                randomCountries = [random.choice(list(myDict["countries"].keys())) for _ in range(5)]
                continue
            elif countryChoice.isdigit():
                idx = int(countryChoice) - 1
                if 0 <= idx < len(randomCountries):
                    country = randomCountries[idx]
                else:
                    print("Invalid number. Try again.")
                    continue
            elif countryChoice in randomCountries:
                country = countryChoice
            else:
                print("Invalid input. Please enter a valid number.")
                continue

            data = myDict["countries"][country]
            print(f"\nCountry: {country}")
            print(f"Capital: {data['capital']}")
            print(f"Currency: {data['currency']}")
            print(f"Vacation Idea: {data['vacation']}")

            capital = data['capital'].strip()
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={capital}&appid={OPENWEATHER_KEY}&units=metric"
            w = requests.get(weather_url).json()
            if "main" in w:
                temp = w["main"]["temp"]
                desc = w["weather"][0]["description"]
                if temp < 10:
                    climate = "cold"
                elif temp < 25:
                    climate = "warm"
                else:
                    climate = "hot"
                print(f"Current Weather in {capital}: {temp}°C, {desc}")
                print(f"This is considered a {climate} country right now.")
            currency_code = data["currency"].split("(")[-1].replace(")", "").strip()
            if currency_code in currency_list:
                url2 = "https://exchange-rates7.p.rapidapi.com/convert"
                headers2 = {
                    "x-rapidapi-key": "",
                    "x-rapidapi-host": "exchange-rates7.p.rapidapi.com"
                }
                q = {"base": "USD", "target": currency_code, "amount": 1}
                r = requests.get(url2, headers=headers2, params=q).json()
                rate2 = float(r["convert_result"]["rate"])
                print(f"1 USD = {rate2} {currency_code}")
