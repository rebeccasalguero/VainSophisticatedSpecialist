import numpy as np

def calculate(list):
    
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")

    newArr = np.array(list).reshape(3,3)
    
    mean = [np.mean(newArr, axis = 0).tolist(),
            np.mean(newArr, axis = 1).tolist(), 
            np.mean(newArr).tolist()]
    
    var = [np.var(newArr, axis = 0).tolist(), 
           np.var(newArr, axis = 1).tolist(), 
           np.var(newArr).tolist()]
    
    stdev = [np.std(newArr, axis = 0).tolist(),
             np.std(newArr, axis = 1).tolist(),
             np.std(newArr).tolist()]
    
    min1 = [np.min(newArr, axis = 0).tolist(),
            np.min(newArr, axis = 1).tolist(),
            np.min(newArr).tolist()]
    
    max1 = [np.max(newArr, axis = 0).tolist(),
            np.max(newArr, axis = 1).tolist(),
            np.max(newArr).tolist()]
    
    sumOf1 = [np.sum(newArr, axis = 0).tolist(),
              np.sum(newArr, axis = 1).tolist(),
              np.sum(newArr).tolist()]
              
    calculations = {"mean": mean,
                "variance": var,
                "standard deviation":stdev,
                "max": max1,
                "min": min1,
                "sum": sumOf1}
  
    return calculations