from Article import Article

class Author:
    _all = []

    def __init__(self, name):
        self._name = name
        self._all.append(self)
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        magazine_list = []
        for article in self._articles:
            if article.magazine() not in magazine_list:
                magazine_list.append(article.magazine())
        return magazine_list

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        categories = set()
        for magazine in self.magazines():
            categories.add(magazine.category())
        return list(categories)
