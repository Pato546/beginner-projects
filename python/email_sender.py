#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yagmail

receiver = "boatengpato.pb@yahoo.com"
body = "Hello there from Yagmail"
filename = 'Chapter3.pdf'

yag = yagmail.SMTP('djangouser10@gmail.com')
yag.send(to=receiver, subject='Yagmail test with attachment', contents=body, attachments=filename,)


