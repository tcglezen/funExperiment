from bs4 import BeautifulSoup
import requests 

#page is set to the html of the website 
page = requests.get('www.tcglezen.com/') 

#soup is a really nicer looking html version
soup = BeautifulSoup(page.content, 'html.parser')

html = list(soup.children)[2] 


