DB = "mysql://root:root@localhost/test"

TORTOISE_ORM = {
    "connections": {"default": DB},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default"
        }
    }
}