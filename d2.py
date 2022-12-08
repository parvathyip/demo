from  bs4 import BeautifulSoup as bs
import requests
import re

url = "http://www.orientalinsurance.org.in/web/guest/public-disclosures"
base_url = "https://orientalinsurance.org.in"
# print(url)
response = requests.get(url)
# print(response)
soup = bs(response.text, 'lxml')

full_quotes = soup.find_all("a", class_="web-content-link")[6:-1]
for year_links in full_quotes[1:-6]:
    year_link = base_url + year_links["href"]
    print(year_link)
    response2 = requests.get(year_link)
    # print(response2)
    year_link_soup = bs(response2.text, 'lxml').find("table", class_="bof_border")
    if year_link_soup:
        print("yes")
        contents=year_link_soup.find_all("tr")[1:]

        for content_data in contents:
            content_tag_list=content_data.find_all("td")
            c = 1
            for content_tag in content_tag_list:
                if "NL" in content_tag.text:
                    nl_name=content_tag.text.split("-")[0]+"-"+content_tag.text.split("-")[1]
                    print(nl_name)

                # if content_tag.find("a"):
                #     print(content_tag,c)
                #     c+=1
            print("#################")
            # print(content.text)


