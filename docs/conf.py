# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Tec+60 de 2025'
copyright = '2025, Tec+60'
author = 'Tec+60'
release = '2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = 'imagens/favicon.ico'
html_favicon = 'imagens/favicon.ico'
#html_theme = 'furo'
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_title = html_short_title = project
html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/tec60/tec60ifrn",
    "repository_branch": "main",
    "use_edit_page_button": True,
    # "use_source_button": True,
    # "use_issues_button": True,
    # "use_repository_button": True,
    # "use_download_button": True
}

