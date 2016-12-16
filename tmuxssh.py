#!/usr/bin/env python
'''
tmuxssh

Usage:
  tmuxssh [--template=<template>] <host>...
  tmuxssh --version
  tmuxssh -h | --help
'''

import subprocess
import os
import docopt


class TmuxSession(object):

    def __init__(self, session_name):
        self._session_name = session_name
        self.tmux('new-session', '-ds', self._session_name)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.kill_session()

    def tmux(self, *args):
        return subprocess.call(['tmux'] + list(args))

    def split_window(self, command):
        self.tmux('split-window', '-t', self._session_name, command)

    def select_layout(self, layout):
        self.tmux('select-layout', '-t', self._session_name, layout)

    def attach(self):
        self.tmux('attach', '-t', self._session_name)

    def set_window_option(self, option, value):
        self.tmux('set-window-option', '-t', self._session_name, option, value)

    def kill_pane(self, n):
        self.tmux('kill-pane', '-t', str(n))

    def kill_session(self):
        self.tmux('kill-session', '-t', self._session_name)


def tmux_commands(commands):
    with TmuxSession('tmux-{}'.format(os.getpid())) as tmux:
        for command in commands:
            tmux.split_window(command)
            tmux.select_layout('tiled')
        tmux.kill_pane(0)
        tmux.select_layout('tiled')
        tmux.set_window_option('synchronize-panes', 'on')
        tmux.attach()


def ssh_command(host, template='ssh {}'):
    return template.format(host)


def main():
    args = docopt.docopt(__doc__, version='1.1.0')
    hosts = (h for host in args.get('<host>') for h in host.split())
    template = args.get('--template')
    commands = (ssh_command(host, template) for host in hosts)
    tmux_commands(commands)


if __name__ == '__main__':
    main()
