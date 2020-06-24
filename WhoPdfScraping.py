from bs4 import BeautifulSoup
import urllib.request

# World Health Organization - COVID PDFs Page
html_page = urllib.request.urlopen("https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports").read()
soup = BeautifulSoup(html_page, features="lxml")


pdf_url_list = []
# Get all <a> elements from page
for link in soup.find_all('a'):
    element_link = link.get('href')
    # Check if href attribute contains pdf (only pdf links)
    if "pdf" in element_link:
        print(link.get('href'))
        # Check if the pdf link is unique in the list ( avoiding duplicates )
        if element_link not in pdf_url_list:
            pdf_url_list.append(element_link)


# Returns a list with all COVID PDF urls
print(len(pdf_url_list))
# pdf_url_list