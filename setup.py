#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
import shutil

from setuptools import Command, setup


VERSION = '1.2.0'


#  https://github.com/kennethreitz/setup.py
class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            shutil.rmtree(
                os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dist')
            )
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(VERSION))
        os.system('git push --tags')

        sys.exit()


setup(
    name='tmuxssh',
    version=VERSION,
    description='SSH into several hosts at once using tmux',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Santiago Pappier',
    author_email='spappier@gmail.com',
    url='https://github.com/spappier/tmuxssh',
    py_modules=['tmuxssh'],
    entry_points={'console_scripts': ['tmuxssh = tmuxssh:main']},
    install_requires=['click>=6.7'],
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    cmdclass={'upload': UploadCommand},
)
