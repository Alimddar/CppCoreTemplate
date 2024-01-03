#!/bin/bash

RESET_SCRIPT_PATH="/Users/alimdar/Desktop/Coding/c++/py-sc/reset.py"
RUN_SCRIPT_PATH="/Users/alimdar/Desktop/Coding/c++/py-sc/run.py"

if [ $# -lt 2 ]; then
    echo "Usage: $0 [reset|run] [1|2|3]"
    exit 1
fi

COMMAND=$1
CHOICE=$2

case $COMMAND in
    reset)
        python3 "$RESET_SCRIPT_PATH" $CHOICE
        ;;
    run)
        python3 "$RUN_SCRIPT_PATH" $CHOICE
        ;;
    *)
        echo "Invalid command. Use 'reset' or 'run'."
        exit 1
        ;;
esac
