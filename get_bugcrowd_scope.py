import requests
import bs4, time
# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def initialize():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled") # bypasses webbdriver detection

    driver = webdriver.Chrome(options=options)
    return driver
# #make list of urls from program_urls.txt
# driver = initialize()
# urls = []
# with open('program_urls.txt', 'r') as f:
#     urls = f.readlines()

# # remove whitespace characters like `\n` at the end of each line
# urls = [x.strip() for x in urls]

# # make request for each url
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# for url in urls:
#     driver.get(url.split(' ')[0])
#     test = driver.find_elements(By.CLASS_NAME, 'cc-rewards-link-table__endpoint')
#     for i in test:
#         print(i.text)

def get_scope(program_url):
    program_url = program_url.strip()
    driver = initialize()
    #print(program_url)


    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    driver.get(program_url)
    test = driver.find_elements(By.CLASS_NAME, 'cc-rewards-link-table__endpoint')
    out_urls = []

    for i in test:
        #print(i.text)
        out_urls.append(i.text)
    return out_urls


#print(get_scope('https://bugcrowd.com/iaf-vdp'))









# #r = requests.get(url, headers=headers)
# # make html session
# session = HTMLSession()
# r = session.get(url)
# # render the page
# links = r.html.links
# #print(links)
# r.html.render(timeout=20)

# test = r.html.full_text
# print(test)


# # write r.text to a file
# with open('bugcrowd_scope.html', 'w') as f:
#     f.write(r.text)


# # the scope urls are in the table with class tk-target-table
# #soup = bs4.BeautifulSoup(r.html, 'html.parser')
# #mainPanel = soup.find('div',attrs={'class':'bc-panel__main'})
# #scopeTable = mainPanel.find('table',attrs={'class':'bc-table'})
# #print(mainPanel)
# #print(scopeTable)
# # get the value of a link in a <code> tag with the class cc-rewards-link-table__endpoint
# #codeTag = soup.findAll('code',attrs={'class':'cc-rewards-link-table__endpoint'})
# #print(codeTag)
# #print(scope.text)