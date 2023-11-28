import requests
import csv
from bs4 import BeautifulSoup

def scrape_market_trends():
# Goey team we can replace with the actual URL of the market trends page
    url = "https://example.com/market-trends" 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    market_trends_data = [] 
#  Initialize an empty list to store the market trend data

    # Extract the market trend data from the HTML and append it to the list
    # Example:
    # market_trends_data.append("Market Trend 1")
    # market_trends_data.append("Market Trend 2")

    
    # Return the market trend data
    return market_trends_data

# Function to scrape domains
# Goey team we can replace with the actual URL of the domains page
def scrape_domains():
    url = "https://example.com/domains"  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    trends = soup.find_all('div', class_='trend')

    # Extract the market trend data from the HTML and append it to the list
    market_trends_data = []  # Initialize an empty list to store the market trend data
    for trend in trends:
        market_trends_data.append(trend.text)

    # TODO: Extract the domain data from the HTML using BeautifulSoup
    domain_data = []  # Initialize an empty list to store the domain data
    # END: ed8c6549bwf9

# Extract the domain data from the HTML and append it to the list
# Example:
# domain_data.append("Domain 1")
# domain_data.append("Domain 2")

# Return the domain data
def scrape_domains():
    url = "https://example.com/domains"  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    trends = soup.find_all('div', class_='trend')

    domain_data = []  # Initialize an empty list to store the domain data

    # Extract the domain data from the HTML and append it to the list
    for trend in trends:
        domain_data.append(trend.text)

    # Return the domain data
    return domain_data

# Main function
def main():
    # Scrape market trends
    market_trends_data = scrape_market_trends()
    
    # Scrape domains
    domain_data = scrape_domains()
    
    # Save the data to a CSV file
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the market trend data to the CSV file
        writer.writerow(['Market Trend'])
        for trend in market_trends_data:
            writer.writerow([trend])
        
        # Write the domain data to the CSV file
        writer.writerow(['Domain'])
        for domain in domain_data:
            writer.writerow([domain])

# Run the main function
if __name__ == "__main__":
    main()
