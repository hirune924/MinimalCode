import torch
import torch.nn as nn
import torch.nn.functional as F


class Block(nn.Module):

    """A convolution, batch norm, ReLU block.

    A block in a feedforward network that performs a
    convolution followed by batch normalization followed
    by a ReLU activation.

    For the convolution operation, a square filter size is used.

    Args:
        out_channels (int): The number of output channels.
        ksize (int): The size of the filter is ksize x ksize.
        pad (int): The padding to use for the convolution.

    """

    def __init__(self, in_channels, out_channels, ksize, pad=1):
        super(Block, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=ksize, stride=1, padding=pad, bias=False)
        self.bn = nn.BatchNorm2d(out_channels)
        
    def forward(self, x):
        out = self.conv(x)
        out = self.bn(out)
        return F.relu(out)
    
class VGG(nn.Module):

    """A VGG-style network for very small images.

    This model is based on the VGG-style model from
    http://torch.ch/blog/2015/07/30/cifar.html
    which is based on the network architecture from the paper:
    https://arxiv.org/pdf/1409.1556v6.pdf

    This model is intended to be used with either RGB or greyscale input
    images that are of size 32x32 pixels, such as those in the CIFAR10
    and CIFAR100 datasets.

    On CIFAR10, it achieves approximately 89% accuracy on the test set with
    no data augmentation.

    On CIFAR100, it achieves approximately 63% accuracy on the test set with
    no data augmentation.

    Args:
        class_labels (int): The number of class labels.

    """

    def __init__(self, class_labels=10):
        super(VGG, self).__init__()
        
        self.block1_1 = Block(3, 64, 3)
        self.block1_2 = Block(64, 64, 3)
        self.block2_1 = Block(64, 128, 3)
        self.block2_2 = Block(128, 128, 3)
        self.block3_1 = Block(128, 256, 3)
        self.block3_2 = Block(256, 256, 3)
        self.block3_3 = Block(256, 256, 3)
        self.block4_1 = Block(256, 512, 3)
        self.block4_2 = Block(512, 512, 3)
        self.block4_3 = Block(512, 512, 3)
        self.block5_1 = Block(512, 512, 3)
        self.block5_2 = Block(512, 512, 3)
        self.block5_3 = Block(512, 512, 3)
        
        self.fc1 = nn.Linear(512, 512, bias=False)
        self.bn_fc1 = nn.BatchNorm1d(512)
        self.fc2 = nn.Linear(512, class_labels, bias=False)

    def forward(self, x):
        # 64 channel blocks:
        h = self.block1_1(x)
        h = F.dropout(h, p=0.3)
        h = self.block1_2(h)
        h = F.max_pool2d(h, kernel_size=2, stride=2)

        # 128 channel blocks:
        h = self.block2_1(h)
        h = F.dropout(h, p=0.4)
        h = self.block2_2(h)
        h = F.max_pool2d(h, kernel_size=2, stride=2)

        # 256 channel blocks:
        h = self.block3_1(h)
        h = F.dropout(h, p=0.4)
        h = self.block3_2(h)
        h = F.dropout(h, p=0.4)
        h = self.block3_3(h)
        h = F.max_pool2d(h, kernel_size=2, stride=2)

        # 512 channel blocks:
        h = self.block4_1(h)
        h = F.dropout(h, p=0.4)
        h = self.block4_2(h)
        h = F.dropout(h, p=0.4)
        h = self.block4_3(h)
        h = F.max_pool2d(h, kernel_size=2, stride=2)

        # 512 channel blocks:
        h = self.block5_1(h)
        h = F.dropout(h, p=0.4)
        h = self.block5_2(h)
        h = F.dropout(h, p=0.4)
        h = self.block5_3(h)
        h = F.max_pool2d(h, kernel_size=2, stride=2)

        h = F.dropout(h, p=0.5)
        h = h.view(h.size(0), -1)
        h = self.fc1(h)
        h = self.bn_fc1(h)
        h = F.relu(h)
        h = F.dropout(h, p=0.5)
        return self.fc2(h)