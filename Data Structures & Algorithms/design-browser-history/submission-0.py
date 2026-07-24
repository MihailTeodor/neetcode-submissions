class ListNode:

    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentPage = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        newPage = ListNode(url)

        self.currentPage.next = newPage
        newPage.prev = self.currentPage

        self.currentPage = newPage
        

    def back(self, steps: int) -> str:
        while self.currentPage.prev and steps > 0:
            self.currentPage = self.currentPage.prev
            steps -= 1

        return self.currentPage.url
        

    def forward(self, steps: int) -> str:
        while self.currentPage.next and steps > 0:
            self.currentPage = self.currentPage.next
            steps -= 1

        return self.currentPage.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)