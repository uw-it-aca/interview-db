import os
from setuptools import setup

README = """
See the README on `GitHub
<https://github.com/uw-it-aca/interview_db>`_.
"""

# The VERSION file is created by travis-ci, based on the tag name
version_path = 'interview_db/VERSION'
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

url = "https://github.com/uw-it-aca/interview_db"
setup(
    name='UW_interview_db',
    version=VERSION,
    packages=['interview_db'],
    author="UW-IT AXDD",
    author_email="aca-it@uw.edu",
    include_package_data=True,
    install_requires=[
        'Django<2.1',
        'Pillow',
        'django-compressor',
        'django-pyscss',
    ],
    license='Apache License, Version 2.0',
    description=('App to collect and tag interview data, artifacts, and stories for publishing using the Django Admin app.'),
    long_description=README,
    url=url,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.0',
    ],
)
