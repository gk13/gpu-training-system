#!/bin/bash
echo "Creating qwen-pull pod..."
kubectl apply -f cluster_setup/qwen-pull-pod.yaml
echo "Waiting for pod to be ready..."
kubectl wait --for=condition=Ready pod/qwen-pull -n training --timeout=600s
echo "Copying pull_model.py to pod..."
kubectl cp cluster_setup/pull_model.py training/qwen-pull:/app/pull_model.py
echo "Running model pull..."
kubectl exec -it qwen-pull -n training -- python3 /app/pull_model.py
echo "Verifying model files..."
kubectl exec -it qwen-pull -n training -- ls /data/qwen_model
echo "Cleaning up pod..."
kubectl delete pod qwen-pull -n training