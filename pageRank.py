from page import Page

class PageRank():

    def CalculatePageRankByIteration(pageList, iteration):
        for i in range(0, iteration):
            
        
    def calculatePageRank(pageList:Page):
        otherPr = 0
        for page in pageList:
            for links in page.eingehendeLinks:
                otherPr +=(links.pageRank / len(page.ausgehendeLinks))
            page.pageRank = ((1 - 0.85) + 0.85 * otherPr)
    
