## Mock Behavior, simulute response db
from unittest.mock import patch

#Operational error to simulate a posible response error.
from psycopg2 import OperationalError as Psycopg2Error

# Provided by django to call a command by name
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase