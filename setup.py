from setuptools import setup

APP = ['transcriber.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': None,  # Optionally add an icon file path (e.g. 'icon.icns')
    'packages': ['openai'],
    # Note: tkinter is part of the standard library; if you get issues, you may need to set the TCL_LIBRARY and TK_LIBRARY environment variables.
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
