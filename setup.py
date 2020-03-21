import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="durgo-sdk", # Replace with your own username
    version="0.0.1",
    author="Safwan Rahman",
    author_email="safwan.rahman15@gmail.com",
    description="Python client for durgo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/safwanrahman/durgo-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
