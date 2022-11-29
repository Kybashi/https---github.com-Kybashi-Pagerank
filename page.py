class Page():
    def __init__(self, ausgehendeLinks, eingehendeLinks, url, pageRank):
        self.ausgehendeLinks = ausgehendeLinks
        self.eingehendeLinks = eingehendeLinks
        self.url = url
        self.pageRank = pageRank
