from send_email import send_email
from data.credentials.config import *
import pandas as pd

def send_email_to_school(school_email):
    df=pd.read_csv(school_email)
    email=df['Email']
    for i in range(len(email)):
        if(email.isnull()[i]):
            continue
        else:
            send_email(TOKEN_PATH,CREDENTIALS_PATH,MESSAGE,email[i],FROM_EMAIL_ADDRESS,EMAIL_SUBJECT,ATTACHMENT_NAME)

send_email_to_school(PRIMARY_SCHOOL_EMAIL_PATH)
send_email_to_school(SECONDARY_SCHOOL_EMAIL_PATH)