#!/usr/bin/env python
# -*- coding: utf-8 -*-

from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

smtp = SMTP('smtp.gmail.com', 587)

smtp.ehlo()

smtp.starttls()

smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

smtp.sendmail(EMAIL_HOST_USER, 'boatengpato.pb@yahoo.com', 'Subject: Testing\nTesting my new email sending app')

print(smtp.quit())


