#!/bin/python

import shutil
import toml
import sys
import os
from pathlib import Path
from tg_api_gen import (
    proj_version,
    proj_name,
)


app_path = Path(
    __file__
).parent.resolve()
pypr_path = Path(
    f'{app_path}/pyproject.toml'
)
dist_path = Path(
    f'{app_path}/dist'
)
pypr_data = {
    'build-system': {
        'requires': ['hatchling'],
        'build-backend': 'hatchling.build',
    },
    'project': {
        'dependencies': [],
        'name': proj_name,
        'version': proj_version,
        'authors': [
            {
                'name': 'gmanka',
                'email': 'gmankab@gmail.com',
            },
        ],
        'description': 'lightweight skript that generates realistic device_model, app_verion, system_version for telegram',
        'readme': 'readme.md',
        'requires-python': '>=3.10',
        'classifiers': [
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
        ],
        'urls': {
            'Homepage': 'https://github.com/gmankab/tg_api_gen',
        }
    }
} 


with open(
    pypr_path,
    'w',
) as file:
    file.write(
        toml.dumps(
            pypr_data
        )
    )


shutil.rmtree(
    dist_path,
    ignore_errors = True,
)

os.system(f'{sys.executable} -m prettygit')

