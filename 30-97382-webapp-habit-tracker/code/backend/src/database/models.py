from tortoise import fields, models # Database Object relation mapper

# User table
class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


# Mental health table
class Mentalhealth(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    notes = fields.TextField()
    added_by = fields.ForeignKeyField("models.Users", related_name="note")
    rating = fields.CharField(max_length=225)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.author_id} on {self.created_at}"
