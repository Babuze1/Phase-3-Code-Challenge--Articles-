from Author import Author
from Magazine import Magazine

def main():
    # Create authors
    author1 = Author("Author 1")
    author2 = Author("Author 2")

    # Create magazines
    magazine1 = Magazine("Magazine A", "Category A")
    magazine2 = Magazine("Magazine B", "Category B")

    # Add articles
    author1.add_article(magazine1, "Article 1 by Author 1")
    author1.add_article(magazine2, "Article 2 by Author 1")
    author2.add_article(magazine1, "Article 1 by Author 2")

    # Print author information
    print("Author 1:")
    print("Name:", author1.name())
    print("Articles:", [article.title() for article in author1.articles()])
    print("Magazines:", [magazine.name() for magazine in author1.magazines()])
    print("Topic Areas:", author1.topic_areas())

    # Print magazine information
    print("\nMagazine A:")
    print("Name:", magazine1.name())
    print("Category:", magazine1.category())
    print("Contributors:", [contributor.name() for contributor in magazine1.contributors()])

if __name__ == "__main__":
    main()
