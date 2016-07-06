# aeroplanner
Scraper for Aeroplan/Star Alliance flights

- Very preliminary
- Hard wired to search for flights from YYZ to LHR on 2016-07-09
- Writes a file called results.json with the search results
- Requires http://scrapy.org/

Sample command:

    scrapy runspider -a member=987654321 -a pin=XXXXXXXX aeroplanner/myspider.py

Sample output:

```json
{
    "CLPlusINTLQuote": {},
    "CLPlusINTLRegular": {},
    "NormalResults": {
        "filters": {
            "aircrafts": {
                "319": "319",
                "320": "320",
                "321": "321",
                "333": "333",
                "763": "763",
                "77L": "77L",
                "77W": "77W",
                "788": "788",
                "789": "789",
                "DH3": "DH3",
                "DH4": "DH4",
                "E75": "E75",
                "E90": "E90"
            },
            "airlines": {
                "AC": "Air\u00a0Canada",
                "LH": "Lufthansa",
                "ST": "Multiple Airlines",
                "UA": "United Airlines"
            },
            "airports": {
                "EWR": "New York Newark",
                "FRA": "Frankfurt",
                "LHR": "London Heathrow",
                "ORD": "Chicago O Hare",
                "YHZ": "Halifax",
                "YOW": "Ottawa",
                "YQB": "Quebec City",
                "YUL": "Montreal Trudeau",
                "YYT": "St. John's",
                "YYZ": "Toronto Pearson"
            },
            "cabin": [
                {
                    "economy": "Economy"
                },
                {
                    "business": "Business"
                }
            ]
        },
        "product": [
            {
                "name": "classic",
                "tripComponent": [
                    {
                        "ODoption": [
                            {
                                "cabin": "E",
                                "class": "W",
                                "isIKK": false,
                                "memberMustTravel": false,
                                "mileage": 0,
                                "optionAltLogo": "",
                                "optionLogo": "AC",
                                "position": 0,
                                "regularMileage": 0,
                                "segment": [
                                    {
                                        "aircraft": "788",
                                        "airline": "AC",
                                        "arrivalDateTime": "2016-07-09T21:00:00",
                                        "bookClass": "X",
                                        "cabin": "E",
                                        "codeshareCode": "",
                                        "codeshareFlight": "",
                                        "codeshareName": "",
                                        "departureDateTime": "2016-07-09T09:05:00",
                                        "destination": "LHR",
                                        "duration": "6h 55 min",
                                        "flightNo": "AC868",
                                        "group": "W",
                                        "lagDays": "0",
                                        "meal": "Complimentary meal",
                                        "nextConnection": "0h 00 min",
                                        "origin": "YYZ",
                                        "position": 0,
                                        "product": "788",
                                        "sisterCities": false,
                                        "stop": "0"
                                    }
                                ],
                                "totalDuration": "6h 55min",
                                "totalLagDays": "0",
                                "totalMinutes": 415,
                                "totalStops": "0"
                            },
                            {
                                "cabin": "E",
                                "class": "WX",
                                "isIKK": false,
                                "memberMustTravel": false,
                                "mileage": 0,
                                "optionAltLogo": "",
                                "optionLogo": "ST",
                                "position": 1,
                                "regularMileage": 0,
                                "segment": [
                                    {
                                        "aircraft": "Embraer 190",
                                        "airline": "AC",
                                        "arrivalDateTime": "2016-07-09T09:26:00",
                                        "bookClass": "X",
                                        "cabin": "E",
                                        "codeshareCode": "",
                                        "codeshareFlight": "",
                                        "codeshareName": "",
                                        "departureDateTime": "2016-07-09T08:00:00",
                                        "destination": "EWR",
                                        "duration": "1h 26 min",
                                        "flightNo": "AC762",
                                        "group": "W",
                                        "lagDays": "0",
                                        "meal": "Meal Not available",
                                        "nextConnection": "8h 59 min",
                                        "origin": "YYZ",
                                        "position": 0,
                                        "product": "E90",
                                        "sisterCities": false,
                                        "stop": "0"
                                    },
                                    {
                                        "aircraft": "Boeing 767-300 ",
                                        "airline": "UA",
                                        "arrivalDateTime": "2016-07-10T06:45:00",
                                        "bookClass": "X",
                                        "cabin": "E",
                                        "codeshareCode": "",
                                        "codeshareFlight": "",
                                        "codeshareName": "",
                                        "departureDateTime": "2016-07-09T18:25:00",
                                        "destination": "LHR",
                                        "duration": "7h 20 min",
                                        "flightNo": "UA110",
                                        "group": "X",
                                        "lagDays": "1",
                                        "meal": "Complimentary meal",
                                        "nextConnection": "0h 00 min",
                                        "origin": "EWR",
                                        "position": 1,
                                        "product": "763",
                                        "sisterCities": false,
                                        "stop": "0"
                                    }
                                ],
                                "totalDuration": "17h 45min",
                                "totalLagDays": "1",
                                "totalMinutes": 1065,
                                "totalStops": "1"
                            },
```