from bs4 import BeautifulSoup as bs
import requests
import re

url = "http://www.orientalinsurance.org.in/web/guest/public-disclosures"
base_url = "https://orientalinsurance.org.in"
# print(url)
response = requests.get(url)
# print(response)
soup = bs(response.text, 'lxml')
# print(soup)
i = 0
year_link_list = []
full_quotes = soup.find_all("a", class_="web-content-link")[6:-1]
for year_links in full_quotes[1:-6]:
    year_link = base_url + year_links["href"]
    y_l_1=base_url+"/sign-in"
    if "2015-16" in year_link or "2017-18" in year_link:#"sign-in?" in year_link:
        continue
    print(year_link)
    # print(i)
    i += 1
    year_link_list.append(year_link)
# print(year_link_list)
# for year_link_item in year_link_list:
#     # print(year_link_item)
#     pass
# for year_link in year_link_list[2:3]:#[2:]: should change for full op
#     print(year_link)
#     year=year_link.split("year-")[1]
#     year_link_response=requests.get(year_link)
#     # print(year_link_response)
#     year_link_soup=bs(year_link_response.text,'lxml').find("table",class_="bof_border").find_all("tr")[2:]
#     # print(year_link_soup)
#     for table_row in year_link_soup:
#         q1_table_data=table_row.find_all("td")[1:2]
#         # print(q1_table_data)
#         for q1_link_tag in q1_table_data:
#             try:
#                 # print(year)
#                 q1_link=q1_link_tag.find("a")["href"]
#                 print(q1_link)
#                 nl_name=q1_link.split("/")[-2].replace(".pdf","").replace("+","-")
#                 # print(nl_name)
#                 pdf_name=year+"_"+"q1"+"_"+nl_name
#                 print(pdf_name)
#             except Exception as e:
#                 print(e)
#         q2_table_data=table_row.find_all("td")[2:3]
#         print(q2_table_data)


#         # for q2_link_tag in q2_table_data:
#         #     try:
#         #         # print(year)
#         #         q2_link=q2_link_tag.find("a")["href"]
#         #         print(q2_link)
#         #         nl_name=q2_link.split("/")[-2].replace(".pdf","").replace("+","-")
#         #         # print(nl_name)
#         #         pdf_name=year+"_"+"q2"+"_"+nl_name
#         #         print(pdf_name)
#         #     except Exception as e:
#         #         print(e)


#     # year_link_response=requests.get(year_link)
#     # # print(year_link_response)
#     # soup2=bs(year_link_response.text,'lxml')#.find("table",class_="bof_border")


#     # try:
#     #     table_data=soup2.find_all("tr")[1:]
#     #     for row in table_data:
#     #         print(row)
#     #         nl_name=row.find("td").text
#     #         print(nl_name)
#     #         next_item=bs(nl_name)
#     #         print(next_item)
#     #         print("************")
#     # except Exception as e:
#     #     print(e)
#     #     print("try another way")
#     #     pass