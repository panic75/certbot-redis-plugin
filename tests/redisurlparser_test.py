import os
import sys
import pytest
SETTINGS_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))
sys.path.insert(0, SETTINGS_DIRECTORY)
from certbot_redis_plugin.redisurlparser import RedisUrlParser


class TestRedisUrlParser(object):
    def test_parses_hostname(self):
        subject = RedisUrlParser('redis://test-host')

        assert subject.hostname == 'test-host'

    def test_parses_port(self):
        subject = RedisUrlParser('redis://a:42')

        assert subject.port == 42

    def test_parses_password(self):
        subject = RedisUrlParser('redis://a:test-Password@b:44')

        assert subject.password == 'test-Password'

    def test_parses_all_parameters(self):
        subject = RedisUrlParser('redis://a:test-Password@test-host:44')

        assert subject.password == 'test-Password'
        assert subject.hostname == 'test-host'
        assert subject.port == 44

