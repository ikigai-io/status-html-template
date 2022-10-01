import os
import sys
import glob
from jinja2 import Environment, FileSystemLoader

# Create the jinja2 environment.
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

def render_template(filename):
    listFiles = [os.path.splitext(filename)[0] for filename in reversed(os.listdir('./public/results'))]
    return env.get_template(filename).render(
        APP1=os.environ.get('APP1'),
        APP1_STATUS=os.environ.get('APP1_STATUS'),
        APP1_STATUS_DESCRIPTION=os.environ.get('APP1_STATUS_DESCRIPTION'),
        data=sorted(listFiles, reverse=True)
    )

original_stdout = sys.stdout # Save a reference to the original standard output
# Find all files with the j2 extension in the current directory
templates = glob.glob('templates/*.md')
for f in templates:
    # rendered_string = render_template(f)
    if f == 'templates/status-template.md':
      filename = "./public/results/%s.md" % (os.environ.get('DATE'))
    elif f == 'templates/index.md':
      filename = "./public/index.md"
    else:
      filename = "./public/none"
    with open(filename, 'w') as newFile:
        rendered_string = render_template(f)
        sys.stdout = newFile # Change the standard output to the file we created.
        print(rendered_string)
        sys.stdout = original_stdout #
