import matplotlib.pyplot as plt

# This neural net will learn AND and OR gate
AND = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
OR = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]

# But it is not learning XOR gate
XOR = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]


input_set = [[i[0], i[1]] for i in OR]

output_set = [i[2] for i in OR]

# print(output_set)

# Read the input
# x, y = map(int, input("Enter the input").split())

# input_matrix = [x, y]

# Initialize weights as 0
weight_matrix = [0.0, 0.0, 0.0]  # The number at -1th position is the bias

LR = 0.1
EPOCH = 5


def stepfn(x):
    return 1 if x >= 0 else 0


# biased weighted sum
def bwsum(i_mat, w_mat):
    s = 0
    for i in range(len(i_mat)):
        s += i_mat[i] * w_mat[i]
    return s + w_mat[-1]


def errfn(predicted, actual):
    return actual - predicted


def learn(wb_mat, i_mat, err, LR=0.1):
    output = []
    for i in range(len(i_mat)):
        output.append(wb_mat[i] + (LR * err * i_mat[i]))
    output.append(wb_mat[-1] + (LR * err))
    return output


accuracy_list = []

# Training loop
for i in range(EPOCH):
    print(f"Epoch: {i}")
    incorrect = 0
    for j in range(len(input_set)):
        pred = stepfn(bwsum(input_set[j], weight_matrix))
        print(f"Prediction: {pred}, Actual: {output_set[j]}")
        err = errfn(pred, output_set[j])
        if err != 0:
            incorrect += 1
            print("Adjusting weights and biases")
            weight_matrix = learn(weight_matrix, input_set[j], err, LR)
            print(f"Adjusted weights matrix: {weight_matrix}")
    accuracy = (len(input_set) - incorrect) * 100 / len(input_set)
    accuracy_list.append(accuracy)
    print(f"Accuracy: {accuracy}%\n")


# Plot the accuracy:
plt.plot(list(range(EPOCH)), accuracy_list)
plt.savefig("accuracy_plot.png")
plt.show()

# Predicting the outputs
print("Validation")
print("Pred\tAct")
for i in range(len(input_set)):
    print(f"{stepfn(bwsum(input_set[i], weight_matrix))}\t{output_set[i]}")
# print(stepfn(wsum(input_matrix, weight_matrix)))
