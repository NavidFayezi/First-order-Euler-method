# this function approximates values of y from an initial point to an end point.
# y(n+1) = y(n) + h*f(inverse_of(y(n)),y(n)).
# h is the step size.
# f is the derivative(slope) of y in a given point.


def euler_method(slope, initial_point_x, initial_point_y, end_point_x, step_size):
    number_of_steps = int(round((end_point_x - initial_point_x) / step_size,5))
    output = [(initial_point_x, initial_point_y)]  # values of y will be stored in output.
    for i in range(1,number_of_steps+1,1):
        temp_y = output[i-1][1] + step_size * slope(output[i-1][0], output[i-1][1])
        output.append((output[i-1][0] + step_size, temp_y))

    return output


def test(x, y):
    return x + y


if __name__ == "__main__":
    print(euler_method(test, 0, 1, 0.3, 0.1))
