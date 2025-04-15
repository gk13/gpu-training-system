# GPU Training System for Qwen-2.5-VL

## Overview
Deploys Qwen-2.5-VL-2B-Instruct on a 2-GPU GKE cluster, mimicking Convergence AI’s Proxy. Uses `transformers` for baseline and vLLM for optimized inference.

## Setup
1. **Cluster**:
   - Run `./cluster_setup/create_cluster.sh` (assumed completed).
   - GKE 1.31.6, 2 nodes, 1 T4 GPU each.
2. **GPU Operator**:
   - Run `./cluster_setup/install_gpu_operator.sh` (assumed completed).
3. **Storage**:
   - Create GCE Persistent Disk: `./storage/create_disk.sh`.
   - Apply PV/PVC: `kubectl apply -f storage/pv.yaml -f storage/pvc.yaml`.
4. **GCS Storage**:
   - Upload model to GCS:
     ```bash
     gsutil mb -p gpu-distributed-training -l europe-west2 gs://gpu-training-uied-data-gk-2025
     gsutil -m cp -r ./qwen_model gs://gpu-training-uied-data-gk-2025/
     ```
5. **Deploy Baseline (transformers):**
   - Build and push Docker image:
     ```bash
     cd cluster_setup
     docker build --platform linux/amd64 -f Dockerfile-basic -t gcr.io/gpu-distributed-training/qwen-basic:latest .
     docker push gcr.io/gpu-distributed-training/qwen-basic:latest
     ```
   - Deploy:
     ```bash
     kubectl apply -f cluster_setup/qwen-basic.yaml
     ```
   - Measure inference time by writing a prompt to /app/prompt.txt:
     ```bash
      kubectl exec -it qwen-basic-<hash> -n training -- sh -c "echo 'Test prompt' > /app/prompt.txt"
      kubectl logs -f qwen-basic-<hash> -n training  
     ```

## Observed Results  

- **Inference Time (Baseline without vLLM)**:
  - Pod 1: **2.2101476192474365** seconds for "Test prompt".
  - Pod 2: **2.307887554168701** seconds for "Test prompt".
  - Measured on two T4 GPUs with FP16 precision, using transformers for Qwen-2.5-VL-2B-Instruct.   
    
