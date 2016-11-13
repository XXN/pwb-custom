#!/usr/bin/python
# -*- coding: utf-8  -*-
# Pywikibot script for importing infoboxes (for German localities) from enwiki. This version works on one page

import pywikibot, re, sys, locale

sname = u"Saal an der Donau"
roname = u"Saal an der Donau"

ssite = pywikibot.getSite("en")
text = pywikibot.Page( ssite, sname )
text = text.get()
m0 = re.search(u"(\{\{Infobox German Location.*\}\})\n*\'\'\'", text, flags=re.DOTALL)
m0 = m0.group(1)
m0 = m0.replace("Infobox German Location", u"Cutie Orașe DE")
"""
text = re.sub(u"insee = .*\n", match, text)
box = re.sub(u"\{\{Infobox German Location(.*)\}\}\n*\'\'\'", u"{{Cutie Orașe DE%s}}\n'''" %s\1, text, flags=re.IGNORECASE|re.DOTALL)
box2 = re.search(u"(\{\{Cutie Orașe DE.*\}\})\n*\'\'\'", box, flags=re.DOTALL)
"""
#match = m1.group()
#box2 = box2.group(1)

rosite = pywikibot.getSite("ro")
page = pywikibot.Page( rosite, roname )
page = page.get()
newpage = '\n'.join((m0,page))


finpage = pywikibot.Page( rosite, roname )
finpage.put(newpage, u"robot: test")
