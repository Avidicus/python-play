class Parameter(object):
    def __init__(self, delta_t=1.0):

        self.start_t = 0.0
        self.end_t = 10.0
        self.tau = .95
        self.N0 = 1
        self.delta_t = delta_t