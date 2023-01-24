import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_package",
    version="0.0.1",
    author="Terekhov Illia",
    author_email="iterekhov@example.com",
    description="My example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.my/my_package",
    project_urls={
        "Bug Tracker": "https://gitlab.my/my_package/issues"
    },
    license="MIT",
    packages=["my_package"],
    package_data={"": ["*.txt", "*.rst", '*.md']},
    install_requires=[
        "djangorestframework-simplejwt>=5.2.0",
        "Django>=3.2.13",
        "requests==2.27.1",
        "djangorestframework>=3.13.1",
    ],
)