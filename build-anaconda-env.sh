#!/bin/bash
wget https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-Linux-x86_64.sh -O ~/miniconda.sh 
bash ~/miniconda.sh -b -p $HOME/miniconda 
git clone https://github.com/bmild/nerf.git 
git clone https://github.com/lucas-t-reis/LLFF.git 
cd LLFF 
pip install -r requirements.txt 
cd .. 
cd nerf 
export PATH=$HOME/miniconda/bin:$PATH 
conda env create -f environment.yml 
conda init bash
