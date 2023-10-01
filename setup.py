import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "stateful-flet",
    version = "1.0.0",
    author = "Mohammed S. Ahmed",
    author_email = "nnkotkshi@example.com",
    description = "Stateless flet now it's Stateful",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/nnko0o/stateful-flet",
    license='MIT',
    project_urls = {
        "Bug Tracker": "https://github.com/nnko0o/stateful-flet/issues",
        "Source":"https://github.com/nnko0o/stateful-flet",
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages = ["stateful_flet"],
    python_requires = ">=3.7",
)