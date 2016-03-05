class User:
    trips = []
    friends = []

    def isFriend(self, user):
        return self.friends.contains(user)

    def addFriend(self, user):
        self.friends.append(user)

    def addTrip(self, trip):
        self.trips.append(trip)
