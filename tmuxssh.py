#!/usr/bin/env python
'''
tmuxssh

Usage:
  tmuxssh [--template=<template>] [--paginate=<per-page>] <host>...
  tmuxssh --version
  tmuxssh -h | --help
'''

import subprocess
import os

import docopt


class TmuxSession(object):
    def __init__(self, name):
        self.name = name
        self.tmux('new-session', '-ds', self.name)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.kill_session()

    def tmux(self, command, *args):
        return subprocess.call(('tmux', command) + args)

    def new_window(self, command):
        self.tmux('new-window', '-at', self.name, command)

    def split_window(self, command):
        self.tmux('split-window', '-t', self.name, command)

    def previous_window(self):
        self.tmux('previous-window', '-t', self.name)

    def select_layout(self, layout):
        self.tmux('select-layout', '-t', self.name, layout)

    def attach(self):
        self.tmux('attach', '-t', self.name)

    def set_window_option(self, option, value):
        self.tmux('set-window-option', '-t', self.name, option, value)

    def kill_window(self, target):
        self.tmux('kill-window', '-t', '{}:{}'.format(self.name, target))

    def kill_session(self):
        self.tmux('kill-session', '-t', self.name)


def tmux_commands(commands, per_page):
    if per_page == 0:
        per_page = len(commands)

    session_name = 'tmux-{}'.format(os.getpid())

    with TmuxSession(session_name) as tmux:
        for n, command in enumerate(commands):
            if n % per_page == 0:
                tmux.new_window(command)
                tmux.set_window_option('synchronize-panes', 'on')
            else:
                tmux.split_window(command)
                tmux.select_layout('tiled')

        # kill default window created with the session
        tmux.kill_window(1)

        # switch to the first window the long way around so that on closing
        # a window the next one (and not the previous one) is shown
        # tmux switches to the last visited window on close
        for _ in range(len(commands) // per_page):
            tmux.previous_window()

        tmux.attach()


def main():
    args = docopt.docopt(__doc__, version='1.2.0')
    hosts = (h for host in args.get('<host>') for h in host.split())
    template = args.get('--template') or 'ssh {}'
    paginate = int(args.get('--paginate') or 0)
    command = template.format

    try:
        commands = [command(host) for host in hosts]
        tmux_commands(commands, per_page=paginate)
    except EnvironmentError:
        print('You need to install tmux.')


if __name__ == '__main__':
    main()
