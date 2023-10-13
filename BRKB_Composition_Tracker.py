import requests
from bs4 import BeautifulSoup

def getData():

    # Set up a request header to bypass scrape blockers
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'} 

    # Traget url
    url = "https://www.sec.gov/Archives/edgar/data/1067983/000095012323008074/25376.xml"

    # Send a GET request to the URL
    response = requests.get(url, headers=HEADERS)
    print(response)

    # Create a BeautifulSoup object with the response content
    soup = BeautifulSoup(response.text, "xml")

    # Find all the tags with nameOfIssuer and value
    name_of_issuer_tags = soup.find_all('nameOfIssuer')
    value_tags = soup.find_all('value')

    # Extract the text from the tags
    name_of_issuers = [tag.text for tag in name_of_issuer_tags]
    values = [int(tag.text) for tag in value_tags]
    # Test if 1:1
    print(len(name_of_issuers)==len(values))


    # Store all the holdings and the total value
    all_holdings = dict()
    total_value = 0

    for name, value in zip(name_of_issuers, values):
        if name not in all_holdings:
            all_holdings[name] = 0
        all_holdings[name] += value
        total_value +=  value

    # Store the ratio of each holding
    all_holdings_percentage = dict()
    for key, value in all_holdings.items():
        all_holdings_percentage[key] = value/total_value * 100

    #Sort all_holdings_percentage by value of dict
    all_holdings_percentage = dict(sorted(all_holdings_percentage.items(), key=lambda item: -1*item[1]))

    return all_holdings_percentage
