import os, subprocess
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from git import Repo
from get_bugcrowd_scope import get_scope

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled") # bypasses webbdriver detection

driver = webdriver.Chrome(options=options)

# make list of urls from program_urls.txt
#base_url = 'https://bugcrowd.com/programs?sort[]=promoted-desc&industry[]=government'
base_url = 'https://bugcrowd.com/programs?sort[]=promoted-desc&industry[]=government&safe_harbor[]=full&search[]=collaboration%3A'


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

temp_dir_name = 'holding-cell/'

# preset data for testing, remove when using for real
output_urls = []
output_urls.append({'name': 'csb-vdp', 'link': 'https://bugcrowd.com/csb-vdp'})

# end preset data

for i in output_urls:
    exists = os.path.exists(temp_dir_name + i['name'])
    if not exists:
        Path(temp_dir_name + i['name']).mkdir( parents=True, exist_ok=True )
        #os.mkdir(temp_dir_name + i['name'])

for i in output_urls:
    path= temp_dir_name + i['name']
    exists = os.path.exists(path)
    if exists:
        os.popen('cp recon.sh ' + path)
        scope = get_scope(i['link'])
        for s in scope:
            print('scope')
            print(s)
            os.chdir(path)
            with open('wildcards', 'a+') as f:
                f.seek(0)
                if (clean_url(s) + "\n" in f.readlines()):
                    print('already exists')
                else:
                    f.write(clean_url(s) + '\n')
            os.chdir('../..')
        # run recon.sh
        os.chdir(path)
        os.popen('chmod +x recon.sh')
        new_env = os.environ.copy()
        new_env["PATH"] = os.pathsep.join(["~/go/bin",new_env["PATH"]])
        subprocess.call(['/bin/bash', '-c', './recon.sh'], env=new_env)
        os.chdir('..')