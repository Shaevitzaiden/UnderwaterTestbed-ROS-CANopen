#!/bin/bash

device=${1-can0}

bitrate=${1-1000000}

sudo modprobe peak_usb
sudo ip link set $device down
sudo ip link set $device up type can bitrate $bitrate $*
