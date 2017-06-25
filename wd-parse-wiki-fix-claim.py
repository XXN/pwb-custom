#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (C) XXN, 2017
#
from __future__ import absolute_import, unicode_literals

import re, urllib
import pywikibot
from pywikibot.page import url2unicode

sname = \
    [
                u"Q3432019",
                u"Q4566912",
                u"Q4998609",
                u"Q6033510",
                u"Q6033541",
                u"Q6321440",
                u"Q6370426",
                u"Q6491743",
                u"Q1642676",
                u"Q8077119",
                u"Q5963450",
                u"Q5963460",
                u"Q5963575",
                u"Q6321489",
                u"Q6453642",
                u"Q7796096",
                u"Q8077114",
                u"Q16106758",
                u"Q11989881",
                u"Q16008087",
                u"Q3377631",
                u"Q3889835",
                u"Q4585958",
                u"Q4586124",
                u"Q4890343",
                u"Q5614693",
                u"Q6217051",
                u"Q6515779",
                u"Q7083024",
                u"Q7513241",
                u"Q7652304",
                u"Q7666547",
                u"Q7825356",
                u"Q11988336",
                u"Q1554799",
                u"Q4559180",
                u"Q4574418",
                u"Q4579325",
                u"Q4585162",
                u"Q4753928",
                u"Q4919560",
                u"Q5653836",
                u"Q6215389",
                u"Q6321526",
                u"Q6437981",
                u"Q6453629",
                u"Q6519406",
                u"Q6419432",
                u"Q6696992",
                u"Q7077434",
                u"Q7083007",
                u"Q7179285",
                u"Q8077117",
                u"Q8077250",
                u"Q547980",
                u"Q1367511",
                u"Q1777055",
                u"Q4573666",
                u"Q4723562",
                u"Q4794689",
                u"Q4919880",
                u"Q6148860",
                u"Q7037410",
                u"Q7651864",
                u"Q8077253",
                u"Q8079339",
                u"Q3442938",
                u"Q4753827",
                u"Q4790656",
                u"Q4794682",
                u"Q5367433",
                u"Q8077233",
    ]

count = 0
for a in sname[0:]:
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    item = pywikibot.ItemPage(repo, a)
    item.get()
    mypage = item.sitelinks['enwiki']
    ssite = pywikibot.getSite("en")
    spage = pywikibot.Page(ssite, mypage)
    text = spage.get()
    count = count + 1
    if 'P31' in item.claims:# and item.claims['P31'][0].getTarget().title() == 'Q5':
        m0 = re.search(ur"\{\{\s*Stortingetbio\s*\|\s*(?:id=)?\s*([^\s}\|]+)\s*[\|\}]", text, flags=re.IGNORECASE)
        if m0:
            m = m0.group(1)
# Convert URL-encoded characters to unicode
            target = url2unicode(m)            
        if 'P3072' in item.claims:
            claim1 = item.claims["P3072"][0]
            claim1.changeTarget(target)
            pywikibot.output(u"Changed claim target to \03{{lightgreen}}{}\03{{default}} for {} - Nr. {}".format(target,a,count))
        else:
            pywikibot.output(u"Item \03{{lightred}}{}\03{{default}} already has P3072 - Nr. {}".format(a,count))
    else:
        pywikibot.output(u"Item \03{{lightred}}{}\03{{default}} doesn't have P31:Q5 - it's not what I need - Nr. {}".format(a,count))
