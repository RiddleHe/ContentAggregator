# Content Aggregator
A web app that automatically gets articles from users' favorite websites and updates them with just one click.
## Features
- Scrapes most recent articles directly from users' chosen websites and add them to feeds in the main page and to their respective topic pages.

    ![index page](static/add_rss.png)

- Automatically generates topics in the header section, the headline, and individual topic pages based on articles added to the app.

    ![index page](static/index.png)

- Updates articles based on how recent they are on all pages with one click.

## Installment
To begin with, clone the project.
```
git clone https://github.com/RiddleHe/content_aggregator
```
After that, in the main directory, set up and activate a virtual environment to harbor the dependencies.
```
python3 -m venv ll_env
source ll_env/bin/activate
```
When the virtual environment is set up, install the dependencies.
```
pip install Django, feedparser, requests, django-bootstrap-v5
```
Then, in the main directory, run the server to load the web application, and now you can interact with it.
```
quiz % python3 manage.py runserver
```
## Technologies
*Using Python, Django, HTML, feedparser, requests, and Bootstrap*
- Built an input form that works with POST request data to activate feedparser and requests, parsing RSS feed from target website and accessing information of the website and individual articles.

    ```
    def add_rss(request):
    """Add RSS reed user entered to database"""

    if request.method == "POST":
        
        channel_rss_feed = "{feed}".format(feed=request.POST.get("q1"))
        channel_name = request.POST.get("q2")
        channel_topic = request.POST.get("q3")
        
        channel = feedparser.parse(requests.get(channel_rss_feed, headers={"User-Agent": "Mozilla/5.0"}).content)
        save_new_article(channel, channel_name, channel_topic)
    ```
- Used class composition techniques to add and update new articles in the database.

    ``` 
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
    ```

- Applied conditionals in HTML files to generate non-redundant links in the header section and individual topic pages.

    ```
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
    ```
