import sys
from setuptools import setup


setup_requires = []
if sys.argv[-1] in ('sdist', 'bdist_wheel'):
    setup_requires.append('setuptools-markdown')


setup(
    name='tmuxssh',
    author='Santiago Pappier',
    author_email='spappier@gmail.com',
    url='http://github.com/spappier/tmuxssh',
    version='1.0',
    description='ssh into several hosts at once using tmux',
    long_description_markdown_filename='README.md',
    license='MIT',
    entry_points=dict(console_scripts=['tmuxssh = tmuxssh:main']),
    py_modules=['tmuxssh'],
    scripts=['tmuxssh.py'],
    install_requires=['docopt'],
    setup_requires=setup_requires,
    keywords='tmux ssh',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ]
)
