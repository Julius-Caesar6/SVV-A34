import numpy as np

class interpolate:

    ''' see example below for how to get the coefficients. Keep in mind its ai(x-xi)^3 etc'''
    def __init__(self, data, pos):
        self.data   = data
        self.n      = len(data)

        #Create a list of all the distances between points.
        self.h      = np.zeros(self.n-1)
        for i in range(self.n-1):
            self.h[i]  = pos[i+1]-pos[i]

        #Setup the matrixes
        co_matrix   = np.zeros((self.n-2,self.n-2))
        f_matrix    = np.zeros((self.n-2,1))

        for i in range(self.n-2):
            co_matrix[i][i]         = (self.h[i]+self.h[i+1])/3

            if i != 0:
                co_matrix[i][i-1]   = self.h[i]/6
                co_matrix[i-1][i]   = self.h[i]/6

            #f matrix is shifted because i is defined weird due to m0 and mn being 0 and not part of the comatrixes


            f_matrix[i][0]          = (data[i+2] - data[i+1])/self.h[i+1] - (data[i+1] - data[i])/self.h[i]
        

        m_matrix    = np.linalg.solve(co_matrix,f_matrix)
        #Add boundary conditions for m_matrix
        m_matrix    = np.vstack((np.array([0]),m_matrix))
        m_matrix    = np.vstack((m_matrix,np.array([0])))

        self.abcd   = np.zeros((self.n - 1 , 4))
        
        

    
        for i in range(self.n-1):

            ai  = (m_matrix[i+1] - m_matrix[i] )/ (6 * self.h[i])
            bi  = m_matrix[i] / 2
            ci  = (self.data[i+1] - self.data[i]) / self.h[i] - self.h[i] / 3 * m_matrix[i] - self.h[i] / 6 * m_matrix[i+1]
            di  = self.data[i]

            self.abcd[i] = [ai,bi,ci,di]


