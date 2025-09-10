from celery import Celery
from llm_model import score_claim

app = Celery('tasks', broker='redis://redis:6379/0')

@app.task
def process_claim(claim_data):
    return score_claim(claim_data)
