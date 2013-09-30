#!/usr/bin/python
#   Copyright 2012-2013 STACKOPS TECHNOLOGIES S.L.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import glob
import os
import setuptools
import subprocess
import sys
import unittest

requirements = ['pep8', 'cuisine', 'pyyaml', 'setuptools',
                'python-keystoneclient', 'MySQL-python', 'pika ',
                'expects>=0.1,<0.2', 'sh']

if sys.version_info < (2, 7):
    requirements.append('argparse')
elif sys.version_info < (2, 6):
    raise 'Must use python 2.6 or greater'


setuptools.setup(name='fabuloso',
                 packages=['fabuloso'],
                 author='StackOps',
                 author_email='developers@stackops.com',
                 description='StackOps remote executor',
                 url='https://github.com/StackOps/fabuloso',
                 install_requires=requirements,
                 entry_points={
                     'console_scripts': [
                         'fabuloso = fabuloso.main:main'
                     ]
                 },
                 data_files=[
                     (os.path.join(os.path.expanduser('~'),
                                   '.config/fabuloso/keys'),
                      ['keys/nonsecureid_rsa', 'keys/nonsecureid_rsa.pub']),
                     (os.path.join(os.path.expanduser('~/.config/fabuloso')),
                      ['keys/keys.cfg'])
                 ],
                 version='0.1',
                 license='Apache License 2.0',
                 classifiers=[
                     "Development Status :: 2 - Pre-Alpha",
                     "Environment :: Console",
                     "Intended Audience :: Developers",
                     "Intended Audience :: Information Technology",
                     "License :: OSI Approved :: Apache Software License",
                     "Natural Language :: English",
                     "Operating System :: POSIX :: Linux",
                     "Programming Language :: Python",
                     "Programming Language :: Python :: 2",
                     "Programming Language :: Python :: 2.7",
                     "Topic :: System"
                 ])
