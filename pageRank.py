from page import Page

class PageRank():

    def calculatePageRankByIteration(self, pageList, iterations, dampFactor):
        for i in range(iterations):
            newPageRanks = []
            print()
            print("Iteration: ", str(i+1))
            for page in pageList:
                
                pageRankSum = 0
                for eingehenderLink in page.eingehendeLinks:
                    pageRankSum = pageRankSum + eingehenderLink.pageRank/len(eingehenderLink.ausgehendeLinks)   
                pagerank = ((1 - dampFactor) + dampFactor * (pageRankSum))
                newPageRanks.append(pagerank)
            count = 0
            for page in pageList:
                page.pageRank = newPageRanks[count]
                count += 1
                print(page.url+": "+str(page.pageRank))

def test_pagerank():
    a1 = Page("google.de", 1)
    b1 = Page("wikipedia.de", 1)
    c1 = Page("youtube.de", 1)
        
    a1.ausgehendeLinks = [b1, c1]
    a1.eingehendeLinks = [c1]

    b1.ausgehendeLinks = [c1]
    b1.eingehendeLinks = [a1]

    c1.ausgehendeLinks = [a1]
    c1.eingehendeLinks = [b1, a1]

    pageList = [a1,b1,c1]

    vorherA1 = a1.pageRank
    vorherB1 = b1.pageRank
    vorherC1 = c1.pageRank
    
    pr = PageRank()

    pr.calculatePageRankByIteration(pageList, 15, 0.85)

    assert a1.pageRank != vorherA1
    assert a1.pageRank == 1.1636117942862079
    assert b1.pageRank != vorherB1
    assert b1.pageRank == 0.6442449692660287
    assert c1.pageRank != vorherC1
    assert c1.pageRank == 1.1921432364477629
test_pagerank()