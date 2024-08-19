import os
import sys

sys.path.insert(0, os.path.abspath('../src')) # Informa onde está o diretório contendo o código fonte

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Conversor'
copyright = '2024, Matheus Venturini Bortoluzzi'
author = 'Matheus Venturini Bortoluzzi'
release = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc', # Usado para que o Sphinx faça parse das docstrings nos arquivos de código fonte do projeto
    'sphinx.ext.viewcode' # Usado para que seja incluído um botão para mostrar o código fonte de uma função na documentação
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

master_doc = 'index' # Por padrão o Sphinx espera que a página inicial da documentação seja "contents.html", mas como iremos utilizar "index.html" temos que especificar isto
