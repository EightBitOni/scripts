import feedgen.feed
import requests
from bs4 import BeautifulSoup

# Prompt for the URL
web_page_url = input("Enter the URL of the web page: ")

# Fetch the web page
response = requests.get(web_page_url)
html_content = response.content

# Create RSS feed object
feed = feedgen.feed.FeedGenerator()
feed.title('Web Page RSS Feed')
feed.link(href=web_page_url, rel='self')
feed.language('en')

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract relevant information and add to RSS feed
for item in soup.find_all('div', class_='post'):
    entry = feed.add_entry()
    entry.title(item.find('h2').text.strip())
    entry.link(href=item.find('a')['href'])
    
    description_paragraph = item.find('p')
    if description_paragraph:
        entry.description(description_paragraph.text.strip())
    else:
        entry.description(input("Enter a description for this entry: "))  # Prompt for description
    
    # Add any additional relevant fields as needed

    # Prompt for a description if it is still not set
    if not entry.description():
        entry.description(input("Enter a description for this entry: "))

# Generate the RSS feed XML
rss_feed_xml = feed.rss_str(pretty=True)

# Save the RSS feed XML to a file
with open('web_page_feed.xml', 'w') as f:
    f.write(rss_feed_xml)

#note: in order for this code to work you would need to install feedgen, request and beautifulsoup4
# you can do that by 'pip install (name)' in the command line