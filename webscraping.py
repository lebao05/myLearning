from bs4 import BeautifulSoup
import requests
import time

def fetchSkill(job):
    skills = job.find_all('a', class_='mr-2 inline-block')
    if skills:
        for skill in skills:
            print(f"- {skill.text.strip()}")
    else:
        print("No skills listed for this job.")

def findJob():
    url = 'https://topdev.vn/it-jobs/ai-kt1555'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        all_Job = soup.find_all('li', class_='mb-4 last:mb-0')
        for job in all_Job:
            title_element = job.find('a', class_='text-lg font-bold transition-all text-primary')
            if title_element:
                titleJob = title_element.string.strip()
                print(f"Job Title: {titleJob}")
                fetchSkill(job)
            else:
                title_element_alt = job.find('a', class_='text-lg font-bold transition-all hover:text-primary')
                if title_element_alt:
                    print(f"Job Title: {title_element_alt.text.strip()}")
                    fetchSkill(job)
                else:
                    print("Job title not found.")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")

# Main loop with Ctrl+C handling
try:
    while True:
        findJob()
        print('Please wait 5 seconds before the next findJob...')
        time.sleep(5)

except KeyboardInterrupt:
    print("\nProgram stopped by user.")
