class NList:
    """Data structure design
    
    O(n) space complexity.

    O(1) time complexity.
    """
    def __init__(self):
        self.content = []
        self.count = 0
        self.max = None
        self.min = None
        self.avg = None
    
    def insert(self, key: int):
        self.content.append(key)
        self.count += 1

        self._updateMaxMin(key)
        self._updateAvg(key)

    def getMax(self) -> int:
        return self.max
    
    def getMin(self) -> int:
        return self.min
    
    def getAvg(self) -> int:
        return self.avg
    
    def _updateMaxMin(self, key: int):
        if self.max is None and self.min is None:
            self.max = key
            self.min = key
        else:
            if key > self.max:
                self.max = key
            
            if key < self.min:
                self.min = key
    
    def _updateAvg(self, key: int):
        if self.avg is None:
            self.avg = key
        else:
            total = self.count * self.avg + key
            self.avg = total / count