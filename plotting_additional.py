# Plotting square, root and cubic functions
from cProfile import label

import numpy as np
import matplotlib.pyplot as plt

# def functions():
#     x=np.linspace(0,50,200)
#     y_root=np.sqrt(x)
#     y_square=x**2
#     y_cubic=x**3
#
#     plt.figure(figsize=(10,10))
#     plt.plot(x,y_root, 'r-', label="root")
#     plt.plot(x,y_square, 'b--', label="square")
#     plt.plot(x,y_cubic, 'gs',label='Cubic')
#     plt.legend()
#     plt.ylim(0, 50)
#     plt.xlim(0, 25)
#     plt.show()
#
# if __name__ == '__main__':
#     functions()

#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# def bar_chart():
#     names = ['Ali', 'Aysel', 'Kamran', 'Nigar']
#     scores = [75, 88, 64, 92]
#
#     plt.figure(figsize=(8, 5))
#     plt.bar(names, scores, width=0.6)
#
#     plt.xlabel('Students')
#     plt.ylabel('Scores')
#     plt.title('Exam Results')
#
#     plt.ylim(0, 100)
#     plt.show()
#
# if __name__ == "__main__":
#     bar_chart()





### Line graph task

import numpy as np
import matplotlib.pyplot as plt

def quadratic_func():
    x=np.linspace(0,120,100)
    y=1/x+23
    plt.plot(x,y)
    plt.show()

if __name__=="__main__":
    quadratic_func()













