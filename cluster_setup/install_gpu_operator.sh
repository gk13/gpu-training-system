#!/bin/bash
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
helm repo update
kubectl create namespace gpu-operator || true
helm install gpu-operator nvidia/gpu-operator \
  --namespace gpu-operator \
  --wait \
  --set node-feature-discovery.priorityClassName=gpu-operator-priority \
  --set operator.priorityClassName=gpu-operator-priority \
  --set node-feature-discovery.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[0].preference.matchExpressions[0].key=node-role.kubernetes.io/control-plane \
  --version 25.3.0 \