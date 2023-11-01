from numpy import array, sort
from matplotlib import pyplot

class Graph:
    def __init__(self, points, title, primary_color="red", secondary_color="blue"):
        self.plt = pyplot
        self.plt.rcParams['figure.figsize'] = (5, 5)
        self.plt.rcParams['figure.autolayout'] = True
        self.plt.grid = True
        self.plt.xlabel('X')
        self.plt.ylabel('Y')

        self.points = array(points)
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.plt.title = title

        self.plt.xticks(range(len(self.points)), self.points)


    def plot(self):
        y = sort(self.points)


        self.plt.plot(
            self.points, y,
            color=self.primary_color,
            marker="o",
            markerfacecolor=self.secondary_color,
            markeredgecolor=self.secondary_color,
            markersize=12,
            linewidth=3
        )
        self.plt.show()