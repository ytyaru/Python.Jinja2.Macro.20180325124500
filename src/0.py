from jinja2 import Template, Environment, FileSystemLoader
import pathlib

path_tpl = (pathlib.Path(__file__).parent.parent / 'res/templates').resolve()
env = Environment(loader=FileSystemLoader(str(path_tpl )))
template = env.get_template('py/MyClasses.py')
print(template.render(Name='ZZZ'))
