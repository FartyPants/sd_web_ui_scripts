from modules.shared import opts
from modules.processing import Processed, process_images, images
import modules.scripts as scripts
import gradio as gr

class Script(scripts.Script):
    def title(self):
        return "Hallucinate"

    def ui(self, is_img2img):
        enable_m = gr.Checkbox(label="Yes please, Hallucinate about Monsters", value=True, elem_id=self.elem_id("enable"))
       
        return [enable_m]

    def run(self, p,enable_m):
       
        if (enable_m==True):
            initial_prompt =  p.prompt
            p.prompt = p.negative_prompt
            p.negative_prompt = initial_prompt

        proc = process_images(p)

        return Processed(p, proc.images, p.seed, "")
