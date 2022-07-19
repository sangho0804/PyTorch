#tensor

from xml.dom import NAMESPACE_ERR
import torch
import numpy as np

#tensor Initialization
print("tensor Initialization\n")
data = [[1,2], [3,4]]
x_data = torch.tensor(data)

np_array = np.array(data)
x_np = torch.from_numpy(np_array)

x_ones = torch.ones_like(x_data)
print(f"Ones Tesor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand}  \n")

shape = (2, 3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor} \n")

# tensor Attribute
print("tensor Attribute \n")
tensor = torch.rand(3,4)

print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

#tensor Operation
print("tensor Operation")
if torch.cuda.is_available():
    tensor = tensor.to('cuda')
    print(f"Device tensor is stored on: {tensor.device}")

tensor = torch.ones(4,4)
tensor[:,1] = 0
print(tensor)

t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)

#요소별 곱(element-wise product)을 계산합니다.
print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")
#다른 문법:
print(f"tensor * tensor \n {tensor * tensor}")

#matmul
print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
#다른 문법:
print(f"tensor @ tensor.T \n {tensor @ tensor.T}")

#inplace 연산
print(tensor, "\n")
tensor.add_(5)
print(tensor)


#NumPy 변환 (Bridge)
print("NumPy 변환\n")
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

t.add_(1)
print(f"t: {t}")
print(f"n: {n}")

#NumPy array to tensor

n = np.ones(5)
t = torch.from_numpy(n)

np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")



















