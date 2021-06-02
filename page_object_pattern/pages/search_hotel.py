import logging
from webdriver_manager import driver
from page_object_pattern.locators.locators import SearchHotelLocators


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

        self.search_hotel_id = SearchHotelLocators.search_hotel_id
        self.search_hotel_input = SearchHotelLocators.search_hotel_input
        self.location_match = SearchHotelLocators.location_match
        self.check_in_input = SearchHotelLocators.check_in_input
        self.check_out_input = SearchHotelLocators.check_out_input
        self.travellers_input_id = SearchHotelLocators.travellers_input_id
        self.person_input_xpath = SearchHotelLocators.person_input_xpath
        self.search_button_xpath = SearchHotelLocators.search_button_xpath

    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element_by_id(self.search_hotel_id).click()
        self.driver.find_element_by_id(self.search_hotel_input).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match).click()

    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting check in {checkin} and {checkout} dates".format(checkin=check_in, checkout =check_out))
        self.driver.find_element_by_id(self.check_in_input).send_keys(check_in)
        self.driver.find_element_by_id(self.check_out_input).send_keys(check_out)

    def set_travellers(self, person):
        self.logger.info("Setting travellers {people}".format(person=person))
        self.driver.find_element_by_id(self.travellers_input_id).click()
        self.driver.find_element_by_xpath(self.person_input_xpath).click()

    def perform_search(self):
        self.logger.info("Performing search")
        self.driver = driver.find_element_by_id(self.search_button_xpath).click()





