import sys
import math
import numpy
from parameter import Parameter
from graph import graph



def main():
    parameters = setup()

    number_of_samples = (parameters.end_t - parameters.start_t) / parameters.delta_t
    x = numpy.linspace(parameters.start_t, parameters.end_t, number_of_samples)

    y = parameters.N0 * numpy.power(numpy.exp(x), -1 / parameters.tau)

    graph(x, y, r'$N_0 e^{\frac{-1}{\tau}t}$')

    pass


def setup():
    # User input

    parameters = Parameter(0.1)
    return parameters


def function(parameter, x):
    # needs to be a numpy.linespace

    return parameter.N0 * math.exp(-x / parameter.tau)


def firstDerivitaveFunction(parameter, t):
    pass


def firstDerivitaveApprox(parameter, t):
    pass


if __name__ == '__main__':
    sys.exit(main())
