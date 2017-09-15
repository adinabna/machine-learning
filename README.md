# Machine Learning
Trying out examples from [Udacity's Machine Learning course](https://www.udacity.com/course/intro-to-machine-learning--ud120).

## Synopsis

_**For the following commands to work, do the Requirements section first if it's your first time running this.**_

Simply run the following command for each file you wish to run:

```
python file_name.py
```

## Requirements

For managing dependencies this project uses a _**requirements.txt**_ file, the _pom_ file of Python.

- Install _**pip**_ using the following command:
```
sudo easy_install pip
```

- Use the _**requirements.txt**_ file **to install all dependencies** by calling the following command **from within the root of the project**:
```
pip install -r requirements.txt
```
This will install, among others, `matplotlib`.
For this, there is a directory in you root called `~/.matplotlib`.
Create a file `~/.matplotlib/matplotlibrc` there and add the following code: `backend: TkAgg` <br />
The reason behind this is explained [here](http://matplotlib.org/faq/usage_faq.html#what-is-a-backend).

If you run into any errors, try installing the following:
```
sudo apt-get install python-setuptools
```

## Description

Machine Learning is an introductory course on this subject.
I am simply trying out the examples from [Udacity's course](https://www.udacity.com/course/intro-to-machine-learning--ud120).

## Errors

All logs will be printed to *stderr*, and thus all the errors will be found there.

## Development Setup

Please install the following in order to run the project and the analysis tool against it:

- [Install pyenv-virtualenv plugin](https://github.com/pyenv/pyenv-virtualenv)
```
  brew install pyenv-virtualenv
```
Please follow all the steps in the Github project link above.

- The analysis tool will run in a virtual environment https://github.com/pyenv/pyenv
Install using the below:
```
  pyenv install 2.7.13
  pyenv virtualenv 2.7.13 machine-learning
  pyenv activate machine-learning
```

Run the following command if you wish to remove the virtual environment created:
```
  pyenv uninstall machine-learning
```

_**This is an extra step before first installing Pylint.**_ <br />
  Change to the root of the project and generate the initial settings file for Pylint using:
  ```
    pylint --generate-rcfile > .pylintrc
  ```

  Disable some of the warnings (e.g. _**missing-docstring, bare-except, fixme, redefined-builtin, too-many-locals**_) by adding these (_**missing-docstring,bare-except,fixme,redefined-builtin,too-many-locals**_) to the end of the line which starts _**disable=**_ if you wish to turn that off.

- Install Pylint https://www.pylint.org/ :
```
  pip install pylint
```

- Now, while in the root of the project opened from the last used command line, evaluate the code using:
```
  pylint *.py
```
You will see something like this:
`Your code has been rated at 8.60/10`

- For managing dependencies use a _**requirements.txt**_ file, the _pom_ file of Python.
```
  pip install -r requirements.txt
```

- See all dependencies using the following command:
```
  pip freeze
```
Pipe directly all dependencies into the _**requirements.txt**_ file in a sorted manner using the following command line:
```
  pip freeze | sort > requirements.txt
```

- When inside the virtual env, you need to install dependencies again, otherwise Pylint will complain it cannot import them. Use the _**requirements.txt**_ file to install all dependencies by calling the following from within the root of the project:
```
pip install -r requirements.txt
```
