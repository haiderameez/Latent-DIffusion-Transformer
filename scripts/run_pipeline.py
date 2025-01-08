from diffusers import StableDiffusionPipeline
import torch

model_id = "stable-diffusion-v1-5/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype = torch.float16)
pipe.to("cpu")