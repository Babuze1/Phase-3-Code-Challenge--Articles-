from classes.Author import Author
from classes.Magazine import Magazine
from classes.Article import Article

class Article:  # Your new Article class
    def __init__(self, articleName):
        self.articleName = articleName

    def name(self):
        return self.articleName

def main():
    # Create authors
    author1 = Author("Author 1")
    author2 = Author("Author 2")
    author3 = Author("Author 3")

    # Create magazines
    magazine1 = Magazine("Magazine A", "Category A")
    magazine2 = Magazine("Magazine B", "Category B")
    magazine3 = Magazine("Magazine C", "Category A")

    # Create articles
    article1 = Article(author1, magazine1, "Article Title 1")
    article2 = Article(author1, magazine2, "Article Title 2")
    article3 = Article(author2, magazine1, "Article Title 3")
    article4 = Article(author3, magazine3, "Article Title 4")
 
    
    print("Authors:")
    print(Author.all())
    print(author1.articles())
    print(author1.magazines())
    print(author1.topic_areas())

    print("\nMagazines:")
    print(Magazine.all())
    print(magazine1.contributors())
    print(magazine1.article_titles())
    print(magazine1.contributing_authors())

    print("\nArticles:")
    print(Article.all())
    print(article1.title())
    print(article1.author().name())
    print(article1.magazine().name())
    print(article1.name())  

if __name__ == "__main__":
    main()
