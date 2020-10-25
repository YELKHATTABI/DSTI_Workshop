# DSTI_Workshop
Python Tutorial

## Istalling Python
Chose the python version that you want (recomended are 3.7 or 3.8)
https://www.python.org/downloads/windows/
Download and install python

Python will install automatically `pip` which is a tool that help install python packages

## Create Virtual Environment (Optional, for better code management)
### Install virtualenv
Virtualenv is a tool that help python developper manage virtual environement for a better python libraries dependencies management

more information here https://virtualenv.pypa.io/en/stable/user_guide.html#introduction


to install virtualenv all you need to do is to run the following commande on your commande line tool 
```
pip install virtualenv 

```

### Create a virtual environment

To create a virtual environment you need to be in the directory of your workspace then run the following comand by replace `myenv` with the ame you want to give to your virtual environement
```
virtualenv myenv
```
for example, on Windows 
```
PS C:\Users\yassi\MyWorkSpace> virtualenv myenv                                                                                                                                                                                              created virtual environment CPython3.8.6.final.0-64 in 1153ms
  creator Venv(dest=C:\Users\yassi\MyWorkSpace\myenv, clear=False, global=False, describe=CPython3Windows)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\yassi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\Local\pypa\virtualenv)
    added seed packages: pip==20.2.4, setuptools==50.3.2, wheel==0.35.1
  activators BashActivator,BatchActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
PS C:\Users\yassi\MyWorkSpace> .\myenv\Scripts\activate      
```


to activate the virtual environment

On Windows

```
./myenv/Scripts/activate
```
example
```
PS C:\Users\yassi\MyWorkSpace> .\myenv\Scripts\activate
(myenv) PS C:\Users\yassi\MyWorkSpace>
```

On Linux and MacOS
```
source myenv/bin/activate
```
`(myenv)` this means that you are in your virtual environment named myenv

once you are in your virtual environment, you can install the packages you will be needing for your project.

At the end of your project

to deactivate the virtual environment you can run the following command
```
deactivate
```

## Installing essential packages

To install a package, you run the command `pip install package-name` replaceing package name by the package you want to install

The necessary packages for data science are the following
- numpy (for array data)
- pandas (to deal with tables)
- matplotlib
- jupyter ( or jupyterlab if you want to be fancy)
- seaborn (for beautifull plots)
- scipy (for scientific calculation)
- scikit-learn (for machine learning algorithms)
- tqdm ( for some fancy progress bars)

If you want to install all those libraries in one command : 
- create a txt file that you can name `requirements.txt` in your working directory
- copy the name of libraries you want to install in that file and save it
```
numpy 
pandas
matplotlib
jupyter
seaborn
scipy
scikit-learn
tqdm
```
- run the following command `pip install -r requirements.txt`

