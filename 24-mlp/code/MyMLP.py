import numpy as np

def process_data(data,mean=None,std=None):
    # normalize the data to have zero mean and unit variance (add 1e-15 to std to avoid numerical issue)
    if mean is not None:
        # directly use the mean and std precomputed from the training data
        data = (data - mean) / (std + 1e-15)
        return data
    else:
        # compute the mean and std based on the training data
        mean, std = np.mean(data, axis=0), np.std(data, axis=0) # placeholder
        data = (data - mean) / (std + 1e-15)
        return data, mean, std

def process_label(label):
    # convert the labels into one-hot vector for training
    one_hot = np.zeros([len(label),10])
    # numpy zero's function to create array of 0's of the required size(10, 10)
    # Replacing 0 with 1 at required location
    for i in range(len(label)):
        one_hot[i][label[i]] = 1

    return one_hot

def tanh(x):
    # implement the hyperbolic tangent activation function for hidden layer
    # You may receive some warning messages from Numpy. No worries, they should not affect your final results
    ''' f(x) = (e^x - e^-x) / (e^x + e^-x); derivative of tanh: f'(x) = (1-g(x^2)'''
    # (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))
    # 1 - tanh(x) * tanh(x) ; 1- np.power(tanh(x), 2)
    f_x = 2 / (1 + np.exp(-2 * x)) - 1
    return f_x

def dtanh(x):
    # implement the hyperbolic deravative tangent activation function for backprobagation
    f_x = 1- np.power(tanh(x), 2)
    return f_x


def softmax(x):
    # implement the softmax activation function for output layer
    f_x = np.exp(x) / np.sum(np.exp(x)) 
    return f_x


def cross_entropy_loss(y, yhat):
    '''
        yHat  = predicted value
        y =  actual label
    '''
    if y == 1:
      return -np.log(yhat)
    else:
      return -np.log(1 - yhat)


class MLP:
    def __init__(self,num_hid):
        # initialize the weights
        self.weight_1 = np.random.random([64,num_hid])
        self.bias_1 = np.random.random([1,num_hid])
        self.weight_2 = np.random.random([num_hid,10])
        self.bias_2 = np.random.random([1,10])

    def fit(self,train_x, train_y, valid_x, valid_y):
        # learning rate
        lr = 5e-3
        # counter for recording the number of epochs without improvement
        count = 0
        best_valid_acc = 0

        """
        Stop the training if there is no improvment over the best validation accuracy for more than 50 iterations
        """
        while count<=50:
            # training with all samples (full-batch gradient descents)
            # implement the forward pass (from inputs to predictions)
            # hidden Layer
            hidden_output = self.get_hidden(train_x)
            y_pred = self.predict(train_x)
            y_label = process_label(y_pred)

            # implement the backward pass (backpropagation)
            # compute the gradients w.r.t. different parameters
            label_diff = train_y - y_label

            update_weight_2 = lr * np.dot(hidden_output.T, label_diff)
            update_bias_2 = lr * np.sum(label_diff, axis=0)

            inner = (np.dot(label_diff, self.weight_2.T))
            dtz = dtanh(hidden_output)
            coeffs = (inner * dtz)

            update_weight_1 = lr * np.dot(train_x.T, coeffs)
            update_bias_1 = lr * np.sum(coeffs, axis=0)

            #update the parameters based on sum of gradients for all training samples
            self.weight_1 += update_weight_1
            self.bias_1 += update_bias_1
            self.weight_2 += update_weight_2
            self.bias_2 += update_bias_2

            # evaluate on validation data
            predictions = self.predict(valid_x)
            valid_acc = np.count_nonzero(predictions.reshape(-1)==valid_y.reshape(-1))/len(valid_x)

            # compare the current validation accuracy with the best one
            if valid_acc>best_valid_acc:
                best_valid_acc = valid_acc
                count = 0
            else:
                count += 1

        return best_valid_acc

    def predict(self,x):
        # generate the predicted probability of different classes
        hidden_op = self.get_hidden(x)

        # convert class probability to predicted labels
        y = softmax(np.dot(hidden_op, self.weight_2) + self.bias_2)
        y_prob = np.argmax(y, axis=1)
        # y = np.zeros([len(x),]).astype('int') # placeholder

        return y_prob

    def get_hidden(self,x):
        # extract the intermediate features computed at the hidden layers (after applying activation function)
        '''
            hidden_input = x.dot(self.weight_1) + self.bias_1
            hidden_ouput = tanh(hidden_input)
        '''
        z = tanh(np.dot(x, self.weight_1) + self.bias_1)
        return z

    def params(self):
        return self.weight_1, self.bias_1, self.weight_2, self.bias_2
