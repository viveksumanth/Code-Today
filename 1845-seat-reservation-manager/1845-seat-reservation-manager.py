class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in (range(1, n+1))]
        
    def reserve(self) -> int:
        use = heapq.heappop(self.seats)
        return use
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)