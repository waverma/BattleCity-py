from cx_Freeze import setup, Executable
import setuptools

executables = [
    Executable(
        'battle_city/__main__.py',
        targetName='BattleCity.exe',
        # base='Win32GUI',
        # icon='log.ico'
    )
]


includes = ['pygame']

zip_include_packages = ['pygame']

include_files = [
    'resources/*'
]

options = {
    'build_exe': {
        'include_msvcr': True,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows',
        'include_files': include_files,
    }
}

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = [x.strip() for x in f]

setup(
    name="battle_city",
    version="1.2",
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
    executables=executables
)


# setuptools.setup(
#     name="battle_city",
#     version="1.2",
#     author="Maxim Rusakov",
#     description="just a Battle City game.",
#     long_description=long_description,
#     packages=setuptools.find_packages(),
#     install_requires=requirements,
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires=">=3.7",
# )
