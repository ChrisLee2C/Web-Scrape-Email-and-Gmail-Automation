import scraper
from data.credentials.config import *

def school_email_scrape(html_path,file_name):
    school_link=scraper.getSchoolLink(html_path)
    print(school_link)
    email_df=scraper.getSchoolEmail(school_link)
    print(email_df)
    email_df.to_csv(f'data/school email/{file_name}_email.csv', index=False)

#Scrape Primary School Email
primary_school_html_path=PRIMARY_SCHOOL_HTML_PATH
csv_name="primary_school"
school_email_scrape(primary_school_html_path,csv_name)

#Scrape Secondary School Email
secondary_school_html_path=SECONDARY_SCHOOL_HTML_PATH
csv_name="secondary_school"
school_email_scrape(secondary_school_html_path,csv_name)