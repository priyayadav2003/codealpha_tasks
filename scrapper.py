import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webside that is used
Web_URL="https://quotes.toscrape.com/page/{}"

quotes_text =[]
name_authors =[]
tag_lists =[]

for page in range (1,4):
      URL = Web_URL.format(page)
      res = requests.get(URL)
      Soup=BeautifulSoup(res.text,"html.parser")


      Quotes = Soup.find_all("div",class_="quote")

      for q in Quotes:
            text =q.find("span",class_="text").text
            Authors = q.find("small",class_="author").text
            Tags= [tag.text for tag in q.find_all("a",class_="tag")]

            quotes_text.append(text)
            name_authors.append(Authors)
            tag_lists.append(", ".join(Tags))


for i in range (min(3,len(quotes_text))):
                  print(f"{quotes_text[i]}-{name_authors }")
                  
data = pd.DataFrame({
      "Quotations":quotes_text,
      "Authers_name":name_authors,
      "Tags_list":tag_lists

})

data.to_csv("quotations_data.csv",index=False)
print("WebScraping Completed !")

for i in range(min(3, len(quotes_text))):
    print(f"{quotes_text[i]} — {name_authors[i]}-{tag_lists[i]}")


data=pd.read_csv("quotations_data.csv")
print(data)






# import requests
# from bs4 import BeautifulSoup

# url = "http://quotes.toscrape.com"
# response = requests.get(url)

# # Step 1: Check if request succeeded
# print("Status Code:", response.status_code)  # Should be 200

# soup = BeautifulSoup(response.text, "html.parser")

# # Step 2: Find quotes and authors
# quotes_list = [q.text for q in soup.find_all("span", class_="text")]
# authors_list = [a.text for a in soup.find_all("small", class_="author")]

# # Step 3: Print counts
# print("Quotes found:", len(quotes_list))
# print("Authors found:", len(authors_list))

# # Step 4: Print first 3 quotes to see data
# for i in range(min(3, len(quotes_list))):
#     print(f"{quotes_list[i]} — {authors_list[i]}")