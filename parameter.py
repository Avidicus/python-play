class Parameter(object):

    def __init__(self, delta_t = 1):

        self.start_t = 0.0
        self.end_t = 1000.0
        self.tau = .5
        self.N0 = 10000
        self.delta_t = delta_t