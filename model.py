from os.path import abspath, dirname
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relation, Session
from sqlalchemy.ext.declarative import declarative_base

class ReaderEngine():
  def __init__(self):
    self.sqlpath = 'sqlite:///' + dirname(abspath(__file__)) + '/rss_reader.db'
    self.engine = create_engine(self.sqlpath)

engine = ReaderEngine().engine
Base = declarative_base(engine)
session = Session(ReaderEngine().engine)

class Model():
  def __init__(self):
    self.query = session.query(self.__class__)

  def save(self):
    try:
      session.add(self)
      session.commit()
    except:
      session.roleback()
      raise

class Feed(Base, Model):
  __tablename__ = 'feeds'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  type =  Column(String)
  htmlUrl = Column(String)
  xmlUrl = Column(String)

  def __init__(self, title='', type='', htmlUrl='', xmlUrl=''):
    Model.__init__(self)
    self.title = title
    self.type = type
    self.htmlUrl = htmlUrl
    self.xmlUrl = xmlUrl

  def exists(self):
    q = self.query.filter(Feed.htmlUrl == self.htmlUrl)
    return session.query(q.exists()).scalar()

if __name__ == '__main__':
  print(Feed(htmlUrl='http://d.hatena.ne.jp/ikkou2otosata0/').exists())
