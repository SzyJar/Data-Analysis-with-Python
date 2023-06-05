import numpy as np

def calculate(list):
  
  if (np.size(list) < 9):
     raise ValueError("List must contain nine numbers.")

  array = np.array(list)
  reshapedArray = np.reshape(array, (3,3))

  meanAxis1 = np.mean(reshapedArray, axis=0).tolist()
  meanAxis2 = np.mean(reshapedArray, axis=1).tolist()
  meanFlattened = np.mean(reshapedArray)
  
  varAxis1 = np.var(reshapedArray, axis=0).tolist()
  varAxis2 = np.var(reshapedArray, axis=1).tolist()
  varFlattened = np.var(reshapedArray)
  
  devAxis1 = np.std(reshapedArray, axis=0).tolist()
  devAxis2 = np.std(reshapedArray, axis=1).tolist()
  devFlattened = np.std(reshapedArray)
  
  maxAxis1 = np.max(reshapedArray, axis=0).tolist()
  maxAxis2 = np.max(reshapedArray, axis=1).tolist()
  maxFlattened = np.max(reshapedArray)
  
  minAxis1 = np.min(reshapedArray, axis=0).tolist()
  minAxis2 = np.min(reshapedArray, axis=1).tolist()
  minFlattened = np.min(reshapedArray)

  sumAxis1 = np.sum(reshapedArray, axis=0).tolist()
  sumAxis2 = np.sum(reshapedArray, axis=1).tolist()
  sumFlattened = np.sum(reshapedArray)

  calculations= {
    'mean': [meanAxis1, meanAxis2, meanFlattened],
    'variance': [varAxis1, varAxis2, varFlattened],
    'standard deviation': [devAxis1, devAxis2, devFlattened],
    'max': [maxAxis1, maxAxis2, maxFlattened],
    'min': [minAxis1, minAxis2, minFlattened],
    'sum': [sumAxis1, sumAxis2, sumFlattened]
  }

  return calculations
