from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A basic image transformations using numpy and opencv'
LONG_DESCRIPTION = 'A package that allows to modify images and vectorize an image using numpy and opencv.'

# Setting up
setup(
    name="image_transformations",
    version=VERSION,
    author="Mauricio-xxi (Alvaro Camacho)",
    author_email="<alvarocamachodavila@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'numpy'],
    keywords=['python', 'image', 'numpy', 'RGB', 'Vectorize', 'opencv'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)