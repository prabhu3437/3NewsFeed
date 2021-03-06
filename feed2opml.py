#!/usr/bin/env python

# 2013-01-10

# Dump NewsFeed database as an OPML file.

# Usage: ./feed2opml.py > myfeeds.opml


from newsfeed import ContentItem, NewsWire, SearchWire, config_file

import os, pickle, html

newfeeds = []
config   = {}

newsfeeds, config = pickle.load(open(config_file, 'rb'))

print('<?xml version="1.0" encoding="utf-8"?>')
print('<opml version="1.0">\n<head><title>NewsFeed Bookmarks</title></head>\n<body>')

def mkfile(t):
	t = "".join([x for x in t if x.isalnum()][:16])
	return t.lower()

for i,f in enumerate(newsfeeds):
	if not isinstance(f, SearchWire):
		title = html.escape(f.name.replace('"', '\\"'))
		name = f.name
		url = html.escape(f.url)
		homeurl = html.escape(f.homeurl)
		fn = 'filename="%s%04u.xml"' % (mkfile(name), i + 1)
		print('<outline text="%s" title="%s" xmlUrl="%s" description="" type="rss" htmlUrl="%s" %s />' % (
			title, title, url, homeurl, fn))

print('</body></opml>')
