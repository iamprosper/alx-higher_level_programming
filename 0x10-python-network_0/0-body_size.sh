#!/usr/bin/env bash
# This file get the body size
curl -si "$1" | grep "Content-Length" | awk '{print $2}'
