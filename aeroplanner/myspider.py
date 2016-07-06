import codecs
import logging
import scrapy
from scrapy.http.request.form import FormRequest
from scrapy.shell import inspect_response

class BlogSpider(scrapy.Spider):
    name = 'aeroplanner'
    # Start with the login page; we need to navigate a couple of intermediate
    # pages before we get to the good stuff.
    start_urls = ['https://www4.aeroplan.com/log_in.do']
    
    def __init__(self, member='', pin=''):
        if not id:
            self.log("No member id specified; use -a id=123456789")
        if not pin:
            self.log("No pin (password) specified; use -a pin=passwrod")
        if not id or not pin:
            raise Exception("Missing required arguments")
        self.member = member
        self.pin = pin

    def parse(self, response):
        self.log("Parsing", level=logging.INFO)
        
        if response.xpath('//form[@id="loginForm"]'):
            self.log("Found login form", level=logging.INFO)
            yield FormRequest.from_response(response,
                formid='loginForm',
                formdata={'cust': self.member,
                          'pin': self.pin,
                          'rToken': 'null',
                },
                callback=self.after_login)

        self.log("Done parsing main page", logging.INFO)

    def after_login(self, response):
        # TODO: check login succeed before going on
        self.log("After login", logging.INFO)
        
        # jump to the bookings page and select English
        yield scrapy.Request(
            response.urljoin('/adr/AirBooking.do?icid=SUB_M_Travel_EN&lang=E'),
            callback = self.parse_search_page)

    def parse_search_page(self, response):
        self.log("English selected", logging.INFO)
        
#         with codecs.open('index.html', 'w', 'utf-8') as f:
#             f.write(response.text) 

#         inspect_response(response, self)

        # extract some info about the user
        user_name = response.xpath('//span[@class="header-name"]/text()').extract_first()
        user_number = response.xpath('//span[@class="header-number"]/text()').extract_first()
        user_mileage = response.xpath('//span[@class="header-mileage"]/text()').extract_first()
        self.log("name=" + user_name, logging.INFO)
        self.log("number=" + user_number, logging.INFO)
        self.log("mileage=" + user_mileage, logging.INFO)

        # submit search form to /adr/SearchProcess.do; this will redirect
        # to /adr/Results.do, which is responsible for displaying the progress
        # bar
        yield FormRequest.from_response(response,
                formxpath='//form[@name="onewayTravel"]',
                formdata={
                          'currentTripTab': 'oneway',
                          'modifySearch': 'false',
                          'forceIkk': 'false',
                          'city1FromOneway': 'YYZ',
                          'city1FromOnewayCode': 'YYZ', 
                          'city1ToOneway': 'LHR',
                          'city1ToOnewayCode': 'LHR',
                          'l1Oneway': '2016-07-09',
                          'l1OnewayDate': '2016-07-09',
                          'OnewayFlexibleDatesHidden': '0',
                          'OnewayAdultsNb': '1',
                          'OnewayChildrenNb': '0',
                          'OnewayTotalPassengerNb': '1',
                          'OnewayCabin': 'Business',
                },
                callback=self.parse_results_do
            )

    def parse_results_do(self, response):
        self.log("Search in progress " + str(response), logging.INFO)

#         with codecs.open('results.html', 'w+', 'utf-8') as f:
#             f.write(response.text)

        # The search is now stored in cookies. POST an empty request to 
        # Results_Ajax to really perform the search. 
        yield scrapy.Request(
                response.urljoin('/adr/Results_Ajax.jsp?searchType=oneway&forceIkk=false'),
                method = 'POST',
                callback=self.parse_ajax)
        
    def parse_ajax(self, response):
#         inspect_response(response, self)

        with codecs.open('results.json', 'w+', 'utf-8') as f:
            f.write(response.text)

