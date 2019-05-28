import numpy as np
import constant.Length as Length

class Environment:
  def __init__(self):
      self.board = np.zeroes((Length, Length))
      self.x = -1
      self.o = 1
      self.winner = None
      self.ended = False
      self.num_states = 3 **(Length*Length)
      
  def reward(self, sym):
      if not self.game_over():
          return 0;
      return 1 if self.winner == sym else 0

  def game_over(self, forece_recalculate=False):
      if not forece_recalculate and self.ended:
          return self.ended
      #check rows
      for i in range(Length):
          for player in (self.x, self.o):
              if self.board[i].sum() == player*Length:
                  self.winner = player
                  self.ended = True
                  return True
      #check rows
      for j in range(Length):
          for player in (self.x, self.o):
              if self.board[:,j].sum() == player*Length:
                  self.winner = player
                  self.ended = True
                  return True
      #check diagonal
      for player in (self.x, self.o):
          if self.board.trace() == player*Length:
              self.winner = player
              self.ended = True
              return True
          if np.fliplr(self.board.trace()) == player*Length:
              self.winner = player
              self.ended = True
              return True
          
  def draw_board(self):
      for i in range(Length):
          for j in range(Length):              
              if self.board[i,j] == self.x:
                  print("x,")
              elif self.board[i,j] == self.o: 
                  print("o,")
              else:
                  print(" ,")
          print("")            
      
  def check_draw(self):
      if np.all((self.board == 0) == False):
          self.winner = None
          self.ended = True
          return True
      #game is not over
      self.winner = None
      return False

  def get_state(self):
      k = 0
      h = 0
      for i in range(Length):
          for j in range(Length):
              if self.board[i,j] == 0:
                  v = 0
              elif self.board[i,j] == self.x:
                  v = 1
              elif self.board[i,j] == self.o:
                  v = 2
              h += (3**k) *v
              k += 1
      return h

  def is_empty(self, i, j):
      return self.board[i,j] == 0
  
        
        
  
