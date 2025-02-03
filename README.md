# Latent-DIffusion-Transformer

This is an implementation of Latent Diffusion Model from scratch.

## Usage Guide

### 1. Download the Repository

### 2. Install all the dependencies using the following line of code:
```python
pip install -r requirements.txt
```

### 3. Download pretrained weights and tokenizer files
- Download `vocab.json` and `merges.txt` from https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5/tree/main and save them in the data folder in the root directory.
- Similarly, also the donwload the pretrained weights `v1-5-pruned-emaonly.ckpt` from the same link and save it in the data folder.

### 2. Open the Notebook  
- Go to the `sd` folder and open the `demo.ipynb` notebook.  

### 3. Text-to-Image Generation  
- Modify the `prompt` variable to specify the image you want to generate.  
- (Optional) Use `uncond_prompt` to exclude certain elements from the generated image.  

### 4. Image-to-Image Generation  
- Create an `images` folder in the root directory.  
- Add your desired image to this folder.  
- Set the `image_path` variable to the relative path of the image.  
- Uncomment the following line:  
  ```input_image = Image.open(image_path)```
- Optimize Performance
  If your system supports CUDA (for NVIDIA GPUs) or MPS (for Apple Silicon), enable faster processing by setting the corresponding constant to True:
  ```ALLOW_CUDA = True  # Enable CUDA for NVIDIA GPUs```
  OR
  ```ALLOW_MPS = True   # Enable MPS for Apple Silicon (M1/M2)```
  
## Huge Thanks to the following repositories
1. https://github.com/CompVis/stable-diffusion/
2. https://github.com/divamgupta/stable-diffusion-tensorflow
3. https://github.com/kjsman/stable-diffusion-pytorch
4. https://github.com/huggingface/diffusers/
5. https://github.com/hkproj/pytorch-stable-diffusion/tree/main
6. https://github.com/haideraqeeb/latent-diffusion/
