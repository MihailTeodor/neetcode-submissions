class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_values_stack:
            self.min_values_stack.append(val)
        else: 
            self.min_values_stack.append(
                min(
                    val, 
                    self.min_values_stack[-1])
                )
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_values_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_values_stack[-1]
        
