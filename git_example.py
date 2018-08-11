```
This python file si a goood starting pouint.
Activation Funstions
```

#libraries
import numpy as np

def sigmoid(x):
  # enter code below
  return (1 / (1 + numpy.exp(-x)))

def tanh(x):
  return((numpy.exp(x)-numpy.exp(-x))/(numpy.exp(x)+numpy.exp(-x)))
  
def relu(x):
  if x<0:
    return 0
  else:
    return x
  
