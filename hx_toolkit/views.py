from django.template.loader import render_to_string


def render_article_html(article):
    article_string = render_to_string('message.html', {'article': article})
    return article_string
