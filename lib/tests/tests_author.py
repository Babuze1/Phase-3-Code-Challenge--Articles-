import sys
sys.path.append("..")

from Author import Author
from Magazine import Magazine

def test_author_name():
    author1 = Author("John Doe")
    assert author1.name == "John Doe"

def test_author_articles():
    author1 = Author("John Doe")
    assert len(author1.articles()) == 0

def test_author_magazines():
    author1 = Author("John Doe")
    magazine1 = Magazine("Tech Today", "Technology")
    author1.add_article(magazine1, "Python Programming")
    assert len(author1.magazines()) == 1
    assert author1.magazines()[0] == magazine1

def test_author_topic_areas():
    author1 = Author("John Doe")
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Fashion Weekly", "Fashion")
    author1.add_article(magazine1, "Python Programming")
    author1.add_article(magazine2, "Summer Fashion Trends")
    assert author1.topic_areas() == ["Technology", "Fashion"]

if __name__ == "__main__":
    test_author_name()
    test_author_articles()
    test_author_magazines()
    test_author_topic_areas()
    print("All Author tests passed!")