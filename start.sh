#!/bin/bash
tmux new-session -d -s bean-counter '/usr/local/bin/python3.9 /home/loki/bean-counter/bean_counter.py'
