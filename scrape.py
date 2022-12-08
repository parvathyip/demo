# from bs4 import BeautifulSoup as bs
# import requests
# import re
# url="https://www.royalsundaram.in/about-us/public-disclosures"
# base_url="https://www.royalsundaram.in"
# # print(url)
# response=requests.get(url)
# # print(response)
# soup=bs(response.text,'lxml').find_all("div",class_="panel-group")[0].find_all("div",class_="panel")
# # print(len(soup))
# for year_links in soup:
#     year_link=year_links.find("div",class_="panel-collapse").find_all("a")
#     # print(year_link)
#     for link in year_link:
#         link_href=base_url+link["href"]
#         print(link_href)
#         year_text_list=link_href.split("/")[-1].split("of-")[-1].split("-")[0:2]
#         year_text=year_text_list[0]+"-"+year_text_list[1]
#         if year_text=="disclosure-2018":
#             year_text="2018-2019"
#         elif year_text=="disclosure-2017":
#             year_text="2017-2018"
#         elif year_text=="disclosure-2020":
#             year_text="2020-2021"
#         elif year_text=="disclosure-2016":
#             year_text="2016-2017"
#         elif year_text=="disclosure-2015":
#             year_text="2015-2016"
#         elif year_text == "disclosure-2014":
#             year_text = "2014-2015"
#         elif year_text=="disclosure-2013":
#             year_text="2013-2014"
#         elif year_text=="disclosure-2012":
#             year_text="2012-2013"
#         elif year_text=="disclosure-2011":
#             year_text="2011-2012"
#         elif year_text == "disclosure-2010":
#             year_text = "2010-2011"
#         elif year_text == "disclosure-2009":
#             year_text = "2009-2010"
#         elif year_text == "disclosure-2008":
#             year_text = "2008-2009"
#         elif year_text == "disclosure-2007":
#             year_text = "2007-2008"
#         elif year_text == "disclosure-2006":
#             year_text = "2006-2007"
#         elif year_text == "disclosure-2005":
#             year_text = "2005-2006"
#         response = requests.get(link_href)
#         # print(response)
#         soup2 = bs(response.text, 'lxml').find("table")
#         # print((soup2))
#         link_text=link.text
#         if "1st Quarter" in link_text:
#             link_text="Q1"
#         elif "1st Half" in link_text:
#             link_text="Q2"
#         elif "3rd Quarter" in link_text or "3rd-quarter" in link_text:
#             link_text="Q3"
#         elif "Annual" in link_text:
#             link_text="Q4"
#         print((link_text))
#         print(year_text)
#     print("########")


from bs4 import BeautifulSoup as bs
import requests
import re

url = "https://www.godigit.com/financials"
base_url = "https://www.godigit.com"
# print(url)
response = requests.get(url)
# print(response)
soup = bs(response.text, 'lxml').find_all("div", class_="row eqHeight investors-info-cards-row")[0].find_all("div",
                                                                                                             class_="col-xs-6 col-md-4 investors-info-card-col financial-info")
# print(soup)
for year_links in soup[0:-2]:  ####remove -3
    year_link = url + year_links.find("a")["href"]
    print(year_link)
    if year_link=="https://www.godigit.com/financials#modal-quarter-info":
        year="2017-18"
    else:
        year=year_link.split("info-")[1]
    print(year)
    print("*************")
    link_response = requests.get(year_link)
    # print(link_response)
    soup2 = bs(link_response.text, "lxml").find_all("div", class_="col-ssm-12 col-xs-6 col-md-4 pad-bt-15")
    # print(soup2)
    # for a_tags in soup2:
    #     # a_tag = a_tags.find("a")
    #     # print(a_tag)
    #     try:
    #         # print(year_link)
    #         a_tag = a_tags.find("a")["href"]
    #         a_tag = a_tag.replace(" ", "").replace("(", "").replace(")", "").replace("'", "")
    #         # print(a_tag)
    #         if a_tag.startswith("/"):
    #             pdf_link = base_url + a_tag
    #             # print(link)
    #         else:
    #             pdf_link = a_tag
    #             # print(pdf_link)
    #
    #         if "q1" in a_tag or "Q1" in a_tag:
    #             q_name = "q1"
    #         elif "q2" in a_tag or "Q2" in a_tag:
    #             q_name = "q2"
    #         elif "q3" in a_tag or "Q3" in a_tag:
    #             q_name = "q3"
    #         elif "q4" in a_tag or "Q4" in a_tag:
    #             q_name = "q4"
            # print(q_name)
            # if q_name not in pdf_link:
            #     pdf_link=""
            #     # print("errrrrrrrr", pdf_link)
            # print(pdf_link)
            # n_name=a_tags.find("h5").text.replace(" ","-")
            # print(n_name)
            # # print(year_link)
            # print("**********")
        # except Exception as e:
        #     print(e)
        #     a_tag = ""

# 2020-2021_q1-nl1.pdf


# from bs4 import BeautifulSoup as bs
# import requests
# import re
# import json
# url="https://www.tataaig.com/publicDisclosure"
# base_url="https://www.royalsundaram.in"
# response=requests.get(url)
# # print(response.text)
# # soup=bs(response.content,'lxml')#.find("body").find("div",{"id":"__next"}).find("main").find("div",class_="container-fluid").find("div",class_="container borderBottom pb-5").find("table")
# # print((soup))
# soup=bs(response.content,'lxml').find("script",{"id":"__NEXT_DATA__"}).text#.find("body").find("div",{"id":"__next"}).find("main").find("div",class_="container-fluid").find("div",class_="container borderBottom pb-5").find("table")
# # soup=str(soup).replace("</script>","")
# data = json.dumps(soup)
# # print((soup))
# print(data)
#
# # pdf_response=requests.get(url)
# # pdf = open("21_html.html", 'wb')
# # pdf.write(pdf_response.content)
# # pdf.close()
# # soup=bs(pdf_response.content,'lxml').find("body").find("div",{"id":"__next"}).find("main").find("div",class_="container-fluid").find("div",class_="container borderBottom pb-5").find("table")
# # print((soup))
