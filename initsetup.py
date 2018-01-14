#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:37:01 2018

@author: rurikoimai
"""
wget https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.7.1-cp34-none-linux_x86_64.whl

pip install tensorflow-0.7.1-cp34-none-linux_x86_64.whl
mv tensorflow-0.7.1-cp3{4,5}-none-linux_x86_64.whl
pip install tensorflow-0.7.1-cp35-none-linux_x86_64.whl

virtualenv --system-site-packages
pip install --upgrade virtualenv 


pip install pillow
pip install lxml
pip install jupyter
pip install matplotlib

git clone https://github.com/tensorflow/models.git

