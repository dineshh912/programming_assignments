import numpy as np

class Tree_node:
    """
    Data structure for nodes in the decision-tree
    """
    def __init__(self,):
        self.feature = None # index of the selected feature (for non-leaf node)
        self.label = None # class label (for leaf node)
        self.left_child = None # left child node
        self.right_child = None # right child node

class Decision_tree:
    """
    Decision tree with binary features
    """
    def __init__(self, min_entropy):
        self.min_entropy = min_entropy
        self.root = None

    def fit(self,train_x,train_y):
        # construct the decision-tree with recursion
        self.root = self.generate_tree(train_x, train_y, self.min_entropy)

    def predict(self,test_x):
        # iterate through all samples
        prediction = np.zeros([len(test_x),]).astype('int') # placeholder
        for i in range(len(test_x)):
            # traverse the decision-tree based on the features of the current sample
            current_node = self.root
            while current_node.label == None:
                if test_x[i][current_node.feature] == 0:
                    current_node = current_node.left_child
                else:
                    current_node = current_node.right_child
            prediction[i] = current_node.label

        return prediction

    def generate_tree(self,data,label, min_entropy):
        # initialize the current tree node
        cur_node = Tree_node()
        left_node_data, left_label, right_node_data, right_label = [], [], [], []

        # compute the node entropy
        node_entropy = self.compute_node_entropy(label)

        # determine if the current node is a leaf node
        if node_entropy < self.min_entropy:
            # determine the class label for leaf node
            """
            1. bincount function counts the number of occurrences of each unique value in an array of non-negative ints.
            2. freq is an array with length of the number of unique labels
            3. label is an array of ints
            """
            freq = np.bincount(label)
            # find the most frequent label
            max_freq = np.argmax(freq)
            # assign most frequent label as nodes label
            cur_node.label = max_freq
            return cur_node

        # select the feature that will best split the current non-leaf node
        selected_feature = self.select_feature(data,label)
        cur_node.feature = selected_feature

        # split the data based on the selected feature and start the next level of recursion
        for i in range(len(data)):
            if data[i][selected_feature] == 0:
                left_node_data.append(data[i])
                left_label.append(label[i])
            else:
                right_node_data.append(data[i])
                right_label.append(label[i])
        # recursively generate the left and right child nodes
        cur_node.left_child = self.generate_tree(np.array(left_node_data),
                                                np.array(left_label), 
                                                min_entropy)
        cur_node.right_child = self.generate_tree(np.array(right_node_data),
                                                np.array(right_label),
                                                min_entropy)

        return cur_node

    def select_feature(self,data,label):
        # iterate through all features and compute their corresponding entropy
        best_feat = 0
        current_entropy = []
        for i in range(len(data[0])):
            left_y = []
            right_y = []
            # compute the entropy of splitting based on the selected features
            for j in range(len(data[:, i])):
                if data[j][i] == best_feat:
                    left_y.append(label[j])
                else:
                    right_y.append(label[j])
            # compute the entropy of the current feature
            current_entropy.append(self.compute_split_entropy(left_y, right_y))

        # select the feature with minimum entropy
        best_feat = np.argmin(current_entropy)
        return best_feat

    def compute_split_entropy(self,left_y,right_y):
        # compute the entropy of a potential split, left_y and right_y are labels for the two branches

        left_prop = len(left_y)/(len(left_y) + len(right_y))
        right_prop = len(right_y)/(len(left_y) + len(right_y))

        node_entropy_left = left_prop * self.compute_node_entropy(left_y)
        node_entropy_right = right_prop * self.compute_node_entropy(right_y)

        split_entropy = node_entropy_left + node_entropy_right

        return split_entropy

    def compute_node_entropy(self,label):
        # compute the entropy of a tree node (add 1e-15 inside the log2 when computing the entropy to prevent numerical issue)
        label = np.array(label)
        classes = np.unique(label)
        node_entropy = 0
        for i in classes:
            prop = len(label[np.where(label == i)])/(len(label))
            node_entropy += -prop * np.log2(prop + 1e-15)

        return node_entropy
