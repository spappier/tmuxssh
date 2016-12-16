from setuptools import setup


setup(
    name='tmuxssh',
    author='Santiago Pappier',
    author_email='spappier@gmail.com',
    url='http://github.com/spappier/tmuxssh',
    version='1.0',
    description='ssh into several hosts at once using tmux',
    license='MIT',
    entry_points=dict(console_scripts=['tmuxssh = tmuxssh:main']),
    py_modules=['tmuxssh'],
    scripts=['tmuxssh.py'],
    install_requires=['docopt'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ]
)
