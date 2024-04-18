def linear_interpolation(points, x):
    """
    Linear interpolation function.
    :param points: List of tuples representing points [(x1, y1), (x2, y2), ...]
    :param x: x value for which to find the approximate y value
    :return: Approximate y value
    """
    if len(points) < 2:
        raise ValueError("Linear interpolation requires at least two points")
    # Sort points by x values
    points.sort(key=lambda p: p[0])
    # Find the interval containing the x value
    for i in range(len(points) - 1):
        if points[i][0] <= x <= points[i + 1][0]:
            # Perform linear interpolation
            x0, y0 = points[i]
            x1, y1 = points[i + 1]
            slope = (y1 - y0) / (x1 - x0)
            return y0 + slope * (x - x0)
    raise ValueError("x value is outside the range of provided points")


def polynomial_interpolation(points, x):
    """
    Polynomial interpolation function for 3 points.
    :param points: List of tuples representing 3 points [(x1, y1), (x2, y2), (x3, y3)]
    :param x: x value for which to find the approximate y value
    :return: Approximate y value
    """
    if len(points) != 3:
        raise ValueError("Polynomial interpolation requires exactly 3 points")
    # Unpack points
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    # Calculate coefficients of the quadratic polynomial
    a0 = y1
    a1 = (y2 - y1) / (x2 - x1)
    a2 = ((y3 - y2) / (x3 - x2) - (y2 - y1) / (x2 - x1)) / (x3 - x1)
    # Evaluate polynomial at x
    return a0 + a1 * (x - x1) + a2 * (x - x1) * (x - x2)


def lagrange_interpolation(points, x):
    """
    Lagrange interpolation function for 3 points.
    :param points: List of tuples representing 3 points [(x1, y1), (x2, y2), (x3, y3)]
    :param x: x value for which to find the approximate y value
    :return: Approximate y value
    """
    if len(points) != 3:
        raise ValueError("Lagrange interpolation requires exactly 3 points")
    # Unpack points
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    # Lagrange basis polynomials
    L1 = ((x - x2) * (x - x3)) / ((x1 - x2) * (x1 - x3))
    L2 = ((x - x1) * (x - x3)) / ((x2 - x1) * (x2 - x3))
    L3 = ((x - x1) * (x - x2)) / ((x3 - x1) * (x3 - x2))
    # Evaluate Lagrange interpolation
    return y1 * L1 + y2 * L2 + y3 * L3


def main():
    # Define pairs of points
    points = [(1, 2), (2, 3), (3, 5)]
    # Define x value for which y value is needed
    x_value = float(input("Enter the x value for which you want to find the y value: "))
    # Choose interpolation method
    method = input("Choose the interpolation method (linear/polynomial/lagrange): ").lower()
    # Find approximate y value using chosen method
    if method == "linear":
        y_value = linear_interpolation(points, x_value)
    elif method == "polynomial":
        y_value = polynomial_interpolation(points, x_value)
    elif method == "lagrange":
        y_value = lagrange_interpolation(points, x_value)
    else:
        print("Invalid interpolation method")
        return
    print(f"Approximate y value for x={x_value} using {method} interpolation: {y_value}")


if __name__ == "__main__":
    main()
