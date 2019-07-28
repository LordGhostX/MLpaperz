# Responsible for scraping & parsing the latest and trending research papers

from requests import get
from bs4 import BeautifulSoup as Soup

# Get the latest research papers
def get_latest(limit=None):
    papers = get_papers("https://paperswithcode.com/latest", limit)
    return papers

# Get the trending research papers
def get_trending(limit=None):
    papers = get_papers("https://paperswithcode.com", limit)
    return papers

# Get Research Papers
def get_papers(url, limit=None):
    # The limit input parameter is used to set a limit to the amount of papers returned
    r = get(url)
    try:
        soup = Soup(r.text, features="html5lib")
    except:
        soup = Soup(r.text)

    # The div element with the class infinite-item is where all the papers are located
    papers = []
    for _ in soup.find_all("div", {"class": "infinite-item"}):
        # Save the link to each of our papers
        paper_url = _.find("a")["href"]
        # Sometimes paper urls can be github links especially trending research so we are not going to include them because they lead to issues in the scraping
        if paper_url[0] == "/":
            papers.append("https://paperswithcode.com" + paper_url)

    if limit:
        return papers[:limit]
    return papers

# Parse paper urls and make it in a more structured format
def parse_papers(papers, tag):
    parsed_papers = []

    for paper in papers:
        # Scrape the paper link and start formatting
        r = get(paper)
        try:
            soup = Soup(r.text, features="html5lib")
        except:
            soup = Soup(r.text)

        # Paper Header
        paper_header = soup.find("div", {"class": "paper-title"})
        paper_title = paper_header.find("h1").text

        # Paper Abstract
        paper_abstract = soup.find("div", {"class": "paper-abstract"})
        abstract_text = paper_abstract.find("p").text.replace("(read more)\n", "").strip() # Removes "read more" text in paper abstract
        abstract_links = paper_abstract.find_all("a")[1:]
        abstract_link_1 = abstract_links[0].text.strip() + " - " + abstract_links[0]["href"]
        abstract_link_2 = abstract_links[1].text.strip() + " - " + abstract_links[1]["href"]

        # Paper Code Implementation
        paper_code = soup.find("a", {"class": "code-table-link"})["href"]

        parsed_papers.append({"url": paper, "title": paper_title, "abstract": abstract_text, "abstract link 1": abstract_link_1, "abstract link 2": abstract_link_2, "code": paper_code, "tag": tag})

    return parsed_papers
