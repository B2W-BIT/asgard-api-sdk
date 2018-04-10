#encoding: utf-8

import unittest
import os

from asgard.sdk.options import get_option

class TestOptions(unittest.TestCase):

    """Tests Option-reading logic"""

    def test_read_empty_option(self):
        self.assertEquals([], get_option("dns", "MYPARAM"))

    def test_read_simple_option(self):
        os.environ['HOLLOWMAN_FILTER_DNS_TIMEOUT'] = "10"
        self.assertEquals(["10"], get_option("filter", "DNS_TIMEOUT"))
        self.assertEquals(["10"], get_option("filter", "dns_timeout"))

    def test_read_composite_gapped_suffix(self):
        """
        If we have a hap on the suffix, values after the gap won't be read.
        """
        os.environ['HOLLOWMAN_FILTER_DNS_FOO_0'] = "abc"
        os.environ['HOLLOWMAN_FILTER_DNS_FOO_1'] = "ab1"
        os.environ['HOLLOWMAN_FILTER_DNS_FOO_2'] = "ab2"
        os.environ['HOLLOWMAN_FILTER_DNS_FOO_4'] = "ab4"
        self.assertEquals(["abc", "ab1", "ab2"], get_option("filter", "dns_foo"))
        self.assertEquals(["abc"], get_option("filter", "dns_foo_0"))

    def test_read_composite_mixed_numeric_suffix(self):
        """
        Tests if we can read both envs: with and without numerix suffix
        When we have both envs, we join then on the result, so:
            HOLLOWMAN_FILTER_DNS_PARAM_FOO = "abc"
            HOLLOWMAN_FILTER_DNS_PARAM_FOO_0 = "xyz"
        results in: ["abc", "xyz"] when calling get_option("dns", "foo")
        """
        os.environ['HOLLOWMAN_FILTER_DNS_BAR'] = "abc"
        os.environ['HOLLOWMAN_FILTER_DNS_BAR_0'] = "xyz"
        self.assertEquals(["abc", "xyz"], get_option("filter", "dns_bar"))

    def test_read_different_namespace(self):
        os.environ['HOLLOWMAN_METRICS_ZK_SERVER_ID_0'] = "a"
        os.environ['HOLLOWMAN_METRICS_ZK_SERVER_ID_1'] = "b"
        os.environ['HOLLOWMAN_METRICS_ZK_SERVER_ID_2'] = "c"
        self.assertEquals(["a", "b", "c"], get_option("metrics", "zk_server_id"))


