# Web Scrape Email and Gmail Automation

## What did I use
1. Selenium, for retrieving page source and navigating websites
2. Beautiful Soup, for extracting page and email links
3. Gmail Api, for sending email 
4. Python, for making this thing to work

## Why did I build this project
Recently, I need to help an NGO OnFire HK, to send email to primary and secondary schools in Hong Kong, to promote projects of volunteer tuition for the underprivileged.<br />
There are about 1000 primary and secondary schools in Hong Kong and it will take a long time for me to gather their email and manually send email to them.<br />
Fortunately, there is a website which has gathered their email already, but the emails are separated in pages. Therefore, I utilized Selenium and Beautiful Soup to scrape the page with a table of page links containing the email inside, then open each page links with Selenium and scrape the email and turn them to csv files.<br />
After preparing the cav files of email links, I used Gmail api to send emails recursively.<br />
The code is developed in a few days for test and error, but the whole automate scraping and sending email action can be done in about 2 hours. I believe the efficiency of both actions can be enhanced by using a few threads and a queue for concurrent scraping and sending.<br />

## Some reminder
1. Always respect the robots.txt
2. The table in www.schooland.hk could not show all school page links in the table, so I tweaked the values a little bit in the html, and save the modified html for use
3. The chrome driver should always be up to date 