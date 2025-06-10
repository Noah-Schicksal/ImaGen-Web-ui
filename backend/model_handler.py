from diffusers import StableDiffusionPipeline
import torch
import uuid

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

def generate_image(prompt, negative_prompt, width, height):
    image = pipe(prompt=prompt, negative_prompt=negative_prompt, width=width, height=height).images[0]
    filename = f"outputs/{uuid.uuid4().hex}.png"
    image.save(filename)
    return filename
