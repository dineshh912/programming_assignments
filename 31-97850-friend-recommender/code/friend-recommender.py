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
        # saving list of users
        list_of_users = []
        # for each user in the network
        for user in self.users:
            # add the user to the list of users
            list_of_users.append(user)
        return list_of_users

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
        self.users[user].append(friend)

    def get_friends(self, user):
        '''Get the friends of a user

        Arguments:
            user (str): The username of the user whose friends to return

        Returns:
            [str]: The list of usernames of the user's friends

        '''
        # get friends of the user and save as a list
        list_of_friends = self.users.get(user, [])
        return list_of_friends

    def suggest_friend(self, user):
        '''Suggest a friend to the user

        See project specifications for details on this algorithm.

        Arguments:
            user (str): The username of the user to find a friend for

        Returns:
            str: The username of a new candidate friend for the user
        '''
        # calculate the jaccard index
        jaccard_index = {}
        dict_of_different_friends = {}
        for others, others_friends in self.users.items():
            if others != user:
                common_friends = 0
                total_people_met = 0
                num_of_different_friends = 0
                for other_friend in others_friends:
                    if other_friend in self.users[user]:
                        common_friends += 1
                    else:
                        num_of_different_friends += 1
                    total_people_met += 1
                dict_of_different_friends[others] = num_of_different_friends
                total_people_met += len(self.users[user]) - common_friends
                jaccard_index[others] = common_friends/total_people_met

        # Get the user with high jaccard index
        highest_ji = 0
        potential_friends = []
        for person, ji_value in jaccard_index.items():
            if ji_value > highest_ji:
                potential_friends = [person]
                highest_ji = ji_value
            elif ji_value == highest_ji:
                potential_friends.append(person)

        #find person with highest number of different friends these highest jaccard people have with user
        potential_friend = "No friends recommended for now!!"
        highest_diff_friends = 0
        for p_friend in potential_friends:
            if dict_of_different_friends.get(p_friend, 0) > highest_diff_friends:
                potential_friend = p_friend
                highest_diff_friends = dict_of_different_friends.get(p_friend)
        return potential_friend


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
    print(network.to_dot())
    print(network.suggest_friend('erin'))


if __name__ == '__main__':
    main()
