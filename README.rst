tmuxssh
#######

ssh into several hosts at once using tmux

Installation
============

::

    pip install tmuxssh

Usage
=====

::

    Usage:
      tmuxssh [--template=<template>] [--paginate=<per-page>] <host>...
      tmuxssh --version
      tmuxssh -h | --help

    Options:
      --template=<template>  ssh command template
      --paginate=<per-page>  hosts to show per tmux window
      --version              show version
      -h --help              show this screen

Examples
--------

::

    tmuxssh --template 'ssh -i ~/.ssh/my.pem -l ubuntu {}' 10.64.93.208 10.64.93.207
    tmuxssh --template 'ssh -i ~/.ssh/my.pem -l ubuntu {}' --paginate 5 $(easytwo --name es-nodes --output public-ip)
    tmuxssh --template 'ssh -ti ~/.ssh/jump.pem 10.1.1.1 "ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/another.pem -l ubuntu {}"' 10.64.93.208 10.64.93.207
