from matplotlib import pyplot
from numpy import array

from utils.Constants import GRAPH_WIDTH, GRAPH_HEIGHT


class Graph:
    def __init__(
            self, vert_indexes, vert_coords, title,
            width=GRAPH_WIDTH, height=GRAPH_HEIGHT,
            arrow_color="black", vert_color="red", font_color="white",
            first_arrow_color="cyan", last_arrow_color="magenta",
            vert_size=200, font_size=10
    ):
        self.width = width
        self.height = height
        self.title = title

        self.plt = pyplot
        self.plt.rcParams['figure.figsize'] = (width, height)
        self.plt.rcParams['figure.autolayout'] = True
        self.plt.grid = True

        self.ax = None
        self.fig = None

        self.vert_indexes = array(vert_indexes)
        self.vert_coords = array(vert_coords)
        self.vert_color = vert_color
        self.vert_size = vert_size

        self.arrow_color = arrow_color
        self.first_arrow_color = first_arrow_color
        self.last_arrow_color = last_arrow_color

        self.font_color = font_color
        self.font_size = font_size

        self.background_color = "white"

    def plot(self):
        # Create a new figure and axis each time plot is called
        self.fig, self.ax = self.plt.subplots(figsize=(self.width, self.height))

        # Labels
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title(self.title)

        x = [self.vert_coords[i][0] for i in self.vert_indexes]
        y = [self.vert_coords[i][1] for i in self.vert_indexes]

        # Directional vectors with steps
        dx = [x[i + 1] - x[i] for i in range(len(x) - 1)]
        dy = [y[i + 1] - y[i] for i in range(len(y) - 1)]
        steps = [str(i + 1) for i in range(len(dx))]

        dx.append(x[0] - x[-1])  # Directional vector from end to beginning vertices
        dy.append(y[0] - y[-1])
        steps.append(str(len(dx)))  # Adding last step from end to beginning vertices

        # Plotting arrows
        self._plot_arrows_(x, y, dx, dy)

        self.ax.scatter(
            x,  # X-coordinate of points
            y,  # Y-coordinate of points
            color=self.vert_color,
            marker='o',
            s=self.vert_size,  # Vertices size
        )

        for i, step in enumerate(steps):
            mid_x = (x[i] + x[i - 1]) / 2 if i > 0 else (x[i] + x[-1]) / 2
            mid_y = (y[i] + y[i - 1]) / 2 if i > 0 else (y[i] + y[-1]) / 2

            self._annotate_with_space_(
                steps[i - 1],
                (mid_x, mid_y),
                fontsize=self.font_size,
                ha='center', va='center',
                color=self.arrow_color,
                pad=0.01,
                fc=self.background_color,  # Default graph background
                ec="none"  # Edges are not drawn
            )

            self.ax.annotate(self.vert_indexes[i], (x[i], y[i]), fontsize=self.font_size, ha='center', va='center',
                             color=self.font_color)

        self.plt.show()

    def _plot_arrows_(self, x, y, dx, dy):
        # First arrow
        self.ax.quiver(
            x[0], y[0],
            dx[0], dy[0],
            color=self.first_arrow_color,
            angles='xy',
            scale_units='xy',
            scale=1
        )

        # All the other arrows except last one
        self.ax.quiver(
            x[1:-1], y[1:-1],
            dx[1:-1], dy[1:-1],
            color=self.arrow_color,
            angles='xy',
            scale_units='xy',
            scale=1
        )

        # Last arrow
        self.ax.quiver(
            x[-1], y[-1],
            dx[-1], dy[-1],
            color=self.last_arrow_color,
            angles='xy',
            scale_units='xy',
            scale=1
        )

    def _annotate_with_space_(self, text, xy, fontsize, ha, va, color, pad, fc, ec):
        bbox_props = dict(boxstyle="round, pad=" + str(pad), fc=fc, ec=ec)
        self.ax.text(xy[0], xy[1], text, fontsize=fontsize, ha=ha, va=va, color=color, bbox=bbox_props, zorder=10)
