from setuptools import setup

setup(
    name="dundie",
    version="0.1.0",  # semantic version
    description="Reward Point System for Dunder Mifflin",
    author="Bruno Chiconato",
    packages=["dundie"],
    entry_points={"console_scripts": ["dundie = dundie.__main__:main"]},
)
