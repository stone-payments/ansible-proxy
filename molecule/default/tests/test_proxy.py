import os
import io

import testinfra.utils.ansible_runner
import ConfigParser

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_proxy_yum(host):
    yum_conf = ConfigParser.RawConfigParser(allow_no_value=True)
    yum_conf_content = host.file("/etc/yum.conf").content_string
    yum_conf.readfp(io.StringIO(yum_conf_content))

    assert yum_conf.has_option('main', 'proxy')


def test_proxy_rhsm(host):
    system_info = host.system_info.distribution

    if system_info == 'redhat':
        rhsm_conf = ConfigParser.RawConfigParser(allow_no_value=True)
        rhsm_conf_content = host.file("/etc/rhsm/rhsm.conf").content_string
        rhsm_conf.readfp(io.StringIO(rhsm_conf_content))

        assert rhsm_conf.has_option('server', 'proxy_hostname')
        assert rhsm_conf.has_option('server', 'proxy_port')

        proxy_hostname = rhsm_conf.get('server', 'proxy_hostname')
        proxy_port = rhsm_conf.get('server', 'proxy_port')

        if str(proxy_hostname) == '':
            assert False

        if str(proxy_port) == '':
            assert False


def test_proxy_env(host):
    assert host.file("/etc/profile.d/proxy.sh").exists
