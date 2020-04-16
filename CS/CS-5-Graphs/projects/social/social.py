from itertools import combinations
import random
from util import Queue
#random.seed(6)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f'Bob_{i+1}')

        # Create friendships
        possible_friendships = list(combinations(range(1, self.last_id + 1), 2))

        # shuffle all possible friendships
        random.shuffle(possible_friendships)

        # create first X pairs, X is total // 2
        total_pairs = num_users * avg_friendships // 2
        for f in possible_friendships[:total_pairs]:
            self.add_friendship(f[0], f[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        q = Queue()
        # !!!! IMPLEMENT ME
        q.enqueue(user_id)
        visited[user_id] = [user_id] # initialize 1st item
        while q.size() > 0:
            parent = q.dequeue()
            children = self.friendships[parent]
            #if parent not in visited.keys():
            #    visited[parent] = children
            for child in children:
                if child not in visited.keys():
                    visited[child] = visited[parent] + [child]
                    q.enqueue(child)

        return visited

# QUESTIONS:
# 1. To create 100 users with an average of 10 friends each, how many times would you need to call add_friendship()? Why?
#
#########
#  500  #
#########
#
# add_friendship() is called in the populate_graph function:
#
#  total_pairs = num_users * avg_friendships // 2
#        for f in possible_friendships[:total_pairs]:
#        self.add_friendship(f[0], f[1])
#
# As we can see it gets called as many times as the number of total_pairs above
# i.e. num_users * avg_friendships // 2 = 100 * 10 / 2 = 500
#
#
# 2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?
#
###################################
#     Very nearly all of them     #
###################################
#
# There doesn't seem to be an ovious objective way to solve this
# (though I'm sure statisticians have figured something out by now)
# So I will do it the experimental way. As ratio of avg_friends
# to number of users increases, the average lenth of the connections
# rapidly approaches the established average number of friends
#
# I've observed after about 9 connections, everyone is connected to everyone
# else in some way with the mean number of contacts away being ~ 4 connections


if __name__ == '__main__':
    print('be patient, this will take about 10 seconds')
    sg = SocialGraph()
    num_users = 1000
    avg_friends = 20
    x = []
    y = []
    for j in range(1, avg_friends + 1):
        sg.populate_graph(num_users, j)
        total_connections = 0
        for i in range(1, avg_friends + 1):
            connections = sg.get_all_social_paths(i)
            total_connections += len(connections)
        x.append(j)
        y.append(total_connections/avg_friends)
        if j == avg_friends:
            degrees_away = sum([len(v) for _,v in connections.items()])/len(connections)
            print(f'average distance away with {num_users} with about {avg_friends} friends apiece is ~ {degrees_away} people')


    import matplotlib.pyplot as plt
    plt.plot(x,y)
    plt.xlabel('avg number of connections per friend')
    plt.ylabel('average number of connections\nin extended social network')
    plt.title('The fraction of people who know eachother rapidly approaches the\n total number of people in the network as average connection size grows')
    plt.show()



    #print(total_connections/num_users)
    #sg = SocialGraph()
    #sg.populate_graph(10, 2)
    #print(sg.friendships)
    #connections = sg.get_all_social_paths(1)
    #print(connections)
