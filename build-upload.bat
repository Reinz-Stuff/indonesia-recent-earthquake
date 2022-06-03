@echo off
rmdir build dist /s /q
py -m build
py -m twine upload --repository pypi dist/*