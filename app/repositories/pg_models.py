from tortoise import Model, fields


class PGWidget(Model):
    """Widget model."""
    currency_id = fields.UUIDField(null=True)
    meta = fields.JSONField(null=True)

    class Meta:
        table = 'pg_widget'
