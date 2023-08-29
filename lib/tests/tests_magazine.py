import sys
sys.path.append("..")

from Author import Author
from Magazine import Magazine

def test_magazine_name():
    magazine1 = Magazine("Tech Today", "Technology")
    assert magazine1.name() == "Tech Today"

def test_magazine_category():
    magazine1 = Magazine("Tech Today", "Technology")
    assert magazine1.category() == "Technology"

def test_magazine_contributors():
    author1 = Author("John Doe")
    magazine1 = Magazine("Tech Today", "Technology")
    author1.add_article(magazine1, "Python Programming")
    assert len(magazine1.contributors()) == 1
    assert magazine1.contributors()[0] == author1

def test_magazine_find_by_name():
    magazine1 = Magazine("Tech Today", "Technology")
    found_magazine = Magazine.find_by_name("Tech Today")
    assert found_magazine == magazine1

def test_magazine_article_titles():
    magazine1 = Magazine("Tech Today", "Technology")
    author1 = Author("John Doe")
    author1.add_article(magazine1, "Python Programming")
    author1.add_article(magazine1, "Data Science Essentials")
    assert magazine1.article_titles() == ["Python Programming", "Data Science Essentials"]

def test_magazine_contributing_authors():
    magazine1 = Magazine("Tech Today", "Technology")
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    author1.add_article(magazine1, "Python Programming")
    author1.add_article(magazine1, "Data Science Essentials")
    author2.add_article(magazine1, "Web Development Trends")
    assert magazine1.contributing_authors() == [author1]

if __name__ == "__main__":
    test_magazine_name()
    test_magazine_category()
    test_magazine_contributors()
    test_magazine_find_by_name()
    test_magazine_article_titles()
    test_magazine_contributing_authors()
    print("All Magazine tests passed!")