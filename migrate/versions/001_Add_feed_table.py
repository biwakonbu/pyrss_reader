from sqlalchemy import *
from migrate import *

meta = MetaData()

feed = Table(
    'feeds', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(32)),
    Column('type', String(8)),
    Column('htmlUrl', String(256)),
    Column('xmlUrl', String(256))
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    feed.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    feed.drop()
