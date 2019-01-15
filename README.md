# My Data Science portfolio

## Steps for local publication

Generate the HTML.
> pelican content

Switch to the output directory
> cd output

Preview
> python -m pelican.server

--> Go to [localhost:8000](http://localhost:8000)


## Steps for publication

> git add *

> git commit -m "New publication"

Update develop branch
> git push origin develop 

> pelican content -s publishconf.py

Import everything in the output folder to the master branch.
> ghp-import output -b master

> git push origin master
