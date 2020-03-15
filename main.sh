#!/bin/bash
while [[ 1 ]]
do
	cd /home/gonzalo/finance
	source /home/gonzalo/Codes/venv/bin/activate
	python main.py
	deactivate
	sleep 3600
done

