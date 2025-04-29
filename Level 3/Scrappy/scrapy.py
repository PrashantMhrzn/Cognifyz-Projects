import requests
from bs4 import BeautifulSoup
from datetime import date

class SimpleNewsScraper:
    def __init__(self):
        self.today = date.today().strftime("%B %d, %Y")
        self.stories = []
    
    def get_stories(self):
        try:
            # Getting the HTML
            print("Downloading Hacker News...")
            response = requests.get("https://news.ycombinator.com/")
            html = response.text
            
            # Parsing the HTML data into an object
            soup = BeautifulSoup(html, 'html.parser')
            
            # Finding all story rows
            rows = soup.find_all('tr', class_='athing')
            
            # For every row getting the data
            for row in rows:
                try:
                    # Getting title and link
                    title_tag = row.find('span', class_='titleline').find('a')
                    title = title_tag.text
                    url = title_tag['href']
                    
                    # Getting the next row which contains votes
                    next_row = row.find_next_sibling('tr')
                    vote_span = next_row.find('span', class_='score')
                    
                    if vote_span:
                        # If there is votes, then converting the votes into int, while removing 'points' to make it sole int 
                        votes = int(vote_span.text.replace(' points', ''))
                    else:
                        votes = 0
                    
                    # Adding to our stories
                    self.stories.append({
                        'title': title,
                        'url': url,
                        'votes': votes
                    })
                except Exception as e:
                    print(f"Error with one story: {e}")
                    continue
            
            # Simple sorting by votes
            for i in range(len(self.stories)):
                for j in range(i+1, len(self.stories)):
                    if self.stories[i]['votes'] < self.stories[j]['votes']:
                        temp = self.stories[i]
                        self.stories[i] = self.stories[j]
                        self.stories[j] = temp
            
            print(f"Found {len(self.stories)} stories!")
            
        except Exception as e:
            print(f"error: {e}")
    
    def show_stories(self, num=5):
        print(f"\n=== Simple Scraper News ===")
        print(f"Date: {self.today}\n")
        
        # If there are no stories 
        if not self.stories:
            print("No stories found! Maybe Hacker News changed their website?")
            return
        
        for i in range(min(num, len(self.stories))):
            story = self.stories[i]
            print(f"{i+1}. {story['title']}")
            print(f"   Votes: {story['votes']}")
            print(f"   Link: {story['url']}\n")

# Run the scraper
if __name__ == '__main__':
    print("Starting scraper...")
    scraper = SimpleNewsScraper()
    scraper.get_stories()
    scraper.show_stories(10)