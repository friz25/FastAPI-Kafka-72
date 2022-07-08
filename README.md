
first go to kafka
`docker-compose -d up`
*check if its up

next go to app
`python -m venv venv`
in cmd `venv\Scripts\activate`
req:
```
pip install fastapi uvicorn
pip install aiokafka
```
uvicorn main:app --reload
*check if its ok

