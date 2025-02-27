#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pybricks documentation build configuration file, created by
# sphinx-quickstart on Thu Sep  6 15:31:12 2018.
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
# flake8: noqa

import os
import re
import sys

from docutils import nodes
from docutils.parsers.rst.directives import flag
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx
from sphinx.domains.python import PyClassmember, PythonDomain
import toml

TOP_DIR = os.path.abspath(os.path.join('..', '..'))
sys.path.insert(0, TOP_DIR)
sys.path.append(os.path.abspath('../common/extensions'))

from pybricks.hubs import EV3Brick  # noqa E402
from pybricks.media.ev3dev import Image  # noqa E402
from pybricks._common import Speaker  # noqa E402

# ON_RTD is whether we are on readthedocs.org
# this line of code grabbed from docs.readthedocs.org
ON_RTD = os.environ.get('READTHEDOCS', None) == 'True'

_pyproject = toml.load(os.path.join(TOP_DIR, 'pyproject.toml'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'color',
    'classlink',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../common/_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = "v" + _pyproject["tool"]["poetry"]["version"]
# The short X.Y version.
version = re.match(r'(v\d+\.\d+)', release)[0]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Figure numbering
numfig = True
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section %s'
}

# Find cross-reference errors
nitpicky = True

# https://stackoverflow.com/a/30624034/1976323
nitpick_ignore = [
    ('py:class', 'bool'),
    ('py:class', 'bytearray'),
    ('py:class', 'bytes'),
    ('py:class', 'callable'),
    ('py:class', 'dict'),
    ('py:class', 'float'),
    ('py:class', 'int'),
    ('py:class', 'iter'),
    ('py:class', 'list'),
    ('py:class', 'object'),
    ('py:class', 'str'),
    ('py:class', 'tuple'),
    ('py:exc', 'OSError'),
    ('py:exc', 'RuntimeError'),
    ('py:exc', 'TypeError'),
    ('py:exc', 'ValueError'),
]

# -- Autodoc options ------------------------------------------------------

autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
}
autoclass_content = 'both'  # This ensures init arguments are not ignored
add_module_names = False  # Hide module name

# -- Options for HTML output ----------------------------------------------

if ON_RTD:
    html_theme = 'default'
else:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_context = {
    'disclaimer': _DISCLAIMER,
}

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
   'style_external_links': True,
   'logo_only': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../common/_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

# Don't hyperlink to larger images for scaled images.
html_scaled_image_link = False

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Pybricksdoc'


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
    'preamble': r'''
    \usepackage{CJKutf8}
    \makeatletter
    \fancypagestyle{normal}{
        \fancyhf{}
        \fancyfoot[R]{{\py@HeaderFamily\thepage}}
        \fancyfoot[C]{\raisebox{-7mm}{\tiny %(disclaimer)s}}
        \fancyhead[L]{{\py@HeaderFamily \@title}}
        \fancyhead[R]{{\py@HeaderFamily \py@release}}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
    }
    \fancypagestyle{plain}{
        \fancyhf{}
        \fancyfoot[R]{{\py@HeaderFamily\thepage}}
        \fancyfoot[C]{\raisebox{-7mm}{\tiny %(disclaimer)s}}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
    }
    \makeatother
    ''' % {
        'disclaimer': ' '.join((_DISCLAIMER, '©', copyright)),
    },

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'extraclassoptions': 'openany,oneside',

    'releasename': 'Version',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, ''.join([project, '-v', version, '.tex']), _TITLE,
     author, 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pybricks', 'Pybricks Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Pybricks', 'Pybricks Documentation',
     author, 'Pybricks', 'One line description of project.',
     'Miscellaneous'),
]


# -- .. availability:: directive

class AvailabilityDirective(Directive):
    has_content = True
    option_spec = {
        'movehub': flag,
        'cityhub': flag,
        'technichub': flag,
        'ev3dev-stretch': flag,
    }

    def run(self):
        if not self.options:
            raise self.error('Must specify at least one platform.')
        # TODO: make links to platform pages
        return [nodes.emphasis(text='Availability: '),
                nodes.Text(', '.join(self.options))]


def setup(app: Sphinx):
    app.add_directive('availability', AvailabilityDirective)


# -- Python domain hacks ---------------------------------------------------

real_get_signature_prefix = PyClassmember.get_signature_prefix


def get_signature_prefix(self, sig):
    # hacks for battery and light
    if sig.count('.') >= 2:
        return ''
    return real_get_signature_prefix(self, sig)


PyClassmember.get_signature_prefix = get_signature_prefix


# HACK: For certain hub attributes, we list the class members of the attributes
# class as if the attribute was a nested class so that readers don't have to
# skip around the docs as much. To make this work, we replace the attribute
# values with the type and override PythonDomain.find_obj so that references
# still work.

base_find_obj = PythonDomain.find_obj


def find_obj(self, env, modname, classname, name, type, searchmode=0):
    if modname == 'pybricks.hubs':
        if classname == 'screen':
            if name.startswith('Font.') or name == 'Font':
                modname = 'pybricks.media.ev3dev'
            elif name.startswith('Image.') or name == 'Image':
                modname = 'pybricks.media.ev3dev'
            else:
                classname = 'EV3Brick.screen'
        elif classname == 'speaker':
            classname = 'EV3Brick.speaker'
    return base_find_obj(self, env, modname, classname, name, type, searchmode)


PythonDomain.find_obj = find_obj

EV3Brick.screen = Image
EV3Brick.speaker = Speaker
