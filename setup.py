import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="addshare-plus",
    version="0.0.1",
    author="baasare",
    author_email="atiemoasare@gmail.com",
    packages=["addshare_plus"],
    description="Simple privacy preserving federated learning framework",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/test-tackage",
    license='Apache License 2.0',
    python_requires='>=3.8',
    install_requires=[]
)