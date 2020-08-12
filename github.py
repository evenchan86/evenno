#!/usr/bin/python
#-*- coding: UTF-8 -*-
import requests
import xml.etree.ElementTree as ET
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

feed = requests.get('https://opscloud.vip/atom.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w') as f:
    f.write(r'''
## Latest blog posts
''')
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        published = entry.find('nsfeed:published', nsfeed).text[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('''
[>>> More blog posts](https://opscloud.vip/archives/)

## Statistics
![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=evenno&show_icons=true&theme=dark)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=evenno&hide=ipynb,html&layout=compact)
''')