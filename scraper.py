from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd

def getDriver():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("useAutomationExtension", False)
    #This is mentioned in documentation it is a must add item to prevent bugs
    options.add_argument("--disable-gpu")
    service=ChromeService(executable_path="D:\Portal\Python\Email Automation\driver\chromedriver.exe")
    driver=webdriver.Chrome(service=service,options=options)
    return driver

def getSchoolLink(html_path):
    driver=getDriver()
    driver.get(html_path)
    driver.switch_to.alert.accept()
    content=driver.page_source
    soup=BeautifulSoup(content,features="html.parser")
    td_list=soup.findAll("td",attrs={'class':"sorting_1"})
    a_list=[]
    school_name=[]
    for td in td_list:
        a=td.find("a",href=True)
        a_list.append(a['href'])
        decoded_school_name=a.decode_contents()
        school_name.append(decoded_school_name)

    data={'School Name':school_name,
          'School_Links':a_list }
    
    df=pd.DataFrame(data)
    driver.close()
    return df

def getSchoolEmail(df):
    school_email=[]
    for page_link in df['School_Links']:
        driver=getDriver()
        driver.get(page_link)
        content=driver.page_source
        soup=BeautifulSoup(content,features="html.parser")
        contact=soup.find("div",attrs={'class':"contact"})
        a_href=contact.findAll("a",href=True)
        try:
            school_email.append(a_href[1].text)
            print(a_href[1].text)
        except:
            school_email.append(None)
        driver.close()
    df['Email']=school_email
    return df