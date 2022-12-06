class Page():
    def __init__(self, url, pageRank):
        self.ausgehendeLinks = []
        self.eingehendeLinks = []
        self.url = url
        self.pageRank = pageRank
