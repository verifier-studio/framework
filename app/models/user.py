from tortoise import Model, fields

class User(Model):
    id = fields.IntField(pk=True)
    role = fields.SmallIntField(default=0)
    username = fields.CharField(50)
    password = fields.CharField(100)
    createTime = fields.IntField()
    loginTime = fields.IntField()