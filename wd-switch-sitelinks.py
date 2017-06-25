#!/usr/bin/python
# -*- coding: utf-8  -*-
# Robot de mutare (interschimbare) a linkurilor (si label-urilor) intre itemii wikidata: Category:Death in % <--> Category:Deaths in %
#
# (C) XXN, 2017
#

import pywikibot, re, sys, locale

mylist =  \
    [
                u"Q8365644",
                u"Q8365687",
                u"Q8365696",
                u"Q8365702",
                u"Q8365656",
                u"Q8365672",
                u"Q8365591",
                u"Q8365602",
                u"Q8365616",
                u"Q8365682",
    ]

count = 0
for a in mylist[0:]:
    try:
        site = pywikibot.Site("wikidata", "wikidata")
        repo = site.data_repository()
        fromItem = pywikibot.ItemPage(repo, a)
        fromItem.get()
        label1 = fromItem.labels['en']
        link1 = fromItem.sitelinks['enwiki']        
        label2 = label1.replace("Category:Death in", "Category:Deaths in")
        tsite = pywikibot.getSite("en")
        tpage = pywikibot.Page(tsite, label2)
        toItem = pywikibot.ItemPage.fromPage(tpage)
        toItem.get()
        count = count + 1
        if ('ruwiki' in fromItem.sitelinks and u'Умершие' in fromItem.sitelinks['ruwiki']) or \
            ('frwiki' in fromItem.sitelinks and u'Décès' in fromItem.sitelinks['frwiki']) or \
            ('itwiki' in fromItem.sitelinks and 'Morti' in fromItem.sitelinks['itwiki']):            
            data1 = {'labels': {'en': ''},
                 'sitelinks': [{'site': 'enwiki', 'title': ''}]}
            fromItem.editEntity(data1, summary=u'Removed [en] label & sitelink, moving to [[%s]]' % toItem.title())
            data2 = {'labels': {'en': '%s' % label1},
                 'sitelinks': [{'site': 'enwiki', 'title': '%s' % link1}]}
            toItem.editEntity(data2, summary=u'Fixed [en] label & sitelink, moved from [[%s]]' % fromItem.title())            
            data10 = {'labels': {'en': '%s' % label2},
                 'sitelinks': [{'site': 'enwiki', 'title': '%s' % label2}]}
            fromItem.editEntity(data10, summary=u'Added [en] label & sitelink, moved from [[%s]]' % toItem.title())
            pywikibot.output(u"\03{{lightgreen}}Edited\03{{default}} items {} & {} ({} vs. {}) - Nr.{}".format(fromItem.title(), toItem.title(), label1, label2, count))
        else:
            pywikibot.output(u"No fr/it/ru sitelinks found in \03{{lightred}}{}\03{{default}}; don't touch the item - Nr.{}".format(fromItem.title(), count))
    except pywikibot.exceptions.NoPage:
        pywikibot.output(u'NoPage {} [{} / {}] - Nr.{}'.format(fromItem.title(), label1, label2, count))
