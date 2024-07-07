import requests
from bs4 import BeautifulSoup
from datetime import datetime
from config_mapping import determine_lighting_configuration

class Scraper():

    # Function to fetch data from Tower website and determine today's event
    def fetch_today_event(today_date):
        
        url = "https://tower.utexas.edu/lighting-updates/"
        response = requests.get(url)
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")

        # Find all divs with class "flex flex-col pb-8"
        events = soup.find_all("div", class_="flex flex-col pb-8")

        # Iterate through events to find today's event and return description
        for event in events:
            date = event.find("p").text.strip()

            description = event.find("p", class_="flex-1").text.strip()
            
            # Convert date string to datetime object for comparison
            event_date = datetime.strptime(date, "%B %d, %Y").strftime("%Y-%m-%d")

            # Check if the event date matches today's date
            if event_date == str(today_date):
                # Determine lighting configuration based on description
                lighting_config = determine_lighting_configuration(description)
                return lighting_config
        
        # Return None if no event matches today's date
        return "None"
    


    