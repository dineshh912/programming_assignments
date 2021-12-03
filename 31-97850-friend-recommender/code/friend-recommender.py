#!/usr/bin/env python3

class SocialNetwork:

    def __init__(self):
        '''Constructor; initialize an empty social network
        '''
        # initializing user dict
        self.users = {}

    def list_users(self):
        '''List all users in the network

        Returns:
            [str]: A list of usernames
        '''
        # retutn  list of users in a list
        return list(self.users.keys())

    def add_user(self, user):
        '''Add a user to the network

        This user will have no friends initially.

        Arguments:
            user (str): The username of the new user

        Returns:
            None
        '''
        # intitalize dict for user
        self.users[user] = []
        

    def add_friend(self, user, friend):
        '''Adds a friend to a user

        Note that "friends" are one-directional - this is the equivalent of
        "following" someone.

        If either the user or the friend is not a user in the network, they
        should be added to the network.

        Arguments:
            user (str): The username of the follower
            friend (str): The username of the user being followed

        Returns:
            None
        '''
        # add friends into the dict of user
        if user in self.users:
            self.users[user].append(friend)

    def get_friends(self, user):
        '''Get the friends of a user

        Arguments:
            user (str): The username of the user whose friends to return

        Returns:
            [str]: The list of usernames of the user's friends

        '''
        # get friends of the user and return as list
        return self.users[user]

    def suggest_friend(self, user):
        '''Suggest a friend to the user

        See project specifications for details on this algorithm.

        Arguments:
            user (str): The username of the user to find a friend for

        Returns:
            str: The username of a new candidate friend for the user
        '''
        # this will store all the friends of the user because we can't suggest person who is already a friend
        user_friends = [] 
        # variable to store jaccard index
        jaccard_index = {}
        # Below variables store count of the mutual and total friends
        # which needed to calculate jaccard index
        mutual_friends = total_friends = 0

        # get all the friends of the user and save it user_friends list
        for friend in self.get_friends(user):
            user_friends.append(friend)

        # loop through the network
        for person in self.users.keys():
            # we already saved the friends of the user in user_friends list
            if person != user:
                different_person_friends = self.get_friends(person)
            
            # check the friends are mutual
            for different_person in different_person_friends:
                # checking the other person friends are matching with user friend
                if different_person in user_friends:
                    mutual_friends += 1
                total_friends += 1
            # calculate the jaccard index
            total_friends += len(user_friends) # add user friends to total friends
            jaccard_index[person] = mutual_friends / total_friends # adding jaccard index to dict

        # find people with highest jaccard index
        max_jaccard_index_person = max(jaccard_index, key=jaccard_index.get)

        # Friends of highst jaccard index person are similar friend list
        similar_friends = self.get_friends(max_jaccard_index_person)

        suggested_friend = []
        # from the similar friends list get suggestion of friends
        for friend in similar_friends:
            if friend not in user_friends and friend != user:
                suggested_friend.append(friend)
        
        suggested_friend_dict = {}
        # if the user is friends with everyone then we can't suggest anyone
        if len(suggested_friend) == 0:
            return "No Suggestion"
        else:
            # in the list of suggested friends and their friends count
            # this step if more than one person to suggest then we will get the person with max friends count
            for friend in suggested_friend:
                suggested_friend_dict[friend] = len(self.get_friends(friend))

        recommnation_friend = max(suggested_friend_dict, key=suggested_friend_dict.get)

        return recommnation_friend

    def to_dot(self):
        result = []
        result.append('digraph {')
        result.append('    layout=neato')
        result.append('    overlap=scalexy')
        for user in self.list_users():
            for friend in self.get_friends(user):
                result.append('    "{}" -> "{}"'.format(user, friend))
        result.append('}')
        return '\n'.join(result)


def create_network_from_file(filename):
    '''Create a SocialNetwork from a saved file

    Arguments:
        filename (str): The name of the network file

    Returns:
        SocialNetwork: The SocialNetwork described by the file
    '''
    network = SocialNetwork()
    with open(filename) as fd:
        for line in fd.readlines():
            line = line.strip()
            users = line.split()
            network.add_user(users[0])
            for friend in users[1:]:
                network.add_friend(users[0], friend)
    return network


def main():
    # network = create_network_from_file('simple.network')
    network = create_network_from_file('intermediate.network')
    # network = create_network_from_file('twitter.network')
    print(network.to_dot())
    print(network.suggest_friend('francis'))
    # Francis not available in twitter network so tested with LAPhil
    # rint(network.suggest_friend('LAPhil'))


if __name__ == '__main__':
    main()
