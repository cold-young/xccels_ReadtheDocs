# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xccels_ReadtheDocs'
copyright = '2024, cold-young'
author = 'cold-young'
release = 'v 0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'myst-parser'
]
source_suffix = {
    '.rst' : 'restructuredtext',
    '.txt' : 'markdown',
    '.md' : 'markdown',
    
}

templates_path = ['_templates']
exclude_patterns = ['build']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = '_themes'
html_static_path = ['_static']
