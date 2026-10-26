"""Sphinx configuration for the Knowage 9.1 documentation."""
project = 'Knowage'
copyright = '2014-2026, Knowage Labs'
author = 'Knowage Labs'
version = '9.1'
release = '9.1.0'
language = 'en'
root_doc = 'index'
extensions = ['sphinx.ext.intersphinx', 'sphinx.ext.todo']
# Historical sources remain in Git and in earlier Read the Docs versions.
# Exclude duplicates and unpublished drafts from the 9.1 build and search index.
exclude_patterns = [
    '_build', '_build/**', '.venv/**', 'maintenance/**',
    'administrator-guide/**', 'installation-guide/**', 'functionalities-guide/**',
    'chapter_1/**', 'chapter_2/**', 'common/**', 'index_old.rst',
    '**/*_old.rst', '**/old_*.rst', '**/*_copy.rst', '**/* copy.rst',
    'chapter_3/create_location/**',
    # Included by manual_installation.rst, not a separate page.
    'chapter_5/installation/ka_inst_man_tomcat.rst',
    'chapter_5/upgrade/how_update_copilot.rst',
]
html_theme = 'sphinx_rtd_theme'
html_title = 'Knowage 9.1 documentation'
html_static_path = ['_static']
html_css_files = ['documentation.css']
html_theme_options = {'navigation_depth': 4}
html_show_sourcelink = True
numfig = True
todo_include_todos = False
linkcheck_ignore = [r'https?://localhost(?::\d+)?/.*', r'https?://127\.0\.0\.1(?::\d+)?/.*']
