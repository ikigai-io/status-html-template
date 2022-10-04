import os
import sys
import glob
import datetime
from jinja2 import Environment, FileSystemLoader

# Create the jinja2 environment.
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

def render_template(filename):
    listFiles = [os.path.splitext(filename)[0] for filename in reversed(os.listdir('./public/results'))]
    return env.get_template(filename).render(
        APP1=os.environ.get('APP1'),
        APP1_STATUS=os.environ.get('APP1_STATUS'),
        APP2=os.environ.get('APP2'),
        APP2_STATUS=os.environ.get('APP2_STATUS'),
        APP3=os.environ.get('APP3'),
        APP3_STATUS=os.environ.get('APP3_STATUS'),
        data=sorted(listFiles, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'), reverse=True)
    )

original_stdout = sys.stdout # Save a reference to the original standard output
# Find all files with the j2 extension in the current directory
templates = glob.glob('.github/templates/*.md')
for f in templates:
    # rendered_string = render_template(f)
    if f == '.github/templates/status-template.md':
      filename = "./public/results/%s.md" % (os.environ.get('DATE'))
    elif f == '.github/templates/index.md':
      filename = "./index.md"
    else:
      filename = "./public/none"
    with open(filename, 'w') as newFile:
        rendered_string = render_template(f)
        sys.stdout = newFile # Change the standard output to the file we created.
        print(rendered_string)
        sys.stdout = original_stdout #
