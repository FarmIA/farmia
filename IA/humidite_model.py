"""
Trains a logistic regression model to predict whether a plant should be watered based on its type and the humidity level.
"""

import numpy as np
import copy
import matplotlib.pyplot as plt

def arrose_easy(plante, humidité):
    if humidité < 50:
        #print("J'arrose la plante " + str(plante))
        return 1
    else:
        #print("Je n'arrose pas la plante " + str(plante))
        return 0

def arrose_hard(plante, humidité):
    if plante < 3:
        if humidité < 50:
            #print("J'arrose la plante " + str(plante))
            return 1
        else:
            #print("Je n'arrose pas la plante " + str(plante))
            return 0
    else:
        if humidité > 50:
            #print("J'arrose la plante " + str(plante))
            return 1
        else:
            #print("Je n'arrose pas la plante " + str(plante))
            return 0
    
### Generate data (replace it with real data when we have it)
# 0 = tomate; 1 = basilic; 2 = menthe; 3 = persil; 4 = ciboulette (random plants for now)
plant_train = np.array([np.random.randint(0, 5) for i in range(1000000)])
humidity_train = np.array([np.random.randint(10, 90) for i in range(1000000)])
X_train = np.array([[plant_train[i] for i in range(1000000)], [humidity_train[i] for i in range(1000000)]])
Y_train = np.array([[arrose_easy(plant_train[i], humidity_train[i]) for i in range(1000000)]])

plant_test = np.array([np.random.randint(0, 5) for i in range(10000)])
humidity_test = np.array([np.random.randint(10, 90) for i in range(10000)])
X_test = np.array([[plant_train[i] for i in range(10000)], [humidity_train[i] for i in range(10000)]])
Y_test = np.array([[arrose_easy(plant_test[i], humidity_test[i]) for i in range(10000)]])

m_train = X_train.shape[1]
m_test = X_test.shape[1]

print ("Number of training examples: m_train = " + str(m_train))
print ("Number of testing examples: m_test = " + str(m_test))

def sigmoid(z):
    """
    Compute the sigmoid of z

    Arguments:
    z -- A scalar or numpy array of any size.

    Return:
    s -- sigmoid(z)
    """
    s = 1/(1+np.exp(-z))
    return s


def initialize_with_zeros(dim):
    """
    This function creates a vector of zeros of shape (dim, 1) for w and initializes b to 0.
    
    Argument:
    dim -- size of the w vector we want
    
    Returns:
    w -- initialized vector of shape (dim, 1)
    b -- initialized scalar (corresponds to the bias) of type float
    """
    w = np.zeros((dim, 1))
    b = 0.
    return w, b


def propagate(w, b, X, Y):
    """
    Implement the cost function and its gradient for the propagation.

    Arguments:
    w -- weights, a numpy array of size (nb of args (here 2 for plant type and humidity), 1)
    b -- bias, a scalar
    X -- data of size (nb of args (here 2 for plant type and humidity), number of examples)
    Y -- true "label" vector (containing 0 if the bot shouldn't water, 1 if it should) of size (1, number of examples)

    Return:
    grads -- dictionary containing the gradients of the weights and bias
            (dw -- gradient of the loss with respect to w, thus same shape as w)
            (db -- gradient of the loss with respect to b, thus same shape as b)
    cost -- negative log-likelihood cost for logistic regression
    """
    m = X.shape[1]
    A = sigmoid(np.dot(w.T,X)+b)
    cost = (-1/m)*np.sum(Y*np.log(A)+(1-Y)*np.log(1-A))

    dw = (np.dot(X,(A-Y).T))/m
    db = (np.sum(A-Y))/m

    cost = np.squeeze(np.array(cost))
    grads = {"dw": dw, "db": db}
    return grads, cost


