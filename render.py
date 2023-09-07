import os
import shutil

import jinja2

TEMPLATE_DIR = "./templates"
OUTPUT_DIR = "./dist"
BASE_DIR = os.getcwd()

env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
tmpls = [x for x in os.walk(TEMPLATE_DIR)][0][2]
for tmpl in tmpls:
    template = env.get_template(tmpl)
    with open(os.path.join(OUTPUT_DIR, tmpl), "w") as f:
        f.write(template.render())

shutil.copytree(os.path.join(BASE_DIR, "assets"), os.path.join(OUTPUT_DIR, "static"), dirs_exist_ok=True)