import torch
if torch.cuda.is_available():
    torch.device('cuda')
    print('cuda')
else:
    torch.device('cpu')
    print('not cuda')