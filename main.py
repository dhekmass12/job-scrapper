from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import psycopg2
import time
import psycopg2.sql
import os

def is_published_date_good(published_date):
    published_date = published_date.split()
    if published_date[1].lower() == "januari":
        published_date[1] = "01"
    elif published_date[1].lower() == "februari":
        published_date[1] = "02"
    elif published_date[1].lower() == "maret":
        published_date[1] = "03"
    elif published_date[1].lower() == "april":
        published_date[1] = "04"
    elif published_date[1].lower() == "mei":
        published_date[1] = "05"
    elif published_date[1].lower() == "juni":
        published_date[1] = "06"
    elif published_date[1].lower() == "Juli":
        published_date[1] = "07"
    elif published_date[1].lower() == "agustus":
        published_date[1] = "08"
    elif published_date[1].lower() == "september":
        published_date[1] = "09"
    elif published_date[1].lower() == "oktober":
        published_date[1] = "10"
    elif published_date[1].lower() == "november":
        published_date[1] = "11"
    elif published_date[1].lower() == "desember":
        published_date[1] = "12"
    day = int(published_date[0])
    month = int(published_date[1])
    year = int(published_date[2])
    a = datetime.datetime.now()
    
    if a.year - year >= 2:
        return False
    elif abs(a.month - month) <= 2:
        return True
    else:
        return False
    
def get_published_date(published_date):
    published_date = published_date.split()
    if published_date[1].lower() == "januari":
        published_date[1] = "01"
    elif published_date[1].lower() == "februari":
        published_date[1] = "02"
    elif published_date[1].lower() == "maret":
        published_date[1] = "03"
    elif published_date[1].lower() == "april":
        published_date[1] = "04"
    elif published_date[1].lower() == "mei":
        published_date[1] = "05"
    elif published_date[1].lower() == "juni":
        published_date[1] = "06"
    elif published_date[1].lower() == "Juli":
        published_date[1] = "07"
    elif published_date[1].lower() == "agustus":
        published_date[1] = "08"
    elif published_date[1].lower() == "september":
        published_date[1] = "09"
    elif published_date[1].lower() == "oktober":
        published_date[1] = "10"
    elif published_date[1].lower() == "november":
        published_date[1] = "11"
    elif published_date[1].lower() == "desember":
        published_date[1] = "12"
    day = published_date[0]
    month = published_date[1]
    year = published_date[2]
    return day + "-" + month + "-" + year

def is_published_date_good2(published_date):
    published_date = published_date.split()

    number = int(published_date[0])
    unit = published_date[1]

    if unit.lower() == "detik" or unit.lower() == "menit" or unit.lower() == "jam" or unit.lower() == "hari" or unit.lower() == "minggu":
        return True
    elif unit.lower() == "bulan":
        if number <= 2:
            return True
        else:
            return False
    else:
        return False
    
def get_published_date2(published_date):
    published_date = published_date.split()
    number = int(published_date[0])
    unit = published_date[1]
    
    if unit.lower() == "detik" or unit.lower() == "menit" or unit.lower() == "jam":
        return datetime.datetime.now().strftime("%d-%m-%Y")
    elif unit.lower() == "hari":
        return (datetime.datetime.now() + datetime.timedelta(days=-number)).strftime("%d-%m-%Y")
    elif unit.lower() == "minggu":
        return (datetime.datetime.now() + datetime.timedelta(days=-number*7)).strftime("%d-%m-%Y")
    elif unit.lower() == "bulan":
        return (datetime.datetime.now() + datetime.timedelta(days=-number*30)).strftime("%d-%m-%Y")

def is_published_date_good3(published_date):
    published_date = published_date.split()
    unit = published_date[2]

    if (unit.lower() == "second" or unit.lower() == "seconds" or
        unit.lower() == "minute" or unit.lower() == "minutes" or
        unit.lower() == "hour" or unit.lower() == "hours" or
        unit.lower() == "day" or unit.lower() == "days" or
        unit.lower() == "week" or unit.lower() == "weeks"):
        return True
    elif unit.lower() == "month":
        return True
    elif unit.lower() == "months":
        number = int(published_date[1])
        if number <= 2:
            return True
        else:
            return False
    else:
        return False
    
