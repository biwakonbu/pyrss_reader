import opml

def read(filepath):
  return opml.parse(filepath)

def flatten(outline):
  sites = []
  for x in outline:
    if hasattr(x, "xmlUrl"):
      sites.append({
        'title': x.title,
        'type': x.type,
        'htmlUrl': x.htmlUrl,
        'xmlUrl': x.xmlUrl
      })
    else:
      sites.extend(flatten(x))
  return sites

if __name__ == '__main__':
  outline = read('export.xml')
