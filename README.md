# `imsanity` (Import Sanity)

Python's import situation is terrible and unusable. `imsanity` makes it usable.

### Install
`pip install imsanity`

### What the dang?
Say you have a python project (not a package), with the following structure:
```
|-- bin/
|   |-- web_server.py
|-- lib/
|   |-- __init__.py
|   |-- email.py
|   |-- test_email.py
|-- tools/
|   |-- reports.py
```

##### How does `test_email.py` import `email.py`?
- `import email` doesn't work, because `email` is a core python package
- `from . import email` works, but won't work if you try to run `python test_email.py`. You have to run `python -m test_email` instead, which is annoying and unexpected.

##### How does `reports.py` import `email.py`?
- `from ..lib import email` is the only thing that works, but it doesn't allow you to run `./reports.py`. You have to instead run `python -m reports`, which is *really* annoying and *very* unexpected.
- If you move `reports.py` to a subfolder inside tools, you'll have to update all its imports

### I guess add the project root to PYTHONPATH?
Sure, you could do that. But then you have to manage this on every machine you work on. And if you have multiple projects like this, you have to make sure the PYTHONPATH is set correctly for each one.

Maybe you can just add all the projects to your PYTHONPATH? But, god forbid you have a library with the same name in different projects, good luck figuring out that mess. So, that's probably not a good idea.

The only safe thing to do is add to the PYTHONPATH whenever you start working on a project, and remember to remove from the PYTHONPATH (and add the new project's base directory to the PYTHONPATH) whenever you switch projects. Sounds terrible, eh?

#### Or, you can use `imsanity`

Simply place a `.imsanity` file in the project root. Then, `import imsanity` at the top of the file. PYTHONPATH will now include the project root.

##### How does `test_email.py` import `email.py`?
`from lib import email` works, and allows you to run `python test_email.py`

##### How does `reports.py` import `email.py`?
`from lib import email` works, and allows you to run `./reports.py`

### Does python really not have a solution to this?

Well... there's [PEP 0366](https://www.python.org/dev/peps/pep-0366/), which recommends you put this:
```
if __name__ == "__main__" and __package__ is None:
    __package__ = "expected.package.name"
```
at the top of every file. Key quotes:
- this boilerplate is sufficient only if the top level package is already accessible via `sys.path`
- if the script is moved to a different package or subpackage, the boilerplate will need to be updated manually

My only response to this is: ahahahahahahahahaha :'(
