# test-task-DataOx


### Smutok Vasyl


## Installation

Python3 must be already installed

```shell
git clone https://github.com/Vasyl-Smutok/test-task-DataOx.git
cd test-task-DataOx
python3 -m venv venv
source venv/bin/activate  # on macOS
venv\Scripts\activate  # on Windows 
pip install -r requirements.txt  
```

Then you need to create variables in os environment
```shell
DB_NAME, DB_USER, DB_PASSWORD, DB_HOST,
```
### You can run the script via Docker or locally

#### To do it locally
```shell
python db_manager # run DB 
python parse.py #run parse
```

#### To do this using Docker
```shell
docker build -t test-task-dataox .
docker-compose up 
```