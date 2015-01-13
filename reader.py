# coding: utf-8

import os
import import_opml
import feedparser

from flask import Flask, request, redirect
from flask import url_for, render_template
from werkzeug import secure_filename
from model import Feed

app = Flask(__name__)
app.debug = True
READER_PATH = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = set(['xml'])
FILE = 'file'

def allowed_file(filename):
  has_extension = '.' in filename
  is_allowed_extenstion = filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
  return has_extension and is_allowed_extenstion

def has_blank(outline):
  if outline['title'] and outline['htmlUrl'] and outline['xmlUrl']:
    return False
  return True

def get_links(xmlUrl):
  items = feedparser.parse(xmlUrl)['items']
  return [{'title': x['title'], 'href': x['id']} for x in items]

@app.route('/')
def reader():
  feeds = Feed().query.all()
  entries = {}
  for feed in feeds:
    entries[feed.xmlUrl] = get_links(feed.xmlUrl)
  return render_template('app.html', feeds=feeds, name=FILE, entries=entries)

@app.route('/import', methods=['POST'])
def opml_import():
  if request.method == 'POST':
    f = request.files[FILE]
    if f and allowed_file(f.filename):
      outlines = import_opml.read(f.stream)
      for outline in import_opml.flatten(outlines):
        feed = Feed(
          outline['title'],
          outline['type'],
          outline['htmlUrl'],
          outline['xmlUrl'])
        if (not has_blank(outline)) and (not feed.exists()):
          try:
            feed.save()
          except:
            return 'import error.'
  return redirect(url_for('reader'))

if __name__ == "__main__":
  app.run()
