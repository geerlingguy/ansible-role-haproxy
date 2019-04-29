#!/bin/venv python3
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_haproxy_is_installed(host):
    pkg = host.package('haproxy')
    assert pkg.is_installed


def test_haproxy_running_and_enabled(host):
    haproxy = host.service("haproxy")
    assert haproxy.is_running
    assert haproxy.is_enabled


def test_check_http_port(host):
    assert host.socket("tcp://:::80").is_listening
