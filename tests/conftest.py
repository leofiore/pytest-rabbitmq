"""Tests main conftest file."""
from pytest_rabbitmq import factories

# pylint:disable=invalid-name
rabbitmq_proc2 = factories.rabbitmq_proc(port=5674, node="test2")
rabbitmq2 = factories.rabbitmq("rabbitmq_proc2")
rabbitmq_rand_proc = factories.rabbitmq_proc(port=None, node="test3")
rabbitmq_rand = factories.rabbitmq("rabbitmq_rand_proc")
rabbitmq_rand_proc2 = factories.rabbitmq_proc(port=None)
rabbitmq_rand_proc3 = factories.rabbitmq_proc(port=None)
rabbitmq_plugindir = factories.rabbitmq_proc(plugindir="/etc")
# pylint:enable=invalid-name
