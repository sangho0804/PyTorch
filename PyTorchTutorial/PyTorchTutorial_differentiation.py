import torch

## 1
# AUTOMATIC DIFFERENTIATION WITH TORCH.AUTOGRAD

x = torch.ones(5)  # input tensor
y = torch.zeros(3)  # expected output
w = torch.randn(5, 3, requires_grad=True)
b = torch.randn(3, requires_grad=True)
z = torch.matmul(x, w)+b
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)

#debug 1.
print("## AUTOMATIC DIFFERENTIATION WITH TORCH.AUTOGRAD.")
print(f"n: {loss}")
print(loss)
print()
print(f"Gradient function for z = {z.grad_fn}")
print(f"Gradient function for loss = {loss.grad_fn}")
print()

## 2
# Computing Gradients

loss.backward()
print("## Computing Gradients.")
print(w.grad)
print(b.grad)
print()

## 3
# Disabling Gradient Tracking

print("## Disabling Gradient Tracking.")
z = torch.matmul(x, w)+b
print(z.requires_grad)

with torch.no_grad():
    z = torch.matmul(x, w)+b
print(z.requires_grad)

z = torch.matmul(x, w)+b
z_det = z.detach()
print(z_det.requires_grad)
print()

## 4
# Optional Reading

print("## Optional Reading.")

inp = torch.eye(5, requires_grad=True)
out = (inp+1).pow(2)
out.backward(torch.ones_like(inp), retain_graph=True)
print(f"First call\n{inp.grad}")
out.backward(torch.ones_like(inp), retain_graph=True)
print(f"\nSecond call\n{inp.grad}")
inp.grad.zero_()
out.backward(torch.ones_like(inp), retain_graph=True)
print(f"\nCall after zeroing gradients\n{inp.grad}")












