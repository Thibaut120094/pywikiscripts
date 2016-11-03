#!/usr/bin/python
# -*- coding: utf-8 -*-

import feedparser
import re
import pywikibot

rss_url = u"http://www.crunchyroll.com/rss/anime?lang=en"
feed = feedparser.parse(rss_url)

site = pywikibot.Site(u'fr', u'wikipedia', u'RobokoBot')
page = pywikibot.Page(site, u"Module:Nombre d\'épisodes d\'anime/data")

for post in feed.entries:
  if u"Naruto Shippuden" in post.title:
   nbepisode = post.title
   break

match = re.search(ur'Episode (\d+)', nbepisode)
nbepisode = match.group(1)

match = re.search(ur'\s*?\["Naruto Shippuden"\]\s*?=\s*?(\d+)\s*?,', page.text)
oldnbepisode = match.group(1)

nbepisode = int(nbepisode)
oldnbepisode = int(oldnbepisode)
  
if nbepisode > oldnbepisode:
  page.text = re.sub(ur'(\s*?\["Naruto Shippuden"\]\s*?=\s*?)\d+(\s*?,)', ur'\g<1>%d\g<2>' % (nbepisode), page.text)
  print(page.text)
  page.save(u'Mise à jour du nombre d’épisodes de [[Naruto Shippuden]] depuis Crunchyroll.')

else :
  print(u'Page not saved.')
  print(u'Cruchyroll: %d' % nbepisode)
  print(u'Wikipedia: %d' % oldnbepisode)
