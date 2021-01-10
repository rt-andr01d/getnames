import requests 
import bs4 
import os
import re

url = 'https://google.com/search?q=site:linkedin.com%20"RSM US LLP"&num=100'
    
request_result=requests.get( url ) 
     
soup = bs4.BeautifulSoup(request_result.text, 
                                       "html.parser") 

print(soup, file=open("out.txt", "a"))

os.system("egrep -o -E '[[:alnum:]]{3,7} [[:alnum:]]{3,7} -' out.txt > names.txt")

os.remove("out.txt")
