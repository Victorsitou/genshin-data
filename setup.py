from setuptools import setup

setup(
    name="Genshin Data",
    version="0.1.0a",
    description="Python version of https://github.com/dvaJi/genshin-data",
    packages=["genshin_data", "genshin_data.types", "genshin_data.min"],
    package_data={"genshin_data.min": ["*.json"]},
    install_requires=["pydantic>=1.10.0,<1.11.0"],
)
