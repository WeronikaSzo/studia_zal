class SearchHotelLocators:

    search_hotel_id = "basic-location"
    search_hotel_input = "basic-location"
    location_match = "/html/body/ul/li/p"
    check_in_input = "basic-date_start"
    check_out_input = "basic-date_end"
    travellers_input_id = "basic-guest"
    person_input_xpath = "/html/body/div[2]/section[1]/div[2]/div/div/div/form/fieldset/div/div[3]/div/div/select/option[2]"
    search_button_xpath = "basic-search_button"

class SearchResultLocators:

    hotel_names_xpath = "//div[contains(@class,'details')]//h3//a"
    hotel_prices_xpath = "//div[contains(@class,'price')]//span"