class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        self._articles = []
        Magazine._all.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def add_contributor(self, author, article):
        self._contributors.append(author)
        self._articles.append(article)

    def contributors(self):
        return self._contributors

    def article_titles(self):
        return [article.title() for article in self._articles]

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all:
            if magazine.name() == name:
                return magazine

    def contributing_authors(self):
        author_count = {}
        for author in self._contributors:
            author_count[author] = author_count.get(author, 0) + 1
        print("Author Count:", author_count) 
        return [author for author, count in author_count.items() if count > 2]
