#!/usr/bin/python
# -*- coding: utf-8 -*-

import pywikibot
import re

site = pywikibot.Site(u'fr', u'wiktionary', u'RobokoBot')
category = pywikibot.Category(site, u"japonais")
list = [u"’", u"\'", u"…", u"..."]

for page in pywikibot.site.APISite.allpages(site, start="!", namespace=[0], filterredir=False):
 title = page.title()
 if title not in list:
   regex1 = ur"^\[\[(\w{1,6}|zh-min-nan|roa-rup)\:%s\]\]\s*(\n|$)" % re.escape(title)
   pattern = re.findall(regex1, page.text, flags=re.MULTILINE)
   if pattern:
     page.text = re.sub(regex1, "", page.text, flags=re.MULTILINE)
     page.save(u"Retrait des liens interlangues qui sont maintenant gérés automatiquement par [[:mw:Extension:Cognate]].")
