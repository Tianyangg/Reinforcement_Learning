import numpy as np
import random as rd

class Mrp:
    # states
    #states = ['Class1', 'Facebook', 'Class2', 'Class3', 'Pub', 'Pass', 'Sleep']
    states = {'Class1': 0, 'Facebook': 1, 'Class2': 2, 'Class3': 3, 'Pub': 4, 'Pass': 5, 'Sleep': 6}
    # use a dictionary
    #transition = ['C1Fb', 'FbFb','FbC1', 'C1C2', 'C2SL', 'C2C3', 'C3Pass', 'PassSL', 'C3Pub', 'PubC2', 'PubC1', 'PubC2']
    #transition = [['C1Fb', 'C1C2'], ['FbFb','FbC1'], ['C2SL', 'C2C3'], ['C3Pass', 'C3Pub'], ['PubC2', 'PubC1', 'PubC2'],['PassSL'], ['Sleep']]
    # write the function that returns the transition probability
    # transition Matrix
    trans_mat = np.matrix[
        [0, 0.5, 0.5, 0, 0, 0, 0],
        [0.1, 0.9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0.8, 0, 0, 0.2],
        [0, 0, 0, 0, 0.4, 0.6, 0],
        [0.2, 0, 0.4, 0.4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1]]

    def get_p(self):
        return 0

