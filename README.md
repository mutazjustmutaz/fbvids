
EDIT: It seems like FB has changed its code again, and as a result this script isn't really useful anymore. I'll rewrite the script as soon as I get to it on my to-do list.

  This is a script that downloads Facebook videos. The script relies on nothing beyond 3 standard libraries, which means that it requires no installation of any additional library or software. As long as Python is installed on your PC, you're ready to go.

#### Usage:

```
python fbvids.py "URL"
```

(The double quotes are necessary to prevent the shell from chopping up URLs with ampersands)

#### Notes:

_If available, the HD version of the video is downloaded by default. 

_I didn't put the script in module form because when it comes to simple scripts like this one the result would be ugly, over-built code.
