import numpy as np


def a_transpose(a: list):
  np_a = np.array(a)
  return np.transpose(np_a).tolist()

def a_lmul(a: list[float], lmul: list[list[float]]):
  np_a = np.array(a)
  np_lmul = np.array(lmul)
  # print(type(np_arr)) # <class 'numpy.ndarray'>z
  # print(type(np_lmul)) # <class 'numpy.ndarray'>
  # print(type(np_lmul[0])) # <class 'numpy.ndarray'>
  # print(type(np_lmul.tolist()[0]), np_lmul.tolist()[0]) # <class 'list'> [1, 2]
  mul = np.dot(np_lmul, np.transpose(np_a))
  return np.transpose(mul).tolist()

def a_relu(a: list[float]):
  np_a = np.array(a)
  return np.maximum(0, np_a)

def a_softmax(a: list[float]):
    exp_x = np.exp(a - np.max(a, axis=-1, keepdims=True))  # 防止数值溢出
    # print(np.max(a, axis=-1, keepdims=True))
    # print(exp_x)
    # print(a - np.max(a, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

if __name__ == '__main__':
  a = np.array([1,2])
  m = np.array([[0,1],[3,0]])
  print(a*m)
  # [[0 2]
  #  [3 0]]
  print(m*a)
  # [[0 2]
  #  [3 0]]
  print(np.dot(a,m)) # [6 1]
  print(np.dot(m,a)) # [2 3]

  print("...")

  a = np.array(None)
  print(a) # None

  print("...")
  
  # 测试 softmax 函数
  x = np.array([[1, 2, 3],
                [4, 5, 6]])
  print("Input:")
  print(x)
  print("\nSoftmax Output:")
  print(a_softmax(x))
  # [[0.09003057 0.24472847 0.66524096]
  #  [0.09003057 0.24472847 0.66524096]]



