#! /bin/bash

. /home/joon/miniconda3/etc/profile.d/conda.sh
conda init zsh
conda activate server
streamlit run streamlit.py --server.port 9039
