#!/bin/bash
NUM_PROC=6
shift
torchrun --nproc_per_node=$NUM_PROC train.py "$@"

