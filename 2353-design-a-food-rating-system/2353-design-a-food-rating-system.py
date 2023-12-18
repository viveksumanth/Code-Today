class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisinesToFood = defaultdict(list)
        self.foodToCuisine = dict()
        self.foodToRating = dict()

        for i in range(0,len(foods)):
            cuisine = cuisines[i]
            food = foods[i]
            rating = ratings[i]

            self.foodToCuisine[food] = cuisine
            self.cuisinesToFood[cuisine].append((-1*rating, food))
            self.foodToRating[food] = -1*rating

        for each in self.cuisinesToFood:
            heapq.heapify(self.cuisinesToFood[each])

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodToCuisine[food]
        self.foodToRating[food] = -1*newRating
        heapq.heappush(self.cuisinesToFood[cuisine], (-1*newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highestRated, food = self.cuisinesToFood[cuisine][0]

        while(highestRated != self.foodToRating[food]):
            heapq.heappop(self.cuisinesToFood[cuisine])
            highestRated, food = self.cuisinesToFood[cuisine][0]

        return self.cuisinesToFood[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)