def optimize(w, b, X, Y, num_iterations=1000, learning_rate=0.009, print_cost=False):
    """
    This function optimizes w and b by running a gradient descent algorithm
    
    Arguments:
    w -- weights, a numpy array of size (nb of args (here 2 for plant type and humidity), 1)
    b -- bias, a scalar
    X -- data of shape (nb of args (here 2 for plant type and humidity), number of examples)
    Y -- true "label" vector (containing 0 if the bot shouldn't water, 1 if it should), of shape (1, number of examples)
    num_iterations -- number of iterations of the optimization loop
    learning_rate -- learning rate of the gradient descent update rule
    print_cost -- True to print the loss every 100 steps
    
    Returns:
    params -- dictionary containing the weights w and bias b
    grads -- dictionary containing the gradients of the weights and bias with respect to the cost function
    costs -- list of all the costs computed during the optimization, this will be used to plot the learning curve.
    """
    w = copy.deepcopy(w)
    b = copy.deepcopy(b)
    dw = None
    db = None

    costs = []
    for i in range(num_iterations):
        # Cost and gradient calculation 
        grads, cost = propagate(w, b, X, Y)

        # Retrieve derivatives from grads
        dw = grads["dw"]
        db = grads["db"]

        # update w and b
        w = w - learning_rate*dw
        b = b - learning_rate*db

        # Record the costs
        if i % 100 == 0:
            costs.append(cost)
            # Print the cost every 100 training iterations
            if print_cost:
                print ("Cost after iteration %i: %f" %(i, cost))

    # update dictionary params
    params = {"w": w, "b": b}
    grads = {"dw": dw, "db": db}
    return params, grads, costs


def predict(w, b, X):
    '''
    Predict whether the label is 0 or 1 using learned logistic regression parameters (w, b)
    
    Arguments:
    w -- weights, a numpy array of size (nb of args (here 2 for plant type and humidity), 1)
    b -- bias, a scalar
    X -- data of size (nb of args (here 2 for plant type and humidity), number of examples)
    
    Returns:
    Y_prediction -- a numpy array (vector) containing all predictions (0/1) for the examples in X
    '''
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    
    # Compute vector "A" predicting the probabilities of a plant needing water
    A = sigmoid(np.dot(w.T,X)+b)
    
    for i in range(A.shape[1]):
        # Convert probabilities A[0,i] to actual predictions p[0,i]
        if A[0, i] > 0.5 :
            Y_prediction[0,i] = 1
        else:
            Y_prediction[0,i] = 0

    return Y_prediction


def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):
    """
    Builds the logistic regression model by calling the function you've implemented previously
    
    Arguments:
    X_train -- training set represented by a numpy array of shape (nb of args (here 2 for plant type and humidity), m_train)
    Y_train -- training labels represented by a numpy array (vector) of shape (1, m_train)
    X_test -- test set represented by a numpy array of shape (nb of args (here 2 for plant type and humidity), m_test)
    Y_test -- test labels represented by a numpy array (vector) of shape (1, m_test)
    num_iterations -- hyperparameter representing the number of iterations to optimize the parameters
    learning_rate -- hyperparameter representing the learning rate used in the update rule of optimize()
    print_cost -- Set to True to print the cost every 100 iterations
    
    Returns:
    d -- dictionary containing information about the model.
    """
    # initialize parameters with zeros
    w, b = initialize_with_zeros(X_train.shape[0])
    
    # Gradient descent 
    params, grads, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)
    
    # Retrieve parameters w and b from dictionary "params"
    w = params["w"]
    b = params["b"]
    
    # Predict test/train set examples
    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b, X_train)

    # Print train/test Errors
    if print_cost:
        print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
        print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

    
    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test, 
         "Y_prediction_train" : Y_prediction_train, 
         "w" : w, 
         "b" : b,
         "learning_rate" : learning_rate,
         "num_iterations": num_iterations}
    return d


logistic_regression_model = model(X_train, Y_train, X_test, Y_test, num_iterations=1000, learning_rate=0.005, print_cost=True)
