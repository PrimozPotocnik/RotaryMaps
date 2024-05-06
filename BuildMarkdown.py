import mistletoe
from mistletoe.html_renderer import HtmlRenderer
from mistletoe.latex_renderer import LaTeXRenderer
import os
import shutil

class MathJaxRenderer(HtmlRenderer, LaTeXRenderer):
  def __init__(self, **kwargs):
    """
    Args:
      **kwargs: additional parameters to be passed to the ancestors'
            constructors.
    """
    super().__init__(**kwargs)

  mathjax_src = '<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-MML-AM_CHTML"></script>\n'

  def render_math(self, token):
    """
    Convert single dollar sign enclosed math expressions to the ``\\(...\\)`` syntax, to support
    the default MathJax settings which ignore single dollar signs as described at
    https://docs.mathjax.org/en/latest/basic/mathematics.html#tex-and-latex-input.
    """
    if token.content.startswith('$$'):
      return self.render_raw_text(token)
    return '\\({}\\)'.format(self.render_raw_text(token).strip('$'))

  def render_document(self, token):
    """
    Append CDN link for MathJax to the end of <body>.
    """
    return super().render_document(token) + self.mathjax_src


def CreateHtml(path: str):
  with open(path, "rt") as fin: rendered = mistletoe.markdown(fin, MathJaxRenderer)
  newFile = ".".join(path.split(".")[:-1])+".html";
  # print(f"Creating for {newFile}. Content length: {len(rendered)}")
  with open(newFile, "wt") as fout: 
    fout.write(f"""<!DOCTYPE html><html class="gist"><head><link rel="stylesheet" href="https://primozpotocnik.github.io/RotaryMaps/github-css.css"></head><body class="markdown-body">{rendered}</body></html>""")


def Walk(path: str):
  for root, dirs, files in os.walk(path):
    for file in files:
      if file.endswith('.md'): 
        CreateHtml(os.path.join(root, file))
    for folder in dirs: 
      Walk(os.path.join(root, folder));
      # print(f"Wandering into {os.path.join(root, folder)}")

if __name__ == "__main__":
  Walk("files/")
  shutil.copytree("./files", "./_site/files")
  shutil.copyfile("./index.html", "./_site/index.html")
  shutil.copyfile("./style.css", "./_site/style.css")
  shutil.copyfile("./github-css.css", "./_site/github-css.css")
