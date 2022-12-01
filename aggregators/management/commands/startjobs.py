#app
from aggregators.models import Article, Channel

#Django
from django.conf import settings
from django.core.management.base import BaseCommand

#Third party
import feedparser, requests
from dateutil import parser

def save_new_article(channel, channel_name, channel_topic):
    """Save new articles for a feedparser object"""

    for feed_entry in channel.entries[0:20]:
        if not Article.objects.filter(guid=feed_entry.id).exists():
            article = Article(
                name = feed_entry.title,
                topic = channel_topic,
                created_time = parser.parse(feed_entry.published),
                url = feed_entry.link,
                series_name = channel_name,
                guid = feed_entry.id,
            )
            article.save()

def fetch_new_article():
    channel_list = Channel.objects.all()
    for channel in channel_list:
        channel_data = feedparser.parse(requests.get(channel.rss_feed, headers={"User-Agent": "Mozilla/5.0"}).content)
        save_new_article(channel_data, channel.name, channel.topic)


class Command(BaseCommand):
    def handle(self, *args, **options):
        fetch_new_article()
