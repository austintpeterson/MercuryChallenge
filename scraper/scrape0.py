#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 13:30:02 2018

@author: allee
"""

from newspaper import Article
import cfscrape

root='http://www.syriahr.com'
scraper=cfscrape.create_scraper(root)

urls = db.fetch("""
select Event_ID, GSS_Link
from gold_standard_report
where Event_ID not in (select Event_ID from gold_standard_article)
and GSS_Link like '{}%'""".format(root))

print(len(urls))

for event_id, url in urls:
    print(event_id, url); sys.stdout.flush()
    try:
        gold=scraper.get(url).content
    except:
        print('failed', url)
    continue

    print("scraped"); sys.stdout.flush()
    article=Article(url, memoize_articles=False)
    article.download(input_html=gold)
    article.parse()
    article.nlp()
    text = article.text
    keywords = article.keywords
    title = article.title
    if title:
        print(title)
    elif text:
        print(text)
    else:
        print('skipped, not title or text')
    continue
    db.store('replace into gold_standard_article(Event_ID,title,text) values (?,?,?)',
             (event_id, title, text))
    for keyword in keywords:
        db.store('replace into gold_standard_keywords(Event_ID, keyword) values (?,?)',
                 (event_id, keyword))