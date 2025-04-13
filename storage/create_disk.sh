#!/bin/bash
gcloud compute disks create data-disk \
  --size=100GB \
  --zone=europe-west2-b \
  --project gpu-distributed-training \
  --type=pd-ssd