import unittest
from unittest import mock
import os

from asgard.sdk.mesos import get_mesos_leader_address, is_master_healthy

from responses import RequestsMock
import requests

class MesosTest(unittest.TestCase):

    def setUp(self):
        pass


    def test_get_mesos_leader_ip(self):
        mesos_addresses = ["http://10.0.2.1:5050", "http://10.0.2.3:5050", "http://10.0.2.2:5050"]
        with mock.patch.dict(os.environ, {"HOLLOWMAN_MESOS_ADDRESS_0": mesos_addresses[0],
                                          "HOLLOWMAN_MESOS_ADDRESS_1": mesos_addresses[1],
                                          "HOLLOWMAN_MESOS_ADDRESS_2": mesos_addresses[2]}), \
            RequestsMock() as rsps:
            rsps.add("GET", url=mesos_addresses[1] + "/redirect", status=307, body="", headers={"Location": "//10.0.2.2:5050"})
            mesos_leader_ip = get_mesos_leader_address()

            self.assertEqual("http://10.0.2.2:5050", mesos_leader_ip)

    def test_mesos_master_is_healthy_ok(self):
        with RequestsMock() as rsps:
            rsps.add("GET", url="http://10.0.0.1:5050/health", status=200, body="")
            self.assertTrue(is_master_healthy("http://10.0.0.1:5050"))

    def test_mesos_master_is_healthy_timeout(self):
        with RequestsMock() as rsps:
            rsps.add("GET", url="http://10.0.0.1:5050/health", body=requests.exceptions.ConnectTimeout())
            self.assertFalse(is_master_healthy("http://10.0.0.1:5050"))

    def test_mesos_master_is_healthy_connection_error(self):
        with RequestsMock() as rsps:
            rsps.add("GET", url="http://10.0.0.1:5050/health", body=requests.exceptions.ConnectionError())
            self.assertFalse(is_master_healthy("http://10.0.0.1:5050"))

