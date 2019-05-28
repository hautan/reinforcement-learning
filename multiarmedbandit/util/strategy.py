import numpy as np
import matplotlib.pyplot as plt

from model.Bandit import Bandit

def run_epsilon_greedy(m1, m2, m3, N, eps):
  bandits = [Bandit(m1, 0), Bandit(m2, 0), Bandit(m3, 0)]
  
  data = np.empty(N)
  
  for i in range(N):
    p = np.random.random()
    if p < eps:
      j = np.random.choice(3)
    else:
      j = np.argmax([b.mean for b in bandits])
    x = bandits[j].pull()
    bandits[j].update(x)
    
    data[i] = x
    
  cumulative_average = np.cumsum(data)/(np.arange(N) + 1)
#  cumulative_average = np.cumsum(data)
  
  plt.plot(cumulative_average)
  plt.plot(np.ones(N)*m1)
  plt.plot(np.ones(N)*m2)
  plt.plot(np.ones(N)*m3)
  plt.xscale('log')
  plt.show()
  
  for b in bandits:
    print(b.mean)
    
  return cumulative_average
    
def run_optimistic_initial_value(m1, m2, m3, N, itv=10):
  bandits = [Bandit(m1, itv), Bandit(m2, itv), Bandit(m3, itv)]
  
  data = np.empty(N)
  
  for i in range(N):
    j = np.argmax([b.mean for b in bandits])
    x = bandits[j].pull()
    bandits[j].update(x)
    
    data[i] = x
    
  cumulative_average = np.cumsum(data)/(np.arange(N) + 1)
#  cumulative_average = np.cumsum(data)
  
  plt.plot(cumulative_average)
  plt.plot(np.ones(N)*m1)
  plt.plot(np.ones(N)*m2)
  plt.plot(np.ones(N)*m3)
  plt.xscale('log')
  plt.show()
  
  for b in bandits:
    print(b.mean)
    
  return cumulative_average

def run_ucb(m1, m2, m3, N, itv=10):
  def ucb(mean, n, nj):
      if nj == 0:
          return float('inf')
      return mean + np.sqrt(2*np.log(n) / nj)
  
  bandits = [Bandit(m1, itv), Bandit(m2, itv), Bandit(m3, itv)]
  
  data = np.empty(N)
  
  for i in range(N):
    j = np.argmax([ucb(b.mean, i+1, b.N) for b in bandits])
    x = bandits[j].pull()
    bandits[j].update(x)
    
    data[i] = x
    
  cumulative_average = np.cumsum(data)/(np.arange(N) + 1)
#  cumulative_average = np.cumsum(data)
  
  plt.plot(cumulative_average)
  plt.plot(np.ones(N)*m1)
  plt.plot(np.ones(N)*m2)
  plt.plot(np.ones(N)*m3)
  plt.xscale('log')
  plt.show()
  
  for b in bandits:
    print(b.mean)
    
  return cumulative_average