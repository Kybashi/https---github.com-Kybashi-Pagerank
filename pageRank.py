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