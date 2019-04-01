import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spotifyapi",
    version="0.0.1",
    author="Zack Elia",
    author_email="pypi@zacharyelia.com",
    description="A Python wrapper to interact the Spotify web API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zackelia/spotifyapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ],
)
