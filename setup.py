from setuptools import setup, find_packages


def read_file(fname):
    with open(fname, "r") as f:
        return f.read()


requirements = [
    "pathvalidate",
    "requests",
    "mutagen",
    "tqdm",
    "pick==1.6.0",
    "beautifulsoup4",
    "colorama",
]

setup(
    name="qobuz-dl-babymetaldev",
    version="0.9.9.11.dev3",
    author="babymetal",
    author_email="",
    description="The complete Lossless and Hi-Res music downloader for Qobuz",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/streetsamurai00mi/qz-dl/tree/dev",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "qobuz-dl-babymetaldev = qobuz_dl:main",
            "qzdl-dev = qobuz_dl:main",
            "qzdl = qobuz_dl:main",
        ],
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

# rm -f dist/*
# python3 setup.py sdist bdist_wheel
# twine upload dist/*
