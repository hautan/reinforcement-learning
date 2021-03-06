import matplotlib.pyplot as plt

from util.strategy import run_epsilon_greedy

if __name__ == "__main__":
  c1 = run_epsilon_greedy(1.0, 2.0, 3.0, 100000, 0.1)
  c05 = run_epsilon_greedy(1.0, 2.0, 3.0, 100000, 0.05)
  c01 = run_epsilon_greedy(1.0, 2.0, 3.0, 100000, 0.01)
  
  plt.plot(c1, label='eps = 0.1')
  plt.plot(c05, label='eps = 0.05')
  plt.plot(c01, label='eps = 0.01')
  plt.legend()
  plt.xscale('log')
  plt.show()
  
  plt.plot(c1, label='eps = 0.1')
  plt.plot(c05, label='eps = 0.05')
  plt.plot(c01, label='eps = 0.01')
  plt.legend()
  plt.show()
  
