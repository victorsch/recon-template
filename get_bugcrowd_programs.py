import os, subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from git import Repo
from get_bugcrowd_scope import get_scope

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled") # bypasses webbdriver detection

driver = webdriver.Chrome(options=options)

# make list of urls from program_urls.txt
base_url = 'https://bugcrowd.com/programs?sort[]=promoted-desc&industry[]=government'
#base_url = 'https://bugcrowd.com/programs?sort[]=promoted-desc&industry[]=government&safe_harbor[]=full&search[]=collaboration%3A'


# make request for each url
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
driver.get(base_url)
test = driver.find_elements(By.CLASS_NAME, 'cc-inline-clamp-2')

output_urls = []

for i in test:
    name = i.text
    #print(i.get_attribute('href'))
    out = {}
    out['name'] = name.replace(' ', '_')
    out['link'] = i.get_attribute('href')
    output_urls.append(out)

def clean_url(url):
    url = url.strip()
    url = url.split(' ')[0]
    if 'https://' in url:
        url = url.split('https://')[1]
    if '*.' in url:
        url = url.split('*.')[1]
    if '/' in url:
        url = url.split('/')[0]
    return url

for i in output_urls:
    #print(i['name'])
    #print(i['link'])
    # make directory if it doesn't exist with name
    # cd into directory
    # make file called wildcards
    # write i['link'] to wildcards
    # cd out of directory
    exists = os.path.exists(i['name'])
    if not exists:
        #print('making directory')
        os.mkdir(i['name'])

for i in output_urls:
    print(i)
    exists = os.path.exists(i['name'])
    print(exists)
    if exists:
        #print(i['link'])
        # copy recon.sh into dir
        os.popen('cp recon.sh ' + i['name'])
        scope = get_scope(i['link'])
        for s in scope:
            print('scope')
            print(s)
            os.chdir(i['name'])
            with open('wildcards', 'a+') as f:
                f.seek(0)
                if (clean_url(s) + "\n" in f.readlines()):
                    print('already exists')
                else:
                    f.write(clean_url(s) + '\n')
            os.chdir('..')
        # run recon.sh
        os.chdir(i['name'])
        os.popen('chmod +x recon.sh')
        new_env = os.environ.copy()
        new_env["PATH"] = os.pathsep.join(["/home/victor/go/bin",new_env["PATH"]])
        subprocess.call(['/bin/bash', '-c', './recon.sh'], env=new_env)
        os.chdir('..')
# out_urls = []
# for i in output_urls:
#     scope = get_scope(i['link'])
#     for s in scope:
#         out_urls.append(s)
#     print(scope)
# print(out_urls)