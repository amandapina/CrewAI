from crewai_tools import BaseTool
import requests
from bs4 import BeautifulSoup

class ScrapingTool(BaseTool):
    name: str = "Web Scraper Tool"
    description: str = (
        "This tool is designed to scrape relevant web pages for information "
        "about the specified topic. It will fetch a list of articles and extract key data."
    )

    def _run(self, argument: str) -> str:
        """
        Scrapes the web for relevant information about the given topic.
        This is a basic example using requests and BeautifulSoup for web scraping.
        """
        # Example URL (replace with a real URL or list of URLs to scrape)
        url = f"https://example.com/search?q={argument}"
        
        # Send a request to the website
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Example: Extract all article titles from the page (this is just a placeholder)
            articles = soup.find_all('h2', class_='article-title')  # Modify this based on the actual website's structure
            result = "\n".join([article.get_text() for article in articles])
            return f"Found the following articles related to {argument}:\n{result}"
        else:
            return f"Failed to retrieve data for topic: {argument}. Status code: {response.status_code}"
