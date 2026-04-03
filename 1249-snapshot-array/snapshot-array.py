class SnapshotArray:

    def __init__(self, length: int):
        self.ls = [[(0, 0)] for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.ls[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1

        return (self.snap_id - 1)

    def get(self, index: int, snap_id: int) -> int:
        ls1 = self.ls[index]
        low = 0
        high = len(ls1) - 1
        result = -1

        while (low <= high):
            mid = low + (high - low) // 2

            if (ls1[mid][0] <= snap_id):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ls1[result][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)