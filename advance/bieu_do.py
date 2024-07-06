import matplotlib.pyplot as plt

x = [1, 2, 2,4,6,9]
y = [2, 4, 6,6,5,7]

plt.plot(x, y, color='green', linewidth = 1, label = "Focus")

x = [1, 2, 5,5,7,8]
y = [2, 3, 5,6,6,8]

plt.plot(x, y, color='red', linewidth = 1, label="Miss")

plt.title('Biểu đồ improve code của bản thân')
plt.xlabel('Thời gian')
plt.ylabel('Năng suất')

plt.legend()

plt.show()