from Author import Author
from Article import Article
from Magazine import Magazine


author1 = Author("John Doe")
author2 = Author("Jane Smith")


magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Fashion Weekly", "Fashion")


author1.add_article(magazine1, "Python Programming")
author1.add_article(magazine2, "Summer Fashion Trends")
author2.add_article(magazine1, "Data Science Essentials")
author2.add_article(magazine1, "Web Development Trends")

# Test methods
print("Authors:")
print(author1.name)
print(author2.name)
print()

print("Magazines:")
print(magazine1.name())
print(magazine2.name())
print()

print("Articles:")
for article in Article.all():
    print(f"{article.title()} - {article.author().name} - {article.magazine().name()}")

print()

print("Contributors for Tech Today:")
for contributor in magazine1.contributors():
    print(contributor.name)
print()

print("Find magazine by name:")
found_magazine = Magazine.find_by_name("Tech Today")
print(found_magazine.name())
print()

print("Article titles for Tech Today:")
print(found_magazine.article_titles())
print()

print("Contributing authors for Tech Today:")
for author in found_magazine.contributing_authors():
    print(author.name)
print()

print("Topic areas for authors:")
print(author1.topic_areas())
print(author2.topic_areas())
