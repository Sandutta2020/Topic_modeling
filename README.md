# Topic Modeling:
This can be solved by in two ways. <br>
 ```diff
+ 1.With GUI(FastAPI) 
+ 2.Through backend
```
 

## The folder Structer and use full

```
Base----|conf : For storing all the configuration file
        |data : The Input data src file
        |model : For Storing the model
        |report For generating the output
        |src : For src code/Business logic	
        |static : For storing all the css and js file
        |template : for storing all the template html file
        |app.py  : FastAPI logic written file and starting point of FastAPI 
        |main.py : Main logic while running from background
        |params.yaml : for storing Necessary parameter file
        |procfile : necessary file for cloud deployment
        |Readme.md :For Git Documentation
        |requirements.txt : All the necessary packages
```

### to install Dependency ,Please run the following commands

```
conda create -n envName python =3.7
conda activate envName
pip install -r requirements.txt
```

## to run FastAPI server 

``` python app.py ```

On successful run it FastAPI will serve 

``` http://127.0.0.1:8000/ ```

## Code lynting using black

``` black app.py```