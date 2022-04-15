from sanic import Blueprint, response
from app.models import User

user = Blueprint("user", url_prefix="/user")

@user.get("/getUserList")
async def getAll(request):
    users = await User.all()
    return response.json({"users": users})