#!/usr/bin/env python3

# Simple script to use redis and celery to quarry jobs to and from Flask app

from celery import Celery
from algorithm import approx

app = Celery(__name__, backend='rpc://', broker='redis://')
# backend: how to extract results
# broker: Queueing mechanism


@app.task
def integrate(*args, **kwargs):
    try:
        return approx(*args,**kwargs)
    except Exception:
        return None
