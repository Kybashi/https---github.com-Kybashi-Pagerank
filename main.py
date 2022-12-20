from pageRank import PageRank
import page



a1 = page.Page("google.de", 1)
b1 = page.Page("wikipedia.de", 1)
c1 = page.Page("youtube.de", 1)

a1.ausgehendeLinks = [b1, c1]
a1.eingehendeLinks = [c1]

b1.ausgehendeLinks = [c1]
b1.eingehendeLinks = [a1]

c1.ausgehendeLinks = [a1]
c1.eingehendeLinks = [b1, a1]

pageList = [a1,b1,c1]

pr = PageRank()

pr.calculatePageRankByIteration(pageList, 15, 0.85)