# -*- coding: utf-8 -*-
#
# PyTorch documentation build configuration file, created by
# sphinx-quickstart on Fri Dec 23 13:31:47 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# NB: C++ API doc generation using doxygen / breathe / exhale is currently disabled
# due to OOM errors in CI. See https://github.com/pytorch/pytorch/issues/79992

import os
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '3.1.2'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'pytorch': ('https://pytorch.org/docs/master', None)
}

# Setup absolute paths for communicating with breathe / exhale where
# items are expected / should be trimmed by.
# This file is {repo_root}/docs/cpp/source/conf.py
this_file_dir = os.path.abspath(os.path.dirname(__file__))
repo_root = os.path.dirname(  # {repo_root}
    os.path.dirname(          # {repo_root}/docs
        os.path.dirname(      # {repo_root}/docs/cpp
            this_file_dir     # {repo_root}/docs/cpp/source
        )
    )
)

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'cpp'

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'PyTorch'
copyright = '2022, PyTorch Contributors'
author = 'PyTorch Contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# TODO: change to [:2] at v1.0
version = 'master'
# The full version, including alpha/beta/rc tags.
# TODO: verify this works as expected
release = 'master'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pytorch_sphinx_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'canonical_url': 'https://pytorch.org/docs/stable/',
    'pytorch_project': 'docs',
    'collapse_navigation': False,
    'display_version': True,
    'logo_only': True,
}

# NOTE: sharing python docs resources
html_logo = os.path.join(
    repo_root, 'docs', 'source', '_static', 'img', 'pytorch-logo-dark-unstable.png'
)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# NOTE: sharing python docs resources
html_static_path = [os.path.join(repo_root, 'docs', 'cpp', 'source', '_static')]


# Called automatically by Sphinx, making this `conf.py` an "extension".
def setup(app):
    # NOTE: in Sphinx 1.8+ `html_css_files` is an official configuration value
    # and can be moved outside of this function (and the setup(app) function
    # can be deleted).
    html_css_files = ['cpp_theme.css']

    # In Sphinx 1.8 it was renamed to `add_css_file`, 1.7 and prior it is
    # `add_stylesheet` (deprecated in 1.8).
    add_css = getattr(app, 'add_css_file', app.add_stylesheet)
    for css_file in html_css_files:
        add_css(css_file)

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
# htmlhelp_basename = 'PyTorchdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pytorch.tex', 'PyTorch Documentation',
     'Torch Contributors', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'PyTorch', 'PyTorch Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'PyTorch', 'PyTorch Documentation',
     author, 'PyTorch', 'One line description of project.',
     'Miscellaneous'),
]
