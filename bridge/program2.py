import numpy as np


class NeuralNetwork():

    def __init__(self):
        # Seed the random number generator
        np.random.seed(1)

        # Set synaptic weights to a 3x1 matrix,
        # with values from -1 to 1 and mean 0
        self.synaptic_weights = 2 * np.random.random((13, 1)) - 1

    def sigmoid(self, x):
        """
        Takes in weighted sum of the inputs and normalizes
        them through between 0 and 1 through a sigmoid function
        """
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        """
        The derivative of the sigmoid function used to
        calculate necessary weight adjustments
        """
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        """
        We train the model through trial and error, adjusting the
        synaptic weights each time to get a better result
        """
        for iteration in range(training_iterations):
            # Pass training set through the neural network
            output = self.think(training_inputs)

            # Calculate the error rate
            error = training_outputs - output

            # Multiply error by input and gradient of the sigmoid function
            # Less confident weights are adjusted more through the nature of the function
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            # Adjust synaptic weights
            self.synaptic_weights += adjustments

    def think(self, inputs):
        """
        Pass inputs through the neural network to get output
        """

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


if __name__ == "__main__":
    # Initialize the single neuron neural network
    neural_network = NeuralNetwork()

    print("Random starting synaptic weights: ")
    print(neural_network.synaptic_weights)

    # input values and 1 output value
    # input dataset

    # open the file
    f = open("bridgein.txt", "r")
    lines = list(f)

    # filter
    river = ["A", "M", "O"]

    location = []
    for index1 in range(1, 53):
        location.append(index1)

    erected = ["CRAFTS", "EMERGING", "MATURE", "MODERN"]

    purpose = ["WALK", "AQUEDUCT", "RR", "HIGHWAY"]

    length = ["SHORT", "MEDIUM", "LONG"]

    lanes = ["1", "2", "4", "6"]

    clear_g = ["N", "G"]

    T_or_D = ["THROUGH", "DECK"]

    material = ["WOOD", "IRON", "STEEL"]

    span = ["SHORT", "MEDIUM", "LONG"]

    rel_l = ["S", "S-F", "F"]

    type = ["WOOD", "SUSPEN", "SIMPLE-T", "ARCH", "CANTILEV", "CONT-T"]

    # input has 96 lines and 13 elements for each line.
    # init the array
    inputData = np.zeros((96, 13), dtype=int)

    # if a match, return 1 else return 0
    # index start at 0
    # ex: inputData[row,[coloum]] = 1
    rowCounter = 0

    for line in lines:
        # go through each line
        eachLine = line.split(",")
        if eachLine[1] in river:
            inputData[rowCounter, [0]] = 1
        if eachLine[2] in location:
            inputData[rowCounter, [1]] = 1
        if eachLine[3] in erected:
            inputData[rowCounter, [2]] = 1
        if eachLine[4] in purpose:
            inputData[rowCounter, [3]] = 1
        if eachLine[5] in length:
            inputData[rowCounter, [4]] = 1
        if eachLine[6] in lanes:
            inputData[rowCounter, [5]] = 1
        if eachLine[7] in clear_g:
            inputData[rowCounter, [6]] = 1
        if eachLine[8] in T_or_D:
            inputData[rowCounter, [7]] = 1
        if eachLine[9] in material:
            inputData[rowCounter, [8]] = 1
        if eachLine[10] in span:
            inputData[rowCounter, [9]] = 1
        if eachLine[11] in rel_l:
            inputData[rowCounter, [10]] = 1
        if eachLine[12] in type:
            inputData[rowCounter, [11]] = 1
        rowCounter += 1

    f.close()
    # print(inputData)

    # insert output data
    # init the outputData array
    outputData = np.zeros((1, 96), dtype=int)
    bridgeIn = open("bridgeOut.txt", "r")
    bridgeLines = list(bridgeIn)
    trueFalseCounter = 0
    checker = ['Okay\n', 'Okay']
    for tfResponse in bridgeLines:
        if tfResponse in checker:
            outputData[0, [trueFalseCounter]] = 1
        trueFalseCounter += 1
    # print(outputData)
    outputData = outputData.T

    # Train the neural network
    neural_network.train(inputData, outputData, 10000)

    print("Synaptic weights after training: ")
    print(neural_network.synaptic_weights)

    #check the input and return value
    riverInput = str(input("Please Enter River: "))
    if riverInput in river:
        riverMeasure = 1
    else:
        riverMeasure = 0

    locationInput = str(input("Please Enter Location: "))
    if locationInput in location:
        locationMeasure = 1
    else:
        locationMeasure = 0

    erectedInput = str(input("Please Enter erected: "))
    if erectedInput in erected:
        erectedMeasure = 1
    else:
        erectedMeasure = 0

    purposeInput = str(input("Please Enter purpose "))
    if purposeInput in purpose:
        purposeMeasure = 1
    else:
        purposeMeasure = 0

    lengthInput = str(input("Please Enter length "))
    if lengthInput in length:
        lengthMeasure = 1
    else:
        lengthMeasure = 0

    lanesInput = str(input("Please Enter lanes "))
    if lanesInput in lanes:
        lanesMeasure = 1
    else:
        lanesMeasure = 0

    clear_gInput = str(input("Please Enter clear_g "))
    if clear_gInput in clear_g:
        clearGMeasure = 1
    else:
        clearGMeasure = 0

    TorD_Input = str(input("Please Enter T or D "))
    if TorD_Input in T_or_D:
        TorDMeasure = 1
    else:
        TorDMeasure = 0

    materialInput = str(input("Please Enter material "))
    if materialInput in material:
        materialMeasure = 1
    else:
        materialMeasure = 0

    spanInput = str(input("Please Enter span "))
    if spanInput in span:
        spanMeasure = 1
    else:
        spanMeasure = 0

    rel_L_input = str(input("Please Enter rel_l "))
    if rel_L_input in rel_l:
        rel_L_Measure = 1
    else:
        rel_L_Measure = 0

    typeInput = str(input("Please Enter Type "))
    if typeInput in type:
        typeMeasure = 1
    else:
        typeMeasure = 0



    print("New situation: input data = ",1, riverMeasure,locationMeasure,erectedMeasure,purposeMeasure,
          lengthMeasure,lanesMeasure,clearGMeasure,TorDMeasure,materialMeasure,spanMeasure,rel_L_Measure,typeMeasure)
    print("There is: ")
    print(neural_network.think(np.array([1,riverMeasure,locationMeasure,erectedMeasure,purposeMeasure,
          lengthMeasure,lanesMeasure,clearGMeasure,TorDMeasure,materialMeasure,spanMeasure,rel_L_Measure,typeMeasure])))
    print(" chance it will be okay")