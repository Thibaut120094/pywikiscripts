#!/usr/bin/python
# -*- coding: utf-8 -*-
# Cherche les redirections de modèles qui n'ont pas le modèle {{Redirection de modèle}}.

import pywikibot
import codecs

site = pywikibot.Site(u'fr', u'wikipedia', u'RobokoBot')

with codecs.open('out.txt','w', "utf-8") as file:
  for page in pywikibot.site.APISite.allpages(site,start="!",namespace=10,filterredir=True):
   if u"edirection de modèle" not in page.text:
    print page.title()
    title = page.title()
    file.write("# [[" + title + "]]\n")
