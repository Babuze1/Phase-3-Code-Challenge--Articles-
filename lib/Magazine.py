from Article import Article

class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._all.append(self)
        self._articles = []

    def name(self):
        return self._name

    def category(self):
        return self._category

    @classmethod
    def all(cls):
        return cls._all

    def contributors(self):
        contributor_list = []
        for article in Article.all():
            if article.magazine() == self and article.author() not in contributor_list:
                contributor_list.append(article.author())
        return contributor_list

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all:
            if magazine.name() == name:
                return magazine

    def article_titles(self):
        titles = []
        for article in self._articles:
            titles.append(article.title())
        return titles

