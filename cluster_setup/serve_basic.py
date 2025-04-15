from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
import torch
import time
import os

os.environ["PYTHONUNBUFFERED"] = "1"

model_path = "/app/qwen_model"
print(f"Checking model path: {model_path}", flush=True)
if not os.path.exists(model_path):
    print(f"Error: {model_path} does not exist", flush=True)
    exit(1)
print(f"Files in model directory: {os.listdir(model_path)}", flush=True)

print("Loading model...", flush=True)
model = Qwen2VLForConditionalGeneration.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    local_files_only=True
).to("cuda")
print("Model loaded", flush=True)

print("Loading processor...", flush=True)
processor = AutoProcessor.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct",
    local_files_only=False
)
print("Processor loaded", flush=True)

def infer(text, image_path=None):
    start = time.time()
    inputs = processor(text=text, images=image_path, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs)
    end = time.time()
    print(f"Inference time: {end - start}s", flush=True)
    return outputs

# Read prompt from file
prompt_file = "/app/prompt.txt"
while True:
    if os.path.exists(prompt_file):
        with open(prompt_file, "r") as f:
            prompt = f.read().strip()
        if prompt:
            print(f"Running inference for prompt: {prompt}", flush=True)
            infer(prompt)
            # Clear file to avoid re-running same prompt
            os.remove(prompt_file)
    print("Ready for inference...", flush=True)
    time.sleep(1)