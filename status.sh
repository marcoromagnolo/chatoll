#!/bin/bash

NOT_RUN="Application not running."
if [ -f chatoll.pid ]; then
    PID=$(cat chatoll.pid)
    if kill -0 "$PID" 2>/dev/null; then
        ps -p "$PID" -o pid,ppid,cmd,%cpu,%mem,stime,user,time
    else
        echo $NOT_RUN
    fi
else
    echo $NOT_RUN
fi