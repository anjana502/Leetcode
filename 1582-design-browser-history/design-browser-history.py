class TreeNode:
    def __init__(self, val = ""):
        self.val = val
        self.next = None
        self.prev = None
    
class BrowserHistory:

    def __init__(self, homepage: str):
        self.front = TreeNode()
        self.rear = TreeNode()
        self.front.next = self.rear
        self.rear.prev = self.front
        self.curr = self.front

        self.visit(homepage)

    def visit(self, url: str) -> None:
        new_node = TreeNode(url)
        next1 = self.curr.next
        new_node.next = next1
        self.curr.next = new_node
        new_node.prev = self.curr
        next1.prev = new_node
        self.curr = new_node

        self.curr.next = self.rear
        self.rear.prev = self.curr

    def back(self, steps: int) -> str:
        while (steps > 0 and self.curr.prev != self.front):
            self.curr = self.curr.prev
            steps -= 1
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        while (steps > 0 and self.curr.next != self.rear):
            self.curr = self.curr.next
            steps -= 1
        
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)