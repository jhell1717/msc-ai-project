import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


class Shape:

    def __init__(self, points, n_points=None, normalise=True):
        """
        Base class for shapes, with optional resampling.

        Parameters
        ----------
        points : ndarray of shape (N, 2)
            The (x, y) coordinates of the shape's points.

        n_points : int, optional
            Number of points to resample the shape to. If None, no resampling
            is performed.
        """
        if n_points is not None:
            points = self._resample(points, n_points)
        if normalise:
            self.points = self._normalise_shape(points)

    @staticmethod
    def _resample(points, n_points):
        """
        Resample the shape to have a fixed number of points.

        Parameters
        ----------
        points : ndarray of shape (N, 2)
            Original points of the shape.

        n_points : int
            Desired number of points.

        Returns
        -------
        ndarray of shape  n_points, 2)
            Resampled points.
        """
        closed_points = np.vstack([points, points[0]])
        distances = np.cumsum(np.linalg.norm(
            np.diff(closed_points, axis=0), axis=1))
        distances = np.insert(distances, 0, 0)
        interp_func = interp1d(distances, closed_points, axis=0, kind="linear")
        uniform_distances = np.linspace(0, distances[-1], n_points)
        return interp_func(uniform_distances)

    def _normalise_shape(self, points):
        """
        Normalises the shape points to the [0, 1] range.

        Returns
        -------
        numpy.ndarray
            Normalised points of the shape.
        """
        min_val = points.min()
        max_val = points.max()
        return (points - min_val) / (max_val - min_val)

    def plot(self, ax=None):
        """
        Plot the shape.

        Parameters
        ----------
        ax : matplotlib.axes.Axes, optional
            Matplotlib axis object. If None, a new figure is created.
        """
        if ax is None:
            _, ax = plt.subplots()
        closed_points = np.vstack([self.points, self.points[0]])
        ax.plot(closed_points[:, 0], closed_points[:, 1], "-o", label="Shape")
        ax.set_aspect("equal", adjustable="box")
        plt.show()


class Circle(Shape):
    def __init__(self, radius=None, n_points=50):
        """
        A circle defined by its radius and number of points.

        Parameters
        ----------
        radius : float
            Radius of the circle.

        n_points : int
            Number of points to approximate the circle.
        """
        if radius is None:
            radius = np.random.uniform(0.1, 1)
        theta = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
        points = np.column_stack(
            (radius * np.cos(theta), radius * np.sin(theta)))
        super().__init__(points, n_points)
        
class Triangle(Shape):
    
    def __init__(self, n_points=50, vertices=None):
        """
        A triangle defined by three vertices, resampled to a fixed number of points.

        Parameters
        ----------
        n_points : int
            Number of points to resample the triangle to.

        vertices : ndarray of shape (3, 2), optional
            Coordinates of the triangle's vertices. If None, a random triangle
            is generated.
        """
        if vertices is None:
            vertices = self._generate_valid_triangle()
        super().__init__(vertices, n_points)

    @staticmethod
    def _generate_valid_triangle():
        """Generate a random valid triangle."""
        while True:
            points = np.random.uniform(-1, 1, size=(3, 2))
            if Triangle._is_valid_triangle(points):
                return points

    @staticmethod
    def _is_valid_triangle(points):
        """
        Check if the given points form a valid triangle.

        Parameters
        ----------
        points : ndarray of shape (3, 2)
            Points to check.

        Returns
        -------
        bool
            True if the points form a valid triangle, False otherwise.
        """
        v1 = points[1] - points[0]
        v2 = points[2] - points[0]
        return np.abs(np.cross(v1, v2)) > 1e-6
