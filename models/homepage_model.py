from sql import sqlserver
from sql.drunkenprost_orm import Topics

class HomePage(object):

    def __init__(self):
        self.db = sqlserver.DrunkenProstServer()

    def get_topics(self):
        topics = []
        result = self.db.query(Topics).all()

        for row in result:
            topics.append(row.topic)

        return topics
