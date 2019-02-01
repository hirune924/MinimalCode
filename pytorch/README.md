# Dataset & DataLoader
## Prepare Data
1. Download data from this competition site

    https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition

2. move those to subdirectory named data/ and unzip

## Prepare Data from CLI
```
pip install kaggle-cli
kg download -u <username> -p <password> -c dogs-vs-cats-redux-kernels-edition
rm *.csv
mkdir data
mv *.zip data/
unzip data/train.zip -d data/
unzip data/test.zip -d data/
```

# Train
## Pre Trained models
* https://github.com/pytorch/vision
* https://github.com/Cadene/pretrained-models.pytorch


# Inference

# Learning Rate Scheduler
* Cosine Annealing

    https://arxiv.org/abs/1608.03983


# Mixed Precision Training (Apex)
* NVIDIA apex

    https://github.com/NVIDIA/apex

    https://nvidia.github.io/apex/

* Install
```
git clone https://www.github.com/nvidia/apex
cd apex
python setup.py install [--cuda_ext] [--cpp_ext]
```

# TensorboardX
* install
```
pip install tensorboardX
``` 
* Start Tensorboard
```
tensorboard --logdir=logs/
```