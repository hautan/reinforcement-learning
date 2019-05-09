import numpy as np
import matplotlib.pyplot as plt

class Bandit:
  def __init__(self, m, initialValue):
    self.m = m
    self.mean = initialValue
    self.N = 0
    
  def pull(self):
    return np.random.rand() + self.m
  
  def update(self, x):
    self.N += 1
    self.mean = (1-1.0/self.N)*self.mean + 1.0/self.N * x
    
#  def defaultMeanGreedy(N, mean, x):
    
    