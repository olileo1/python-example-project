import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-project",
    author="Oliver Leodolter",
    author_email="oliver.leodolter@gmx.at",
    description="Example Project to show a project setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={"": ["*.ini", "*.yaml", "*.csv", "*.sql"]},
    url="https://github.com/olileo1/python-example-project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent", ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    entry_points={
        "console_scripts":
            [
                "sum_up="
                "package_1.executables.sum_up:main"], },
    python_requires=">=3.9")
