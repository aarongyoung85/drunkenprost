from flask import Flask
from sql import sqlserver
from sql.drunkenprost_orm import Topics, topics_map
app = Flask(__name__)
logger = app.logger

class HomePage(object):

    def __init__(self):
        self.db = sqlserver.DrunkenProstServer()

    def get_topics(self):
        topics = []
        result = self.db.query(Topics).all()

        for row in result:
            topics.append(row.topic.capitalize())

        return topics

    def get_recent_entries_by_topic(self):
        recent_entries = {}
        topics = self.get_topics()

        for topic in topics:
            result = self.db.query(topics_map[topic]).order_by(topics_map[topic].created.desc()).limit(3).all()

            recent_entries[topic] = []
            for row in result:
                recent_entries[topic].append({'id': row.id, 'display_name': row.display_name.decode('utf-8')})

        return recent_entries
