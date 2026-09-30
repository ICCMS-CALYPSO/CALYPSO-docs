# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CALYPSO'
copyright = '2023, CALYPSO Dev Group'
author = 'CALYPSO Develop Group'
html_logo = './_static/CALYPSO_LOGO.png'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxemoji.sphinxemoji',
    'sphinx_design',
    'sphinx_markdown_tables',
    # 'sphinx_multiversion',
    # 'sphinx_sitemap',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinxcontrib.mermaid',
]

exclude_patterns = ['development']

myst_heading_anchors = 4
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "fieldlist",
    "deflist",
    "colon_fence",
    "attrs_inline",
    "attrs_block",
]
myst_fence_as_directive = ["mermaid"]

intersphinx_mapping = {
    'py3': ('https://docs.python.org/3', None),
    'np': ('https://numpy.org/doc/stable', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

templates_path = ['_templates']
html_sidebars = {
    '**': [
        #         'about.html',
        #         'searchfield.html',
        #         'navigation.html',
        #         'relations.html',
        #         'donate.html',
        #         'versioning.html',
        #         'versions.html',
    ],
}

##### LATEX parameter
latex_engine = 'pdflatex'
latex_elements = {
    'preamble': r'''
\usepackage{amsmath}
\usepackage{amssymb}
# \usepackage{unicode-math}
# \setmathfont{XITS Math}
''',
}
# latex_elements = {
#     'preamble': r'''
# \usepackage[heading=true]{ctex}
# ''',
#     'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
#     'printindex': r'\footnotesize\raggedright\printindex',
# }
latex_show_urls = 'footnote'
