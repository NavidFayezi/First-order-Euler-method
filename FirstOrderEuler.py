
# this function approximates values of y from an initial point to an end point.
# y(n+1) = y(n) + h*f(inverse_of(y(n)),y(n)).
# h is the step size.
# f is the derivative(slope) of y in a given point.


def euler_method(slope, initial_point_x, initial_point_y, end_point_x, step_size):

    number_of_steps = int((end_point_x - initial_point_x) / step_size)
    output = [(initial_point_x, initial_point_y)]                  # values of y will be stored in output.
    for i in range(number_of_steps):
        temp_y = output[i] + step_size * slope(output[i][0], output[i][1])
        output.append((output[i][0]+step_size, temp_y))

    return output
