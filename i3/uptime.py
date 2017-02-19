#!/usr/bin/python
# -*- coding:utf-8 -*-
from datetime import timedelta

with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime = str(timedelta(seconds = uptime_seconds))

print('['+uptime[0:7]+']')
