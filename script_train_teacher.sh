#!/bin/bash

python train_teachers.py --train_dir checkpoints \
       			 --data_dir RAW_DATA \
			 --dataset mnist \
			 --max_steps 150 \
			 --nb_labels 10 \
			 --nb_teachers 123 \
			 --teacher_id 0
