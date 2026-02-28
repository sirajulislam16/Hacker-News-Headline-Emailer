 # http requests
import requests

#web scraping
from bs4 import BeautifulSoup

#send the mail
import smtplib


#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# system date and time manipulation
import datetime
now = datetime.datetime.now()

# email content placeholder

content = ' '

# extracting Hacker News Stories
def extract_news(url):
    print("Extracting Hacker News Stories...")
    ctn = ''
    ctn += ('<b>HN Top Stories</b>\n'+'<br>'+'-'*50+'</br>')
    response = requests.get(url)
    content= response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(
        soup.find_all('td', attrs={'class':'title','valign':''})
    ):
        ctn +=((str(i+1)+' :: '+tag.text+"\n"+'<br>')if tag.text != 'More' else'')
        #print(tag.prettify) find all('span),attrs={'class':''sitestr'}
    return(ctn)
