import sys
import argparse
import urllib.request


def partition(bigstr,sep1,sep2):
 x=bigstr.rpartition(sep1)
 y=x[2].rpartition(sep2)
 return y[0]

fb_parse = argparse.ArgumentParser(prog='FBVids', description="This script downloads Facebook videos.")
fb_parse.add_argument('userurl', help='URL of the FB video.')
argsobj = fb_parse.parse_args()
userurl=argsobj.userurl

if('facebook.com/' in userurl):
 cleanurl = 'https://facebook.com/'+userurl.rpartition('facebook.com/')[2]
else:
 raise ValueError('Check URL.')

fbsrc = urllib.request.Request(cleanurl, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Referer": "https://www.facebook.com/", "Origin": "https://www.facebook.com", "DNT": "1", "Connection": "keep-alive", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site"}) 

with urllib.request.urlopen(fbsrc) as fbdata:
 fbstr=str(fbdata.read())

try:
 fbstr.index('hd_src:')
except ValueError:
 print('Check URL.')

mediastr = partition(fbstr,'hd_src:',',hd_tag:')     
medialist = mediastr.split('"')
vidurl= medialist[1]
filename=partition(vidurl,'/','?')

vidreq = urllib.request.Request(vidurl, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Referer": "https://www.facebook.com/", "Origin": "https://www.facebook.com", "DNT": "1", "Connection": "close", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site"})
with urllib.request.urlopen(vidreq) as vidobj:
 vidata=vidobj.read()
with open(filename,'wb') as vid:
 vid.write(vidata)
