#!/bin/bash
gcloud container clusters create gpu-cluster \
  --zone europe-west2-b \
  --machine-type n1-standard-4 \
  --accelerator type=nvidia-tesla-t4,count=1 \
  --num-nodes 2 \
  --preemptible \
  --project gpu-distributed-training \
  --enable-ip-alias \
  --cluster-version 1.31
