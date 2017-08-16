Steps for each post:
- Create post in ipython-notebook
- Copy notebook to content
- Create identically named file called <notebook-name>.ipynb-meta
- run pelican content -s publishconf.py
- run ghp-import output -b master
- git push origin master


When Updating the dev branch (where this stuff goes):
- git checkout -b dev
- git add 
- git commit 
- git push