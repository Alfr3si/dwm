#!/bin/bash

DIR="$HOME/.dwm/dwm/dwmbar/scripts/"
while [[ true ]]; do
	mem="$($DIR/memory)"
	vol=$($DIR/volume)
	key=$($DIR/keymap)
	bat=$($DIR/battery)
	clock=$($DIR/clock2)
	xsetroot -name "$mem $vol $key $bat $clock"
	sleep 1
done
