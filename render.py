import os

import jinja2

TEMPLATE_DIR = "./templates"
OUTPUT_DIR = "./dist"

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
tmpls = [x for x in os.walk(TEMPLATE_DIR)][0][2]
for tmpl in tmpls:
    template = env.get_template(tmpl)
    with open(os.path.join(OUTPUT_DIR, tmpl), 'w') as f:
        f.write(template.render())
        
os.system("cp -r ./assets ./dist/static")