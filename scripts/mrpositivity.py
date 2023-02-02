from modules.shared import opts
from modules.processing import Processed, process_images, images
import modules.scripts as scripts
import gradio as gr
import random

class Script(scripts.Script):
    def title(self):
        return "Mr. Positivity"

    def ui(self, is_img2img):
        enable_m = gr.Checkbox(label="Enable Mr. Positivity (needs negative prompts)", value=True, elem_id=self.elem_id("enable"))
        weight = gr.Slider(label="Mr. Positivity's optimism", minimum=0, mmaximum=100, value=50, step=1, elem_id=self.elem_id("weight"))
       
        return [enable_m,weight]

    def run(self, p,enable_m,weight):
        all_prompts = []
        infotexts = []

        if (enable_m==True):

            initial_positive =  p.prompt
            initial_positive = initial_positive.replace(",", ", ")
            initial_positive = initial_positive.replace("  "," ")
            words_pos = initial_positive.split()
            initial_neg = p.negative_prompt
            initial_neg = initial_neg.replace(",", ", ")
            initial_neg = initial_neg.replace("  "," ")
            words_neg = initial_neg.split()
 
            p.prompt = ""
            p.negative_prompt = ""

            #drops positive
            for i, word in enumerate(words_pos):
                if random.random() > weight/100.0:
                    p.prompt  = p.prompt +" "+ word

            for i, word in enumerate(words_neg):
                if random.random() < weight/100.0:
                    p.prompt = p.prompt+" "+ word
                else:
                    p.negative_prompt = p.negative_prompt+" "+ word    


        proc = process_images(p)

        all_prompts = proc.all_prompts
        infotexts = proc.infotexts

        return Processed(p, proc.images, p.seed, "",all_prompts=all_prompts,infotexts=infotexts)
