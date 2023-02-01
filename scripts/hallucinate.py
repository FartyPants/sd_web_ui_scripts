from modules.shared import opts, cmd_opts, state
from modules.processing import Processed, StableDiffusionProcessingImg2Img, process_images, images
import modules.scripts as scripts
import gradio as gr
from random import randint

class Script(scripts.Script):
    def title(self):
        return "Hallucinate"

    def ui(self, is_img2img):
        enable_m = gr.Checkbox(label="Yes please, Hallucinate", value=True, elem_id=self.elem_id("enable"))
       
        return [enable_m]

    def run(self, p,enable_m):
       
        initial_prompt =  p.prompt
        p.prompt = p.negative_prompt
        p.negative_prompt = initial_prompt
        proc = process_images(p)

        return Processed(p, proc.images, p.seed, "")
