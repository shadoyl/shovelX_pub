#!/bin/bash env

# CentOS7 Server setup from base

# Setting up git version control
sudo yum install -y git
sudo yum install -y \
 gettext-devel\
 openssl-devel\
 perl-CPAN\
 perl-devel\
 zlib-devel
echo "TEST git version:"
git --version

# Setting up Python3.6 dependencies:
 sudo yum install -y update &&\
  sudo yum -y upgrade &&\ 
  sudo yum -y install yum-utils &&\
  sudo yum -y groupinstall development\
  sudo yum install -y \
  https://centos7.iuscommunity.org/ius-release.rpm\
  sudo yum install -y python36u\
echo "TEST Python version installed:"
python3.6 -V


# Setting up Pip package manager for python36
sudo yum install -y python36u-pip\
sudo yum install -y python36u-devel
echo "TEST pip package manager installed at:"
which pip3.6

sudo yum install -y wget
sudo yum install -y update

which python3.6
which pip
which pip3

# Run the following after setting up the virtual environment to get rid of the nss/openssl backend error:
# pip3.6 uninstall pycurl &&\
#    export PYCURL_SSL_LIBRARY=nss &&\
#    pip3.6 install pycurl --no-cache-dir

# Setting up Python3 virtualenv: [repo access needs to be fixed]
cd ~ &&\
 mkdir shovelProject &&\
 cd shovelProject
python3.6 -m venv venvPy3.6-shovelX && source venvPy3.6-shovelX/bin/activate &&\
 cd shovelProject && git clone repo