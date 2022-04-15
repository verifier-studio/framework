from sanic import Sanic, response
from tortoise.contrib.sanic import register_tortoise

from app.run import api

app = Sanic(__name__)
app.update_config("./app/config.py")
app.blueprint(api)

register_tortoise(app, db_url=app.config.DB, modules={"models": ["app.models"]}, generate_schemas=True)