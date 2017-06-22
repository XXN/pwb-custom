#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (C) XXN, 2017
#
from __future__ import absolute_import, unicode_literals

import re, pywikibot

sname = \
    [
#                u"Adare, Queensland",
#                u"Airdmillan, Queensland",
#                u"Bloomsbury, Queensland",              
#                u"Bybera, Queensland",
#                u"Chelona, Queensland",
#                u"Dynevor, Queensland",
#                u"Haly Creek, Queensland",
#                u"Hampden, Queensland",
#                u"Oakenden, Queensland",
#                u"Prospect, Queensland",
#                u"Ringwood, Queensland",
#                u"Riversleigh, Queensland",
#                u"Shoal Point, Queensland",
#                u"St Helens Beach",
#                u"Upper Warrego",
#                u"Yalboroo, Queensland",
                u"Yandilla, Queensland",
                u"Yandina, Queensland",
                u"Yangan, Queensland",
                u"Yarrabilba, Queensland",
                u"Yarraden, Queensland",
                u"Yarwun, Queensland",
                u"Yengarie, Queensland",
                u"Yeppoon",
                u"Yeronga, Queensland",
                u"Yimbun, Queensland",
                u"Yorkeys Knob, Queensland",
                u"Zillmere, Queensland",
    ]

count = 0
for a in sname[0:]:
    ssite = pywikibot.getSite("en")
    spage = pywikibot.Page(ssite, a)
    text = spage.get()
    site = pywikibot.Site("wikidata", "wikidata")
    item = pywikibot.ItemPage.fromPage(spage)
    item.get()
    count = count + 1
    if 'P131' in item.claims:
        if not 'P3257' in item.claims:
            m0 = re.search("\{\{\s*cite\s*QPN\s*\|\s*(\d+)\s*\|\s*", text, flags=re.IGNORECASE)
            if m0:
                for m in re.finditer("\{\{\s*cite\s*QPN\s*\|\s*(\d+)\s*\|\s*", text, flags=re.IGNORECASE):
                    newclaim = pywikibot.page.Claim(site, 'P3257')
                    target = m.group(1)
                    newclaim.setTarget(target)
                    item.addClaim(newclaim, summary = 'imported from {}'.format(spage))#Added [[Property:P3257]]
                    source = pywikibot.Claim(site, u'P143')
                    enwp = pywikibot.ItemPage(site, u'Q328')
                    source.setTarget(enwp)
                    newclaim.addSource(source)
                    pywikibot.output(u"Added {} to \03{{lightgreen}}{}\03{{default}} - Nr. {}".format(target,a,count)) 
            else:
                pywikibot.output(u"\03{{lightred}}No matches for Cite QPN in {}\03{{default}} - Nr. {}".format(a,count)) 
        else:
            pywikibot.output(u"Item \03{{lightred}}{}\03{{default}} already has P3257 - Nr. {}".format(a,count))
    else:
        pywikibot.output(u"Item \03{{lightred}}{}\03{{default}} doesn't have P131 - it's not what I need - Nr. {}".format(a,count))
