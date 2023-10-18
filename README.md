# Demo app

To run the app

```bash
python main.py
```

or 

```bash
uvicorn main:app --port 4000 --reload
gunicorn main:app -w 2 -k uvicorn.workers.UvicornWorker --reload
```