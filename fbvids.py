import sys
import argparse
import urllib.request

def xpartition(bigstr,sep1,sep2):
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

fbsrc = urllib.request.Request(cleanurl, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "DNT": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "cross-site","Sec-Fetch-User": "?1","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"}) 
with urllib.request.urlopen(fbsrc) as fbdata1:
 fbstr=str(fbdata1.read())

try:
 fbstr.index('playable_url')
except ValueError:
 print('Check URL.')

mediastr = xpartition(fbstr,'"playable_url":',',"spherical_video_fallback_urls')
medialist = mediastr.split('"')
if (':null' in medialist) or ('_nc_vs' in medialist[5]):
 vidurl = medialist[1].replace('\\','')
else:
 vidurl = medialist[5].replace('\\','')
 
filename = xpartition(vidurl,'/','?')

vidreq = urllib.request.Request(vidurl, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "DNT": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "cross-site","Sec-Fetch-User": "?1","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"})
with urllib.request.urlopen(vidreq) as vidobj:
 vidata=vidobj.read()
with open(filename,'wb') as vid:
 vid.write(vidata)
