from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.http import HttpResponseRedirect

from .management.commands.startjobs import feedparser, requests, save_new_article



from .models import Article, Channel


@login_required
def index(request):

    if len(Article.objects.all()) != 0:
        context = {}
        temp = Article.objects.filter().order_by("-created_time")
        context["articles"] = temp[1:]
        context["newest_article"] = temp[0]

        topic_list = []
        for article in temp:
            if not article.topic in topic_list:
                topic_list.append(article.topic)
        context["topics"] = topic_list

        return render(request, 'aggregators/index.html', context)
    
    else:
        context = {}
        return render(request, 'aggregators/index.html', context)


@login_required
def topic(request, topic_name):
    
    temp1 = Article.objects.filter(topic=topic_name).order_by('-created_time')
    topical_articles = temp1[1:]
    newest_article = temp1[0]

    temp2 = Article.objects.filter().order_by("-created_time")
    topic_list = []
    for article in temp2:
        if not article.topic in topic_list:
            topic_list.append(article.topic)

    context = {'topical_articles': topical_articles, 'newest_article': newest_article, 'topics': topic_list}

    return render(request, 'aggregators/topic.html', context)

@login_required
@csrf_protect
def add_rss(request):
    """Add RSS reed user entered to database"""

    if request.method == "POST":
        
        channel_rss_feed = "{feed}".format(feed=request.POST.get("q1"))
        channel_name = request.POST.get("q2")
        channel_topic = request.POST.get("q3")
        
        channel = feedparser.parse(requests.get(channel_rss_feed, headers={"User-Agent": "Mozilla/5.0"}).content)
        save_new_article(channel, channel_name, channel_topic)

        if not Channel.objects.filter(rss_feed=channel_rss_feed).exists():
            channel = Channel(rss_feed=channel_rss_feed, name=channel_name, topic=channel_topic)
            channel.save()

        return HttpResponseRedirect(reverse("aggregators:index"))

    return render(request, 'aggregators/add_rss.html')



