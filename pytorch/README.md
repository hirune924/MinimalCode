# data download
1. Download data from this competition site
https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition
2. move those to subdirectory named data/ and unzip

## from CLI
pip install kaggle-cli
kg download -u <username> -p <password> -c dogs-vs-cats-redux-kernels-edition
rm *.csv
mkdir data
mv *.zip data/ -d data/
unzip data/*.zip -d data/





tensorboard --logdir=logs/
