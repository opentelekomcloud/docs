# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import warnings

import otcdocstheme
import recommonmark
from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'otcdocstheme',
    'recommonmark'
]

# openstackdocstheme options
repository_name = 'opentelekomcloud/docs'
html_last_updated_fmt = '%Y-%m-%d %H:%M'
html_theme = 'otcdocs'

# TODO(shade) Set this to true once the build-openstack-sphinx-docs job is
# updated to use sphinx-build.
# When True, this will raise an exception that kills sphinx-build.
enforcer_warnings_as_errors = False

# autodoc generation is a bit aggressive and a nuisance when doing heavy
# text edit cycles.
# execute "export SPHINX_DEBUG=1" in your terminal to disable

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = ['.md', 'rst']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'docs'
copyright = u'2020, Various members of the OpenTelekomCloud'

# A few variables have to be set for the log-a-bug feature.
#   gitsha: The SHA checksum of the bug description. Extracted from git log.
#   bug_tag: Tag for categorizing the bug. Must be set manually.
#   bug_project: Launchpad project to file bugs against.
# These variables are passed to the logabug code via html_context.
git_cmd = "/usr/bin/git log | head -n1 | cut -f2 -d' '"
try:
    gitsha = os.popen(git_cmd).read().strip('\n')
except Exception:
    warnings.warn("Can not get git sha.")
    gitsha = "unknown"

bug_tag = "docs"
pwd = os.getcwd()
# html_context allows us to pass arbitrary values into the html template
html_context = {"pwd": pwd,
                "gitsha": gitsha}

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

autodoc_member_order = "bysource"

# Locations to exclude when looking for source files.
exclude_patterns = []

# -- Options for HTML output ----------------------------------------------

# Don't let openstackdocstheme insert TOCs automatically.
theme_include_auto_toc = False

# Output file base name for HTML help builder.
htmlhelp_basename = '%sdoc' % project

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ('index',
     '%s.tex' % project,
     u'%s Documentation' % project,
     u'OpenTelekomCloud', 'manual'),
]


github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'


def setup(app):
    app.add_config_value('recommonmark_config', {
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
