# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Tec+60 de 2024'
copyright = '2024, Tec+60'
author = 'Tec+60'
release = '2024'

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
html_theme = 'furo'
#html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_title = html_short_title = project
html_theme_options = {
    'navigation_with_keys': True,
    'source_repository': 'https://gitea.mange.ifrn.edu.br/tec60/turma-2024/',
    'source_branch': 'estudantes',
    'source_directory': 'docs',
    'source_edit_link': 'https://gitea.mange.ifrn.edu.br/tec60/turma-2024/_edit/estudantes/docs/{filename}',
    'source_view_link': 'https://gitea.mange.ifrn.edu.br/tec60/turma-2024/src/estudantes/docs/{filename}',
}

