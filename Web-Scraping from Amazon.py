### WEB-SCRAPING FROM AMAZON ###


#Importing the Libraries that we gonna use
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


#Requesting to get the Amazon URL and saving it has response 
response = request.get("https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A976419031%2Cp_89%3AApple&dc&ds=v1%3AVykN3ePeKgAkQxfea9rZYOxtIdS%2Bg3JznS82Av2dbLM&qid=1713340541&ref=sr_ex_n_1")
response


#Displaying all the Content from the given URL
response.content


#Displaying all the content from the URL in HTML
soup = bs(response.content,"html.parser")
soup


#Display all the Appple phones from the Amazon names
phones = soup.find_all("span", {"class":"a-size-base-plus a-color-base a-text-normal"})
phones

#Print all the Phone names in a list
phones_name = [i.text for i in phones]
phones_name


#Display all the Appple phones prices from the Amazon 
price = soup.find_all("span", {class="a-price-whole"})
price


##Print all the Phone names in a list
price_of_phones = [i.text for i in price]
price_of_phones

#Display the both phones_name and price_of_phones
display(phones_name, price_of_phones)


#Saving this information in a variable called data
data = {"Apple Phones": phones_name,"Apple_phones_price" : price_of_phones}
data


#Now we gonna use pandas to view in a data frame
df = pd.DataFrame(data)
df


#You can save this information in any format you want csv,xlsx,json etc..
df.to_csv("Amazon_Apple_Phones.csv")
