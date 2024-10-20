import random
import matplotlib.pyplot as plt

# Write your functions with their docstrings here

# nextMiddleSquare
def nextMiddleSquare(number):
  square = int(number)**2
  square = f"000{str(square)}"
  middle_digits = square[-3:-1]
  return middle_digits

# listMiddleSquare
def listMiddleSquare(start):
  list1 = []
  iteration = start
  for i in range(500):
    iteration = nextMiddleSquare(iteration)
    list1.append(int(iteration)/100)
  return list1
   
# nextLehmer
def nextLehmer(number):
  a = 17
  m = 101
  return (a * number) % m

# listLehmer
def listLehmer(start):
  list2 = []
  iteration = start
  for i in range(500):
    iteration = nextLehmer(iteration)
    list2.append(iteration/101)
  return list2

# listRandom
def listRandom(): 
  list3 = []
  for i in range(500):
    list3.append(random.randint(0,100)/100)
  return list3

def chartRandomNumbers(mid, lehmer, rand):
  '''
  This function draws a histogram of the three lists on the same plot
  :param mid: a list of random numbers from middle squares
  :param lehmer: a list of random numbers from lehmer
  :param rand: a list of random numbers from Python random module
  '''
  multi = [mid, lehmer, rand]
  plt.hist(multi, histtype='bar', label=['middle square', 'lehmer', 'random module'])
  plt.legend(prop={'size': 10})
  plt.show()
  
def main():
  start = 29 # I recommend seed = 83 since it yields a more diverse output
  list1 = listMiddleSquare(start)
  list2 = listLehmer(start)
  list3 = listRandom()
  chartRandomNumbers(list1, list2, list3)

if __name__ == "__main__":
  main()