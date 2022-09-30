import os
import glob
from jinja2 import Environment, FileSystemLoader

# Create the jinja2 environment.
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

# Find all files with the j2 extension in the current directory
templates = glob.glob('templates/*.md')

def render_template(filename):
    return env.get_template(filename).render(
        APP1='Mantra API',
        APP1_STATUS='label-danger',
        APP1_STATUS_DESCRIPTION='Filed to complie or test'
    )

for f in templates:
    rendered_string = render_template(f)
    print(rendered_string)
