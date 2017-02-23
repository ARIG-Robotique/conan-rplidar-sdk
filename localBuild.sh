#!/bin/bash

export CONAN_UPLOAD=1
export CONAN_USERNAME=gdepuille
export CONAN_REFERENCE=RPLidarSDK/1.5.7
export CONAN_CHANNEL=stable
export CONAN_PASSWORD=$1

python build.py -s arch=x86_64
