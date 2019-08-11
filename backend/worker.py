#!/usr/bin/env python3

# Simple script to use redis and celery to quarry jobs to and from Flask app

from celery import celery
from algorithm import approx

app = Celery(__name__, backend='rcp://', broker='redis://')
# backend: how to extract results
# broker: Queueing mechanism


@app.task
def integrate(*args, **kwargs):
    try:
        approx(*args,**kwargs)
    except Exception:
        return None
