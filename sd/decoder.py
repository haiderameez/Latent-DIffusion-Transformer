import torch
from torch import nn
from torch.nn import functional as F
from attention import SelfAttention

class VAE_AttnetionBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init()
        self.groupnorm_1 = nn.GroupNorm(32, in_channels)
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1)

        self.groupnorm_2 = nn.GroupNorm(32, out_channels)
        self.conv2 = nn.conv2d(in_channels, out_channels, kernel_size=3, padding=1)
        