class Article:
    def __init__(self, articleName):
        self.articleName = articleName

    def name(self):
        return self.articleName

articleOne = Article("She make it clap")

print(articleOne.name())
