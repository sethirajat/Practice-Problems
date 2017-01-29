import urllib
from bs4 import BeautifulSoup, SoupStrainer
import re
import urlparse
import httplib2
import requests
HEADER = "http://"
def check_url(url):

    if len(url) < 1:
        raise ValueError("incorrect url")
    if not url.startswith("http"):
        url += HEADER

    resp = requests.head(url)
    if resp.status_code > 400:
        print "URlerror: "
        print resp.text, resp.headers
        return False,url

    return True,url

def read_input(url):
    http = httplib2.Http()
    status, response = http.request(url)

    return response



def get_links(content, output):
    output_file = open(output,'a')
    output_file.write("[links]\n")
    for link in BeautifulSoup(content, parseOnlyThese=SoupStrainer('a')):
        if link.has_attr('href'):
            output_file.write(link['href'] + "\n")


    output_file.close()

def clean(content):
    regex = r"\w+=\".*\""
    result = re.sub(regex, '', content, 0)
    return result




def get_tags(content,output):

    output_file = open(output, 'a')
    soup = BeautifulSoup(content)
    clear_soup = clean(str(soup))
    matches = re.finditer(r"<(/)?(\w+)\b[^>/]*(/)?>", clear_soup)
    output_file.write("[tags]\n")
    tags_str = ''

    for matchNum, match in enumerate(matches):
        found = match.groups()
        if found[0] == '/':
            tags_str += '</' + found[1] + '>'
        elif found[2] == '/':
            tags_str += '<' + found[1] + '/>'
        else:
            tags_str += '<' + found[1] + '>'

    output_file.write(tags_str + "\n")
    output_file.close()


def get_sequences(content, output):

    output_file = open(output, 'a')
    soup = BeautifulSoup(content)
    #pattern = re.compile("([A-Z][\w-]*(\s+[A-Z][\w-]*)+)")
    #pattern = re.compile("([A-Z][a-zA-Z0-9-]*)([\s][A-Z][a-zA-Z0-9-]*)+")
    pattern = re.compile("([A-Z][a-zA-Z0-9-]*([\s][A-Z][a-zA-Z0-9-]*)+)")
    #print soup.text
    #strl = "Rajat\n\n\n\n\n\n\n\n Sethi is a good boy For Sure Bro"
    matches = re.findall(pattern, soup.text)
    #matches = re.findall(pattern, strl)
    output_file.write("[sequence]\n")
    for match in matches:
        if len(match) > 1:
            output_file.write(match[0] + "\n")

    output_file.close()


def main(url,output):
    url_ok, newurl = check_url(url)
    if url_ok:
        content = read_input(newurl)
        get_links(content,output)
        get_tags(content,output)
        get_sequences(content,output)
    else:
        raise ValueError("incorrect url")


if __name__ == '__main__':

    url = 'http://www.nytimes.com'
    output = "kush2.txt"

    main(url,output)

    str1 = "rajatsethi"
    




