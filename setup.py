import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = [x.strip() for x in f]

setuptools.setup(
    name="battle_city-py",
    version="1.0",
    author="Maxim Rusakov",
    description="just a Battle City game.",
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
