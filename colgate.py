#!/usr/bin/python
# -*- coding: utf-8 -*-

import pywikibot
import re

site = pywikibot.Site(u'fr', u'wiktionary', u'RobokoBot')
category = pywikibot.Category(site, u"japonais")

for page in pywikibot.site.APISite.categorymembers(site, category, namespaces=[0]):
   title = page.title()
   regex1 = ur"^\[\[(\w{1,6}|zh-min-nan)\:%s\]\]\s*(\n|$)" % title
   pattern = re.findall(regex1, page.text, flags=re.MULTILINE)
   print title
   if pattern:
     page.text = re.sub(regex1, "", page.text, flags=re.MULTILINE)
     page.save(u"Retrait des liens interlangues qui sont maintenant gérés automatiquement par [[:mw:Extension:Cognate]].")
