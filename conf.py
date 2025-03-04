#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Digital Earth Australia documentation build configuration file, created by
# sphinx-quickstart on Wed Jun  7 17:22:24 2017.

import os
import sys

extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "myst_parser",
    "sphinxext.rediraffe",
    "sphinxext.opengraph",
    "sphinxcontrib.video",
    # Fix jQuery is not defined error on Sphinx 6+
    # See https://github.com/readthedocs/sphinx_rtd_theme/issues/1452#issuecomment-1490504991
    "sphinxcontrib.jquery", 
#    "sphinxcontrib.spelling",
]

# Add dea_tools to Python path for autosummary doc generation
sys.path.insert(0, os.path.abspath("./notebooks/Tools"))
autosummary_generate = ["notebooks/Tools/index.rst"]
autodoc_default_options = {
    "members": True,
}

ogp_site_url = "https://docs.dea.ga.gov.au/"
ogp_image = "_static/dea-logo-inline.png"

# We are are not installing dea_tools dependencies, so we need
# to mock them so autodocs does not fail
autodoc_mock_imports = [
    "aiohttp",
    "boto3",
    "botocore",
    "branca",
    "ciso8601",
    "dask",
    "dask_gateway",
    "dask_ml",
    "datacube",
    "dill",
    "distutils",
    "fsspec",
    "fiona",
    "folium",
    "geopandas",
    "geopy",
    "hdstats",
    "ipyleaflet",
    "ipython",
    "ipywidgets",
    "joblib",
    "lxml",
    "matplotlib",
    "mpl_toolkits",
    "numexpr",
    "numpy",
    "odc",
    "osgeo",
    "otps",
    "OWSLib",
    "owslib",
    "packaging",
    "pandas",
    "pathos",
    "pyproj",
    "python_dateutil",
    "psycopg2",
    "pyTMD",
    "pytz",
    "rasterio",
    "rasterstats",
    "requests",
    "rios",
    "rsgislib",
    "scikit_learn",
    "sklearn",
    "scipy",
    "setuptools",
    "setuptools_scm",
    "shapely",
    "skimage",
    "tqdm",
    "traitlets",
    "xarray",
]
autosummary_mock_imports = autodoc_mock_imports

# Ensure that dea_tools Numpy docstrings are interpreted correctly
napoleon_google_docstring = False
napoleon_numpy_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# disable automatic running of .ipynb files
nbsphinx_execute = "never"

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#source_suffix = [".rst", ".md"]

extlinks = {
        'dea-s3': ('s3://dea-public-data/%s', '%s'),
        'dea-data': ('https://data.dea.ga.gov.au/?prefix=%s', '%s'),
}

# The master toctree document.
master_doc = "index"

# General information about the project.
from datetime import datetime

year = datetime.now().strftime("%Y")

project = "Digital Earth Australia"
copyright = f"2017-{year}, Geoscience Australia"
author = "Geoscience Australia"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "1.0.0"
# The full version, including alpha/beta/rc tags.
release = "1.0.0"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    "notebooks/Scientific_workflows",
    "notebooks/.github",
    "notebooks/DEA_notebooks_template.ipynb",
    "notebooks/USAGE.rst",
    ".*",
]

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

try:
    import sphinx_rtd_theme

    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_theme_options = {
        "logo_only": True,
        "analytics_id": "G-4B9D450HR4",
        "display_version": False,
        "canonical_url": "https://docs.dea.ga.gov.au/",
    }
except ImportError:
    html_theme = "alabaster"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_logo = "_static/dea-logo-inline.svg"

html_favicon = "_static/dea-favicon.ico"

html_use_index = True


rediraffe_redirects = "redirects.txt"
rediraffe_branch = "master~1"


spelling_word_list_filename = 'notebooks/.github/workflows/configs/spellcheck_wordlist.txt'

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "odc": ("https://datacube-core.readthedocs.io/en/stable/", None),
}


def setup(app):
    app.add_css_file("css/custom.css")
