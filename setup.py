import io
import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutoraspects_extension", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-contrib-aspects_extension",
    version=ABOUT["__version__"],
    url="https://github.com/bmtcril/tutor-contrib-aspects-extension",
    project_urls={
        "Code": "https://github.com/bmtcril/tutor-contrib-aspects-extension",
        "Issue tracker": "https://github.com/bmtcril/tutor-contrib-aspects-extension/issues",
    },
    license="Apache 2.0",
    author="Brian Mesick",
    author_email="bmesick@axim.org",
    description="Example tutor plugin for extending Aspects functionality",
    long_description=load_readme(),
    long_description_content_type="text/x-rst",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["tutor>=13.0.0,<14.0.0"],
    extras_require={
        "dev": [
            "tutor[dev]>=13.0.0,<14.0.0",
        ]
    },
    entry_points={
        "tutor.plugin.v1": [
            "aspects_extension = tutoraspects_extension.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
