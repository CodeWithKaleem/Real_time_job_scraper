import requests
from bs4 import BeautifulSoup
import time
# Fetch the data from webpage
html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_file)

# Srcape the data and gain valuable insights
soup = BeautifulSoup(html_file,'lxml')
#print(soup.prettify())

# Take the user skillset
known_skill = input("Enter your skills with comma separated:")
known_skill = known_skill.split(',')

def scrap_jobs():
    
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        date_posted = job.find('span',class_='sim-posted').text.strip()
        skills = job.find('span',class_='srp-skills').text.replace(' ','').strip().split(',')
        if 'today' in date_posted and set(known_skill) & set(skills):
                job_description = job.header.h2.a['href']
                company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','').strip()
                
        
                print(f'''
Company Name: {company_name} 
Skills Required: {skills}
Date Posted: {date_posted}
Job Description Link: {job_description}
                ''')
                print("*****************************")

if __name__ == '__main__':
    while True:
         scrap_jobs()
         print("Waiting for 5 seconds")
         time.sleep(5)
