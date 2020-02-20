
import numpy as np

class interpolate:
    def __init__(self, data,pos):
        self.data   = data
        self.n      = len(data)
        self.h      = pos[1]-pos[0]

        co_matrix   = np.zeros((self.n-2,self.n-2))
        f_matrix    = np.zeros((1,self.n-2))

        for i in range(self.n-2):
            co_matrix[i][i]        = 4

            if i != 0:
                co_matrix[i][i-1]  = 1
                co_matrix[i-1][i]  = 1

            f_matrix[0][i]         = (data[i] -2*data[i+1] + data[i+2])*6  / self.h**2
        

        m_matrix    = np.linalg.inv(co_matrix).dot(f_matrix.transpose())

        self.abcd   = np.zeros[(4 , self.n - 1)]

        for i in range(self.n-1):
            ai  = m_matrix[i+1] - m_matrix[i] / (6 * self.h)
            bi  = m_matrix[i] / 2
            ci  = (self.data[i+1] - self.data[i]) / self.h - self.h / 3 * m_matrix[i] - self.h / 6 * m_matrix[i+1]
            di  = self.data[i]

            self.abcd[:][i] = [ai,bi,di,zi]


        print(co_matrix)
        print(f_matrix)
        print(m_matrix)





data = [0.5,0.8,1,0.8,0.5]
pos = [-1,-.5,0,.5,1]
interpolate(data,pos)