def get_published_date3(published_date):
    published_date = published_date.split()
    unit = published_date[2]
    number = 1
    
    if (unit.lower() == "second" or unit.lower() == "seconds" or
        unit.lower() == "minute" or unit.lower() == "minutes" or
        unit.lower() == "hour" or unit.lower() == "hours"):
        return datetime.datetime.now().strftime("%d-%m-%Y")
    elif unit.lower() == "day":
        return (datetime.datetime.now() + datetime.timedelta(days=-number)).strftime("%d-%m-%Y")
    elif unit.lower() == "days":
        number = int(published_date[1])
        return (datetime.datetime.now() + datetime.timedelta(days=-number)).strftime("%d-%m-%Y")
    elif unit.lower() == "week":
        return (datetime.datetime.now() + datetime.timedelta(days=-number*7)).strftime("%d-%m-%Y")
    elif unit.lower() == "weeks":
        number = int(published_date[1])
        return (datetime.datetime.now() + datetime.timedelta(days=-number*7)).strftime("%d-%m-%Y")
    elif unit.lower() == "month":
        return (datetime.datetime.now() + datetime.timedelta(days=-number*30)).strftime("%d-%m-%Y")
    elif unit.lower() == "months":
        number = int(published_date[1])
        return (datetime.datetime.now() + datetime.timedelta(days=-number*30)).strftime("%d-%m-%Y")

def is_published_date_good4(published_date):
    published_date = published_date.split()
    if published_date[0].isnumeric():
        number = int(published_date[0])
        unit = published_date[1]
    elif published_date[1]:
        number = int(published_date[1])
        unit = published_date[2]

    if unit.lower() == "day" or unit.lower() == "days" or unit.lower() == "week" or unit.lower() == "weeks":
        return True
    elif unit.lower() == "month" or unit.lower() == "months":
        if number <= 2:
            return True
        else:
            return False
    else:
        return False
    
def get_published_date4(published_date):
    published_date = published_date.split()
    if published_date[0].isnumeric():
        number = int(published_date[0])
        unit = published_date[1]
    elif published_date[1]:
        number = int(published_date[1])
        unit = published_date[2]
    
    if (unit.lower() == "second" or unit.lower() == "seconds" or
        unit.lower() == "minute" or unit.lower() == "minutes" or
        unit.lower() == "hour" or unit.lower() == "hours"):
        return datetime.datetime.now().strftime("%d-%m-%Y")
    elif unit.lower() == "day" or unit.lower() == "days":
        return (datetime.datetime.now() + datetime.timedelta(days=-number)).strftime("%d-%m-%Y")
    elif unit.lower() == "week" or unit.lower() == "weeks":
        return (datetime.datetime.now() + datetime.timedelta(days=-number*7)).strftime("%d-%m-%Y")
    elif unit.lower() == "month" or unit.lower() == "months":
        return (datetime.datetime.now() + datetime.timedelta(days=-number*30)).strftime("%d-%m-%Y")

def scrap_jobs_from_karir(job_field):
    url = "https://karir.com/search-lowongan?keyword={}".format(job_field)
    driver = webdriver.Chrome()
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    titles = soup.find_all("p", attrs={"class":"MuiTypography-root MuiTypography-body1 text-ellipsis css-au5tz6", "type":"Heading4"})
    companies = soup.find_all("p", attrs={"class":"MuiTypography-root MuiTypography-body1 css-rd4nzp"})
    locations = soup.find_all("p", attrs={"class":"MuiTypography-root MuiTypography-body1 css-xl10kd"})
    published_dates = soup.find_all("p", attrs={"class":"MuiTypography-root MuiTypography-body1 css-1cyztla"})
    result= []
    for i in range(len(titles)):
        job = {"title": '', "company": '', "location": "", "published_date": "", "source": "", "link": "", "job_field": ""}
        job["published_date"] = published_dates[i].string
        if not is_published_date_good(job["published_date"]):
            continue
        
        job["published_date"] = get_published_date(job["published_date"])
        job["title"] = titles[i].string
        job["company"] = companies[i].string
        job["location"] = locations[i].string
        job["source"] = "Karir.com"
        job["job_field"] = job_field
        result.append(job)

    return result

