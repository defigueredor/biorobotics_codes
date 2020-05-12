from environment import ENVIRONMENT
import constants as c

class ENVIRONMENTS:

    def __init__(self):
        self.envs = {}
        for e in range(0, c.numEnvs):
            self.envs[e] = ENVIRONMENT(e)