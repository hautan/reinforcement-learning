import matplotlib.pyplot as plt

from util.strategy import run_epsilon_greedy, run_ucb

if __name__ == "__main__":
  c1 = run_epsilon_greedy(1.0, 2.0, 3.0, 100000, 0.1)
  i10 = run_ucb(1.0, 2.0, 3.0, 100000, 10)
  
  plt.plot(c1, label='eps = 0.1')
  plt.plot(i10, label='ucb1')
  plt.legend()
  plt.xscale('log')
  plt.show()
  
  plt.plot(c1, label='eps = 0.1')
  plt.plot(i10, label='ucb1')
  plt.legend()
  plt.show()
  
# -*- coding: utf-8 -*-

