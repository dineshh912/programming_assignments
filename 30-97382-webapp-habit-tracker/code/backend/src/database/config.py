import os

# Need to configure Database in here!
DATABASE_URL = "mysql://root:@localhost:3306/habit"
TORTOISE_ORM = {
    # Define database URL
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            # src.database.models is main database
            # aerich.models is migration databases
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}