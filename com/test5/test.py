import matplotlib.pyplot as plt


# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)

#
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
#
plt.tick_params(axis='both', which='major', labelsize=14)

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.axis([0, 1100, 0, 1100000])

plt.scatter(x_values, y_values, s=40)

plt.show()