def scrap_jobs_from_jobstreet(job_field):
    try:
        url = "https://www.jobstreet.co.id/id/{}-jobs".format(job_field)
        driver = webdriver.Chrome()
        driver.get(url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        jobs = soup.find_all("article", attrs={"data-automation":"normalJob"})
        
        result= []
        for job in jobs:
            try:
                info = {"title": '', "company": '', "location": "", "link": "", "source": "", "published_date": "", "job_field": ""}
                info["published_date"] = job.find("span", attrs={"data-automation":"jobListingDate"}).string
                if not is_published_date_good2(info["published_date"]):
                    continue
                info["title"] = job.find("a", attrs={"data-automation":"jobTitle"}).string
                info["company"] = job.find("a", attrs={"data-automation":"jobCompany"})
                if (info["company"] is None):
                    info["company"] = "Pengiklan Anonim"
                else:
                    info["company"] = info["company"].string
                locations = job.find_all("a", attrs={"data-automation": "jobLocation"})
                for location in locations:
                    info["location"] = info["location"] + location.string + ", "
                info["published_date"] = get_published_date2(info["published_date"])
                info["source"] = "jobstreet.co.id"
                info["link"] = job.find("a", attrs={"data-automation":"job-list-view-job-link"})["href"]
                info["job_field"] = job_field
                result.append(info)
            except Exception:
                continue
        return result
    except:
        return []

def scrap_jobs_from_kalibrr(job_field):
    try:
        url = "https://www.kalibrr.com/home/te/{}".format(job_field)
        driver = webdriver.Chrome()
        driver.get(url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        links = soup.find_all("a", attrs={"class":"k-w-36 k-text-center k-btn-primary k-bg-white k-text-primary-color", "itemprop":"name"})

        result= []
        for i in range(len(links)):
            try:
                links[i] = "https://www.kalibrr.com" + links[i]["href"]
                driver = webdriver.Chrome()
                driver.get(links[i])
                page_source = driver.page_source
                soup = BeautifulSoup(page_source, 'html.parser')

                job = {"title": '', "company": '', "location": "", "link": "", "source": "", "published_date": "", "job_field": ""}
                job["title"] = soup.find("h1", attrs={"itemprop":"title"}).get_text().replace("\xa0", "")
                print(soup.find("h1", attrs={"itemprop":"title"}))
                job["company"] = soup.find("h2", attrs={"class":"k-inline-block"}).string
                job["location"] = soup.find("span", attrs={"itemtype":"http://schema.org/PostalAddress"}).string
                job["published_date"] = soup.find("div", attrs={"class":"k-text-subdued k-text-caption md:k-text-right"}).find("p").string
                job["source"] = "kalibrr.com"
                job["link"] = links[i]
                if not is_published_date_good3(job["published_date"]):
                    continue
                job["published_date"] = get_published_date3(job["published_date"])
                job["job_field"] = job_field
                result.append(job)
            except Exception:
                continue
        return result
    except Exception:
        return []

def scrap_jobs_from_linkedin(job_field):
    try:
        email = os.environ["EMAIL"]
        password = os.environ["PASS"]
        
        # Login
        driver = webdriver.Chrome(webdriver.ChromeOptions())
        driver.get("https://linkedin.com/uas/login")
        time.sleep(5)
        username = driver.find_element("id", "username")
        username.send_keys(email) 
        pword = driver.find_element("id", "password")
        pword.send_keys(password)    
        driver.find_element("xpath", "//button[@type='submit']").click()
        time.sleep(5)
        driver.get("https://www.linkedin.com/jobs/search/?keywords={}".format(job_field))  
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        jobs = soup.find_all("div", attrs={"data-view-name":"job-card"})

        result = []
        for job in jobs:
            try:
                info = {"title": '', "company": '', "location": "", "link": "", "source": "", "published_date": "", "job_field": ""}
                info["link"] = "https://www.linkedin.com/" + job.find("a")["href"]
                driver.get(info["link"])
                page_source = driver.page_source
                job = BeautifulSoup(page_source, 'html.parser')
                info["title"] = job.find('div', attrs={"class":"t-24 job-details-jobs-unified-top-card__job-title"}).find("h1").get_text()
                info["company"] = job.find("div", attrs={"class":"job-details-jobs-unified-top-card__company-name"}).find("a").get_text()
                job = job.find("div", attrs={"class":"job-details-jobs-unified-top-card__primary-description-container"}).find_all("span", attrs={"class":"tvm__text tvm__text--low-emphasis"})
                info["location"] = job[0].get_text()
                info["published_date"] = job[2].find_all("span")[-1].get_text()
                info["source"] = "linkedin.com/jobs"
                if not is_published_date_good4(info["published_date"]):
                    continue
                info["published_date"] = get_published_date4(info["published_date"])
                info["job_field"] = job_field
                result.append(info)
            except Exception:
                continue
        return result
    except Exception:
        return []
        

def scrap_jobs():
    jobs = []
    for job_field in ["programmer", "data", "network", "cyber security"]:
        while len(jobs) == 0:
            jobs = jobs + scrap_jobs_from_karir(job_field)
        jobs = jobs + scrap_jobs_from_jobstreet(job_field)
        jobs = jobs + scrap_jobs_from_kalibrr(job_field)
        jobs = jobs + scrap_jobs_from_linkedin(job_field)
    return jobs

def check_if_table_exists(cur):
    CHECK_IF_TABLE_EXISTS_COMMAND = """SELECT EXISTS (
        SELECT FROM pg_tables
        WHERE  schemaname = 'public'
        AND    tablename  = 'job'
    )"""
    
    try:
        cur.execute(CHECK_IF_TABLE_EXISTS_COMMAND)
        result = cur.fetchall()[0][0]
        print(result)
        return result
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def create_table(conn, cur):
    CREATE_TABLE_COMMAND = '''
        CREATE TABLE job(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            company VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL,
            link VARCHAR(255) NOT NULL,
            source VARCHAR(255) NOT NULL,
            published_date VARCHAR(255) NOT NULL,
            job_field VARCHAR(255) NOT NULL
        )
    '''
    try:
        cur.execute(CREATE_TABLE_COMMAND)
        conn.commit()
        result = cur.fetchall()[0][0]
        print("Create table: ", result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
def truncate_table(conn, cur):
    TRUNCATE_TABLE_COMMAND = '''
        truncate job
    '''
    try:
        cur.execute(TRUNCATE_TABLE_COMMAND)
        conn.commit()
        result = cur.fetchall()[0][0]
        print("Truncate table: ", result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
def insert_jobs(conn, cur, jobs):
    try:
        for job in jobs:
            cur.execute("insert into job(title, company, location, link, source, published_date, job_field) values (%s, %s, %s, %s, %s, %s, %s)", 
                (job["title"],
                job["company"],
                job["location"],
                job["link"],
                job["source"],
                job["published_date"],
                job["job_field"])
            )
            conn.commit()
        result = cur.fetchall()[0][0]
        print("Insert all jobs: ", result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def main():    
    jobs = scrap_jobs()
    conn = psycopg2.connect('postgres://avnadmin:AVNS_4bs3MyIAyVcRfFZ3shQ@iap-online-mysql.c.aivencloud.com:10372/defaultdb?sslmode=require')
    cur = conn.cursor()
    cur.execute('SELECT VERSION()')
    version = cur.fetchone()[0]
    print(version)
    if (not check_if_table_exists(cur)):
        create_table(conn, cur)
    else:
        truncate_table(conn, cur)
    check_if_table_exists(cur)
    insert_jobs(conn, cur, jobs)
    return jobs, 200

if __name__ == "__main__":
    main()