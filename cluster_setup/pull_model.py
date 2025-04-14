from transformers import Qwen2VLForConditionalGeneration
import torch

def pull_qwen_model(save_path):
    print(f"Pulling Qwen-2.5-VL model to {save_path}...")
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        'Qwen/Qwen2-VL-2B-Instruct',
        torch_dtype='float16'
        )
    model.save_pretrained(save_path)
    print(f"Model saved to {save_path}")

if __name__ == "__main__":
    pull_qwen_model("/data/qwen_model")
