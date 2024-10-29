import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="secret-santa-solver",
    version="0.0.1",
    author="Jean Plancher",
    author_email="python@plean.fr",
    description="The Secret Santa Solver is a Python tool designed to assign Secret Santa gift pairs for a group of participants. Each participant has the option to specify a list of people they feel comfortable gifting to, allowing for a personalized and comfortable gift exchange experience. If no preferences are specified, the participant can be assigned to any other participant.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 license",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
