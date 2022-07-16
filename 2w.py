from bs4 import BeautifulSoup    #websraping times jobs wesite to get information about the jobs relating to certain qualities
import requests
import time
print("put a skill")
unfamiliar_skill= input(">")
print(f'filtiring out {unfamiliar_skill}')
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text ,'lxml')#this is imortant (create soup object)the same
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_dates= job.find("span",class_="sim-posted").span.text
        if "few"in published_dates:
            company_name = job.find('h3' , class_='joblist-comp-name').text.replace(' ','')#for the white space
            skills = job.find("span",class_="srp-skills").text.replace(" ","")
            more_info= job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open("posts/{index}.txt","w")as f:
                    f.write(f'''company name :{company_name.strip()}\n ''')
                    f.write(f'''Required skills: {skills.strip()}\n''')
                    f.write(f'more info:{more_info}')
                print(f'file saved:{index}')

if __name__ =="__main__":
    while True:
        find_jobs()
        time_wait=10
        print(f'waiting{time_wait}minutes...')
        time.sleep(time_wait* 60)
