#!/usr/bin/env python3
# coding: utf-8

import sys
import argparse
import time
from js8net import *

########
### Based upon js8net example.py
########
def ghostmode(args, js8host, js8port, enable_auto):
    if args.verbose:
        print("Connecting to JS8Call...")
    start_net(js8host,js8port)
    if args.verbose:
        print("Connected.")
        print("Call: ",get_callsign())
        print("Grid: ",get_grid())
        print("Info: ",get_info())
        print("Freq: ",get_freq())
        print("Speed: ",get_speed())
    queue_message({"params":{},"type":"MODE.ENABLE_AUTO","value":enable_auto})
    time.sleep(10)
    while tx_queue.qsize() > 1:
        time.sleep(1.0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="verbose print output", action="store_true")
    parser.add_argument("--host", nargs=1, help="hostname or IP running JS8Call (defaults to localhost)");
    parser.add_argument("--port", nargs=1, type=int, help="port number for JS8Call (defaults to 2442)")
    parser.add_argument("--enable_auto", required=True, type=int, choices=[0,1], help="0 to disable auto TX, 1 to enable auto TX")
    args = parser.parse_args();
    
    js8host="localhost"
    js8port=2442
    
    if args.host:
        js8host = args.host[0]
        if args.verbose:
            print(f"Setting Host: {js8host}")
    if args.port:
        js8port = int(args.port[0])
        if args.verbose:
            print(f"Setting Port: {js8port}")
    
    ghostmode(args, js8host, js8port, f"{args.enable_auto}")
