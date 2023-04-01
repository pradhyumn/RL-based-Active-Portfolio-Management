from ..tdagent import TDAgent
import numpy as np

class BEST(TDAgent):
    '''Best Stock Strategy
    '''
    def __init__(self, last_b=None):
        super(BEST, self).__init__()
        self.last_b = last_b

    def decide_by_history(self, x, last_b, test_data=None, **kwargs):
        if self.last_b is None:
            data = test_data
            data = data.T
            n, m = data.shape
            tmp_cumprod_ret = np.cumprod(data, axis=0)
            best_ind = np.argmax(tmp_cumprod_ret[-1,:])
            self.last_b = np.zeros(m)
            self.last_b[best_ind] = 1
        return self.last_b.ravel()
