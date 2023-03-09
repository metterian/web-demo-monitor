#! /bin/bash

. /home/joon/miniconda3/etc/profile.d/conda.sh
conda init zsh
conda activate server
cd /home/joon/server-status
python /home/joon/server-status/update.py
