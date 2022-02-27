import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py_sb_win_tools',
    version='0.0.1',
    author='Sean Branner',
    author_email='seanbranner@gmail.com',
    description='Custom tools made for manipulating dataframes.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://stash.us.dominos.com/scm/~brannes/py-sb-win-tools',
    project_urls = {
        "Bug Tracker": "https://github.com/seanbranner/py-sb-win-tools/issues"
    },
    license='MIT',
    packages=['py_sb_win_tools'],
    install_requires=[
    ],
)