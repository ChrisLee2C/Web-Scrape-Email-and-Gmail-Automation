from send_email import send_email
from data.credentials.config import *
import pandas as pd
import concurrent.futures

def send_email_to_school(school_email):
    for i in range(len(school_email)):
        if(school_email.isnull()[i]):
            continue
        else:
            send_email(TOKEN_PATH,CREDENTIALS_PATH,MESSAGE,school_email[i],FROM_EMAIL_ADDRESS,EMAIL_SUBJECT,ATTACHMENT_NAME)

df_primary_school=pd.read_csv(PRIMARY_SCHOOL_EMAIL_PATH)
df_secondary_school=df=pd.read_csv(SECONDARY_SCHOOL_EMAIL_PATH)
email_primary_school=df_primary_school['Email']
email_secondary_school=df_secondary_school['Email']
with concurrent.futures.ThreadPoolExecutor(5) as executor:
    executor.map(send_email_to_school,email_primary_school)
    executor.map(send_email_to_school,email_secondary_school)