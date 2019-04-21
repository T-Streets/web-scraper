import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.rithmschool.com/blog')
soup = BeautifulSoup(response.text, 'html.parser') 
articles = soup.find_all('article')


#open csv file to write data to
with open('blog-data.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['title', 'link', 'date'])

#extract all the titles, date, and url from the articles and write to file
    for article in articles:
        a_tag = article.find('a')
        titles = a_tag.get_text()
        url = a_tag['href']
        date = article.find('time')['datetime']
        csv_writer.writerow([titles, url, date])