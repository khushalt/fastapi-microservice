import fastapi
from fastapi import FastAPI


def init_notification_app():
    """register all config for app here"""
    app_ = FastAPI(title="Supplier Service", description="Customer service description")
    return app_


app: fastapi.FastAPI = init_notification_app()
