import unittest
from unittest import mock
from responses import RequestsMock

from asgard.sdk.mesos import get_mesos_leader_address

import os

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
