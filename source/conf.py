project = "Python&图像处理教程"

#copyright = ''
# author = 'Will Wang'

# The full version, including alpha/beta/rc tags
# release = '1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark','sphinx_markdown_tables','sphinx_sitemap', 'sphinx_multiversion']

language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []



#html_theme = 'furo'
#html_theme = 'sphinx_book_theme'
#html_theme = 'insipid'
html_theme = 'sphinx_rtd_theme'

#html_permalinks_icon = '§'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# html_static_path = ['_static']


# The suffix of source filenames.
#source_parsers = {
#   '.md': 'recommonmark.parser.CommonMarkParser',
#}
source_suffix = ['.rst','.md']

master_doc = 'index'

# -- Options for LaTeX output ---------------------------------------------

# 注：在生成html的时候这句话要注释
# latex_engine = 'xelatex'

latex_elements={# The paper size ('letterpaper' or 'a4paper').
'papersize':'letterpaper',
# The font size ('10pt', '11pt' or '12pt').
'pointsize':'12pt',
'classoptions':',oneside',
'babel':'',#必须
'inputenc':'',#必须
'utf8extra':'',#必须
# Additional stuff for the LaTeX preamble.
'preamble': r"""
\usepackage{xeCJK}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
\setCJKmainfont{WenQuanYi Micro Hei}
\setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
\setCJKfamilyfont{song}{WenQuanYi Micro Hei}
\setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
"""}
