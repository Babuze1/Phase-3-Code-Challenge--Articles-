from Author import Author
from Magazine import Magazine


def test_author_methods():
    author1 = Author("John Doe")
    assert author1.name == "John Doe"
    assert len(author1.articles()) == 0

def test_magazine_methods():
    magazine1 = Magazine("Tech Today", "Technology")
    assert magazine1.name() == "Tech Today"
    assert magazine1.category() == "Technology"

def test_article_methods():
    author1 = Author("John Doe")
    magazine1 = Magazine("Tech Today", "Technology")
    article1 = author1.add_article(magazine1, "Python Programming")
    assert article1.title() == "Python Programming"
    assert article1.author() == author1
    assert article1.magazine() == magazine1


if __name__ == "__main__":
    test_author_methods()
    test_magazine_methods()
    test_article_methods()
    print("All tests passed!")