import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="journalize-io",
    version="0.0.1",
    author="Journalize.io",
    author_email="support@journalize.io",
    description="Client library for journalize.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/journalize-io/journalize-python",
    project_urls={
        "Homepage": "https://www.journalize.io"
    },
    packages=['journalizeio'],
    python_requires=">=3.6",
    install_requires=['requests']
)