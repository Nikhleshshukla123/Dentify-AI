#### Dentify AI Project Setup
`Requirements:`<br>
- `8 GB RAM`<br>
- `Code Editor VSCode / Pycharm`<br>
- `Git CLI`<br>
- `Docker Desktop`<br>
- `Web Browser Chrome / Edge`<br>
- `python 3.12.4`<br>
  
#### Clone the Project
```
git clone git@github.com:nikhivishwaa/dentify-ai.git -b dev
```

#### Go to Project Directory
```
cd dentify-ai
```

#### Create virtual environment and install dependencies
- `Create environment`<br>
```
python -m virtualenv env -p python312
```

- `Activate environment`<br>
```
.\env\Scripts\activate
```

- `Install Dependencies`<br>
```
pip install -r requirements.txt
```

`You Are all Set to use the Project`<br>


##### Run the Project
```
cd .\dentify_ai\
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### Update the Code
- `Reach the dentify-ai directory first`<br>

```
git pull
.\env\Scripts\activate
pip install -r requirements.txt
cd .\dentify_ai\
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
