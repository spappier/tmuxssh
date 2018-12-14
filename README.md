# tmuxssh

SSH into several hosts at once using tmux

## Install

```bash
pip install --user --upgrade tmuxssh
```

## Usage

```
Usage: tmuxssh [OPTIONS] [HOSTS]...

Options:
  --template TEXT     Connection template, default: ssh {}.
  --paginate INTEGER  Panes per tmux window, default: 0.
  --help              Show this message and exit.
```

## Examples

```bash
tmuxssh --template 'ssh -i ~/.ssh/my.pem -l ubuntu {}' 10.64.93.208 10.64.93.207
tmuxssh --template 'ssh -i ~/.ssh/my.pem -l ubuntu {}' --paginate 5 $(easytwo --name es-nodes --output public-ip)
tmuxssh --template 'ssh -ti ~/.ssh/jump.pem 10.1.1.1 "ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ~/.ssh/another.pem -l ubuntu {}"' 10.64.93.208 10.64.93.207
```
