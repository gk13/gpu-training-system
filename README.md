# GPU Training System for Qwen-2.5-VL 
## Setup
1. **Cluster**: `./cluster_setup/create_cluster.sh`
2. **GPU Operator**: `./cluster_setup/install_gpu_operator.sh`
3. **Storage**: `./storage/create_disk.sh && kubectl apply -f storage/`
4. **Pull Model**:
   - Run `./cluster_setup/pull_model.sh` to pull Qwen-2.5-VL to `/data/qwen_model`.
   - Creates a pod with `huggingface/transformers-pytorch-gpu`, pulls the model, and saves it to the PVC.
