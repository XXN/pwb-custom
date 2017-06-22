#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (C) XXN, 2017
#
from __future__ import absolute_import, unicode_literals

import os, re, sys, time
import pywikibot

def main():
    site = pywikibot.Site('wikidata', 'wikidata')
    repo = site.data_repository()

    mylist = \
        [
                u"Q3001778",
                u"Q37115",
                u"Q55246",
                u"Q55563",
                u"Q55611",
        ]
    
    targetlangs = ['bg', 'bs', 'ca', 'cs', 'da', 'de', 'en', 'en-ca', 'en-gb', 'el', 'es', 'fi', 'fr', 'hr', 'hu', 'it', 'lv', 'mk', 'nb', 'nl', 'nn', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sco', 'sh', 'sk', 'sl', 'sr', 'sv', 'tr', 'uk', ]
   
    for q in mylist[0:]:
        item = pywikibot.ItemPage(repo, q)
        item.get()
        if 'P577' in item.claims and item.claims['P31'][0].getTarget().title() == 'Q7889':
            try:
                myclaim = item.get()['claims']['P577'][0].getTarget()
                dic = myclaim.toWikibase()
                Text = myclaim.toTimestr()
            
                if dic['precision'] >= 9:
                    year = str(int(Text[8:12]))
                    for targetlang in targetlangs:
                        translations = {
                            'bg': 'видеоигра от ~YEAR~ година',
                            'bs': 'videoigra',
                            'ca': 'videojoc de ~YEAR~',
                            'cs': 'videohra z roku ~YEAR~',
                            'da': 'computerspil fra ~YEAR~',
                            'de': 'Videospiel',
                            'en': '~YEAR~ video game',
                            'en-ca': '~YEAR~ video game',
                            'en-gb': '~YEAR~ video game',  
                            'el': 'βιντεοπαιχνίδι του ~YEAR~', 
                            'es': 'videojuego de ~YEAR~',
                            'fi': '~YEAR~ videopeli',
                            'fr': 'jeu vidéo de ~YEAR~',
                            'hr': 'videoigra',
                            'hu': 'videojáték',
                            'it': 'videogioco del ~YEAR~',
                            'lv': 'videospēle',
                            'mk': 'видеоигра од ~YEAR~ година',
                            'nb': 'videospill fra ~YEAR~',
                            'nl': 'computerspel uit ~YEAR~',
                            'nn': 'dataspel frå ~YEAR~',
                            'pl': 'gra wideo z ~YEAR~ roku',
                            'pt': 'vídeojogo de ~YEAR~',
                            'pt-br': 'jogo eletrônico de ~YEAR~',
                            'ro': 'joc video din ~YEAR~',
                            'ru': 'видеоигра ~YEAR~ года',
                            'sco': 'video gemme',
                            'sh': 'videoigra',
                            'sk': 'počítačová hra z ~YEAR~',
                            'sl': 'videoigra iz leta ~YEAR~',
                            'sr': 'видео-игра',
                            'sv': 'datorspel från ~YEAR~',
                            'tr': '~YEAR~ video oyunu',
                            'uk': 'відеогра ~YEAR~ року',
                        }
                        descriptions = item.descriptions
                        addedlangs = []
                        for lang in translations.keys():
                            if not lang in descriptions.keys():
                                translation = translations[lang]
                                translation = translation.replace('~YEAR~', str(year))
                                descriptions[lang] = translation
                                addedlangs.append(lang)
                        data = { 'descriptions': descriptions }
                        addedlangs.sort()
                        if addedlangs:
                            summary = 'Bot: Adding descriptions (%s languages): %s' % (len(addedlangs), ', '.join(addedlangs))
                            try:
                                item.editEntity(data, summary=summary)
                                pywikibot.output(u'{} - \03{{lightgreen}}{}\03{{default}}'.format(q,translations['en'].replace('~YEAR~', str(year))))
                            except:
                                pywikibot.output('Error while saving {}'.format(q))
                                continue
            except:
                continue
        else:#no P577
            for targetlang in targetlangs:
                translations = {
                    'bg': 'видеоигра',
                    'bs': 'videoigra',
                    'ca': 'videojoc',
                    'cs': 'videohra',
                    'da': 'computerspil',
                    'de': 'Videospiel',
                    'en': 'video game',
                    'en-ca': 'video game',
                    'en-gb': 'video game',  
                    'el': 'βιντεοπαιχνίδι', 
                    'es': 'videojuego',
                    'fi': 'videopeli',
                    'fr': 'jeu vidéo',
                    'hr': 'videoigra',
                    'hu': 'videojáték',
                    'it': 'videogioco', 
                    'lv': 'videospēle',
                    'mk': 'видеоигра',
                    'nb': 'videospill',
                    'nn': 'dataspel',
                    'nl': 'computerspel',
                    'pl': 'gra wideo',
                    'pt': 'vídeojogo',
                    'pt-br': 'jogo eletrônico', 
                    'ro': 'joc video',
                    'ru': 'видеоигра',
                    'sco': 'video gemme',
                    'sh': 'videoigra',
                    'sk': 'počítačová hra',
                    'sl': 'videoigra',
                    'sr': 'видео-игра',
                    'sv': 'datorspel',
                    'tr': 'video oyunu',
                    'uk': 'відеогра',
                }
                descriptions = item.descriptions
                addedlangs = []
                for lang in translations.keys():
                    if not lang in descriptions.keys():
                        translation = translations[lang]
                        descriptions[lang] = translation
                        addedlangs.append(lang)
                data = { 'descriptions': descriptions }
                addedlangs.sort()
                if addedlangs:
                    summary = 'Bot: Adding descriptions (%s languages): %s' % (len(addedlangs), ', '.join(addedlangs))
                    print(summary)
                    try:
                        item.editEntity(data, summary=summary)
                        pywikibot.output(u'{} - \03{{lightgreen}}{}\03{{default}}'.format(q,translations['en']))
                    except:
                        pywikibot.output('Error while saving {}'.format(q))
                        continue

if __name__ == "__main__":
    main()
