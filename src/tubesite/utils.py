# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.postgres.fields import JSONField as PostgresJSONField
from jsonfield import JSONField as ThirdPartyJSONField


# Define JSONField

db_engine = settings.DATABASES['default']['ENGINE']
is_postgres = "postgres" in db_engine

JSONField = PostgresJSONField if is_postgres else ThirdPartyJSONField
