import alpha
from alpha import scheduler


def set_client(new_client):
    alpha.client = new_client


def add_job(function, seconds=3):
    scheduler.add_job(function, "interval", seconds=seconds, args=[alpha.client])
