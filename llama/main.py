import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import requests
from io import BytesIO

url = "https://huggingface.co/qresearch/llama-3-vision-alpha-hf/resolve/main/assets/demo-2.jpg"
response = requests.get(url)
image = Image.open(BytesIO(response.content))

model = AutoModelForCausalLM.from_pretrained(
    "qresearch/llama-3.1-8B-vision-378",
    trust_remote_code=True,
    torch_dtype=torch.float16,
).to("cuda")

tokenizer = AutoTokenizer.from_pretrained("qresearch/llama-3.1-8B-vision-378", use_fast=True)

print(
    model.answer_question(
        image, "Briefly describe the image", tokenizer, max_new_tokens=128, do_sample=True, temperature=0.3
    ),
)
