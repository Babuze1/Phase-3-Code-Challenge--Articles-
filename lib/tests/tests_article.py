import sys
sys.path.append("..")

from Author import Author
from Magazine import Magazine

def test_article_title():
    author1 = Author("John Doe")
    magazine1 = Magazine("Tech Today", "Technology")
    article1 = author1.add_article(magazine1, "Python Programming")
    assert article1.title() == "Python Programming"

def test_article_author():
    author1 = Author("John Doe")
    magazine1 = Magazine("Tech Today", "Technology")
    article1 = author1.add_article(magazine1, "Python Programming")
    assert article1.author() == author1

def test_article_magazine():
    author1 = Author("John Doe")
    magazine1 = Magazine("Tech Today", "Technology")
    article1 = author1.add_article(magazine1, "Python Programming")
    assert article1.magazine() == magazine1

if __name__ == "__main__":
    test_article_title()
    test_article_author()
    test_article_magazine()
    print("All Article tests passed!")