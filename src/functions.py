import numpy as np


# Physical constants
hbar = 1.05457182E-34
m = 9.1093837E-31


# def theta2k(E,theta):
#     Ejoule = E *1.6E-19
#     k = np.arcsin((k/np.sqrt(Ejoule))*(hbar/np.sqrt(2*m)))
#     return k

def k2theta(E,k):
    Ejoule = E *1.6E-19
    k = k*1E10
    theta = np.arcsin((k/np.sqrt(Ejoule))*(hbar/np.sqrt(2*m)))
    return np.rad2deg(theta)


def theta2k(E,theta):
    Ejoule = E *1.6E-19
    theta = np.deg2rad(theta)
    k = (np.sqrt(2*m)/hbar)*np.sqrt(Ejoule)*np.sin(theta)
    return k*1E-10
















# class Utilities:


#     def __init__(self):
#         # Physical constants
#         self.hbar = 1.05457182E-34
#         self.m = 9.1093837E-31
        



#     def k2theta(self,E,k):
#         Ejoule = E *1.6E-19
#         theta = np.arcsin((k/np.sqrt(Ejoule))*(self.hbar/np.sqrt(2*self.m)))
#         return theta
