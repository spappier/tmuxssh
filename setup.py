from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

setup(
    name='tmuxssh',
    author='Santiago Pappier',
    author_email='spappier@gmail.com',
    url='http://github.com/spappier/tmuxssh',
    version='1.1.0',
    description='ssh into several hosts at once using tmux',
    long_description=readme,
    license='MIT',
    entry_points=dict(console_scripts=['tmuxssh = tmuxssh:main']),
    py_modules=['tmuxssh'],
    scripts=['tmuxssh.py'],
    install_requires=['docopt'],
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
