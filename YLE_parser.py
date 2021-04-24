from bs4 import BeautifulSoup
import json

top_stories="mostRead"
latest_stories="tuoreimmat"

def remove_hyphens(text):
    return text.replace("­", "")

def parse_webpage(data):
    print("web page ready for parsing!")
    most_read_unparsed = None
    parsed_news_data = []
    yle_url = "https://yle.fi"
    init_parse = BeautifulSoup(data, 'html.parser')
    side_bar = init_parse.find("div", {"class":"yle__app"})
    for x in side_bar.find_all("ol"):
        if(x.get('data-test-key') == latest_stories):
           most_read_unparsed = x

    for x in most_read_unparsed.find_all("a"):
        final_url = None
        content = None
        if x.get('data-test-key') == "headline":
            final_url = yle_url + x.get("href")
        content = x.find("h6")
        news_obj = json.dumps({"msg":remove_hyphens(content.text), "url":final_url, "sub_id":3})
        parsed_news_data.append(news_obj)

    return parsed_news_data



