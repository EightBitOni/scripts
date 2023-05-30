import feedgen.feed
import requests
from bs4 import BeautifulSoup

# Fetch the web page (replace with your own URL)
web_page_url = "https://example.com/page"
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
    entry.description(item.find('p').text.strip())
    # Add any additional relevant fields as needed

# Generate the RSS feed XML
rss_feed_xml = feed.rss_str(pretty=True)

# Save the RSS feed XML to a file
with open('web_page_feed.xml', 'w') as f:
    f.write(rss_feed_xml)
