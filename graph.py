import matplotlib.pyplot as plt


plt.ion()


def plot(scores):
    plt.clf()
    plt.title("Training...")
    plt.xlabel("Number of Games")
    plt.ylabel("Time (s)")
    plt.plot(scores)
    plt.pause(0.1)
