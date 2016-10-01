import sys
import math
import numpy as np
from parameter import Parameter
from graph import graph



def main():
    parameters = setup();

    x = np.linspace(parameters.start_t, parameters.end_t, parameters.delta_t)
    y = function(parameters, x)

    graph(x, y, 'N0 * e^(x/tau)')

    pass


def setup():
    parameters = Parameter(1);
    return parameters


def function(parameter, x):
    return parameter.N0 * math.exp(x / parameter.tau)


def firstDerivitaveFunction(parameter, t):
    pass


def firstDerivitaveApprox(parameter, t):
    pass


if __name__ == '__main__':
    sys.exit(main())
