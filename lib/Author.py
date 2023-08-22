import Article
class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        magazine_set = set()
        for article in self._articles:
            magazine_set.add(article.magazine())
        return list(magazine_set)

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine.add_contributor(self, article)

    def topic_areas(self):
        topics = set()
        for article in self._articles:
            topics.add(article.magazine().category())
        return list(topics)
