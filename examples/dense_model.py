"""
  Generated using Konverter: https://github.com/ShaneSmiskol/Konverter
"""

import numpy as np

wb = np.load('C:\Git\konverter\examples/dense_model_weights.npz', allow_pickle=True)
w, b = wb['wb']

def tanh(x):
  return np.tanh(x)
def relu(x):
  return np.maximum(0, x)

def predict(x):
  l0 = np.dot(x, w[0]) + b[0]
  l0 = tanh(l0)
  l1 = np.dot(l0, w[1]) + b[1]
  l1 = relu(l1)
  l2 = np.dot(l1, w[2]) + b[2]
  l2 = relu(l2)
  l3 = np.dot(l2, w[3]) + b[3]
  l3 = relu(l3)
  l4 = np.dot(l3, w[4]) + b[4]
  return l4