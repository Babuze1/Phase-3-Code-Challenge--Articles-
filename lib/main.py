from Author import Author
from Article import Article
from Magazine import Magazine


author1 = Author("Emmanuel Mwanzia")
author2 = Author("Victoria Blessing")

magazine1 = Magazine("Twin Turbos", "Nitrous")
magazine2 = Magazine("Cars", "Engines")


author1.add_article(magazine1, "The Future of Motor vehicle modifications")
author1.add_article(magazine2, "Advancements in Engine Computing")
author2.add_article(magazine1, "Machine Using Techniques")


print(author1.articles()[0].title())  
print(magazine1.contributors()[0].name()) 
print(magazine1.article_titles())  
print(Magazine.find_by_name("Twin Turbos").category()) 
print(magazine1.contributing_authors()[0].name())  
