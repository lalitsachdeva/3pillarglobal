# Suppose we have a text with many email addresses
import re
str = 'purple ali.ce@google.com, https://www.facebbok.edu blah monkey bob@abc.com1 blah dishwasher'

  ## Here re.findall() returns a list of all the found email strings
#emails = re.findall(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', str) ## ['alice@google.com', 'bob@abc.com']
#"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", 
emails = re.findall(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", str)
for email in emails:
   # do something with each found email string
   print email