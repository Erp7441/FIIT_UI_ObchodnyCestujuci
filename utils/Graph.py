from numpy import array, sort
from matplotlib import pyplot
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch

class Graph:
    def __init__(self, vert_indexes, vert_coords, title,
                width=6, height=6,
                arrow_color="black", vert_color="red", font_color="white",
                first_arrow_color="cyan", last_arrow_color="magenta",
                vert_size=200, font_size=10
    ):
        self.plt = pyplot
        self.plt.rcParams['figure.figsize'] = (width, height)
        self.plt.rcParams['figure.autolayout'] = True
        self.plt.grid = True
        self.plt.xlabel('X')
        self.plt.ylabel('Y')

        self.vert_indexes = array(vert_indexes)
        self.vert_coords = array(vert_coords)
        self.vert_color = vert_color
        self.vert_size = vert_size

        self.arrow_color = arrow_color
        self.first_arrow_color = first_arrow_color
        self.last_arrow_color = last_arrow_color

        self.font_color = font_color
        self.font_size = font_size

        self.plt.title = title

        self.background_color = "white"


    def plot(self):
        x = [self.vert_coords[i][0] for i in self.vert_indexes]
        y = [self.vert_coords[i][1] for i in self.vert_indexes]

        # Vytvorenie smerových vektorov a priradenie krokov
        dx = [x[i+1] - x[i] for i in range(len(x)-1)]
        dy = [y[i+1] - y[i] for i in range(len(y)-1)]
        steps = [str(i + 1) for i in range(len(dx))]

        dx.append(x[0] - x[-1])  # Smerový vektor pre spojenie posledného bodu s prvým bodom
        dy.append(y[0] - y[-1])
        steps.append(str(len(dx)))  # Pridáme krok pre posledný bod

        # Plotting arrows
        self._plot_arrows_(x, y, dx, dy)

        self.plt.scatter(
            x,  # X-coordinate of points
            y,  # Y-coordinate of points
            color=self.vert_color,
            marker='o',
            s=self.vert_size,  # Veľkosť bodov
        )

        for i, step in enumerate(steps):
            mid_x = (x[i] + x[i-1]) / 2 if i > 0 else (x[i] + x[-1]) / 2
            mid_y = (y[i] + y[i-1]) / 2 if i > 0 else (y[i] + y[-1]) / 2

            self._annotate_with_space_(
                steps[i-1],
                (mid_x, mid_y),
                fontsize=self.font_size,
                ha='center', va='center',
                color=self.arrow_color,
                pad=0.01,
                fc=self.background_color,  # Default graph background
                ec="none"  # Edges are not drawn
            )

            self.plt.annotate(self.vert_indexes[i], (x[i], y[i]), fontsize=self.font_size, ha='center', va='center',
                              color=self.font_color)

        self.plt.show()

    def _plot_arrows_(self, x, y, dx, dy):
        # Plotting arrows (prvá šípka)
        self.plt.quiver(
            x[0],  y[0],
            dx[0], dy[0],
            color=self.first_arrow_color,  # Farba prvej šípky
            angles='xy',
            scale_units='xy',
            scale=1
        )

        # Plotting arrows (všetky okrem poslednej šípky)
        self.plt.quiver(
            x[1:-1],  # X a Y-coordinate of starting points (všetky okrem poslednej)
            y[1:-1],
            dx[1:-1],      # Zmena X pre smerové vektory
            dy[1:-1],      # Zmena Y pre smerové vektory
            color=self.arrow_color,  # Farba pre všetky okrem poslednej
            angles='xy',
            scale_units='xy',
            scale=1
        )

        # Posledná šípka (iná farba)
        self.plt.quiver(
            x[-1],  # X-coordinate of the last point
            y[-1],  # Y-coordinate of the last point
            dx[-1],  # Zmena X pre posledný smerový vektor
            dy[-1],  # Zmena Y pre posledný smerový vektor
            color=self.last_arrow_color,  # Farba poslednej šípky
            angles='xy',
            scale_units='xy',
            scale=1
        )

    def _annotate_with_space_(self, text, xy, fontsize, ha, va, color, pad, fc, ec):
        bbox_props = dict(boxstyle="round, pad="+str(pad), fc=fc, ec=ec)
        self.plt.text(xy[0], xy[1], text, fontsize=fontsize, ha=ha, va=va, color=color, bbox=bbox_props, zorder=10)