class Magazine:
    _magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        Magazine._magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    @classmethod
    def all(cls):
        return cls._magazines

    def add_contributor(self, author):
        if author not in self._contributors:
            self._contributors.append(author)

    def contributors(self):
        return self._contributors

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._magazines:
            if magazine.name() == name:
                return magazine

    @classmethod
    def article_titles(cls):
        titles = []
        for magazine in cls._magazines:
            titles.extend(article.title() for article in magazine.articles())
        return titles

    def contributing_authors(self):
        return [author for author in self._contributors if len(author.articles()) > 2]
