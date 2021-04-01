#!/usr/bin/env python

import re

def parse_software_ios(text):
    regex = re.compile(r"Software\s.+\),\sVersion\s(?P<software>\S+),")
    match = regex.search(text)

    if match:
        return match.group("software")
    else:
        return None

def parse_model_ios(text):
    regex = re.compile(r"[Cc]isco\s+(?P<model>\S+)\s+\(.+\)")
    match = regex.search(text)

    if match:
        return match.group("model")
    else:
        return None

def parse_serial_ios(text):
    regex = re.compile(r"[Pp]rocessor\s+board\s+ID\s+(?P<serial>\S+)")
    match = regex.search(text)

    if match:
        return match.group("serial")
    else:
        return None

def parse_hostname_ios(text):
    regex = re.compile(r"(?P<hostname>\S+)\s+uptime\s+is\s+")
    match = regex.search(text)

    if match:
        return match.group("hostname")
    else:
        return None

def parse_loop0_ios(text):
    regex = re.compile(r"Loopback0\s+(?P<loop0>\S+)\s+\w+")
    match = regex.search(text)

    if match:
        return match.group("loop0")
    else:
        return None

def parse_ospf_neighbor_id_ios(text):
    regex = re.compile(r"(?P<neighbor_id>\S+)\s+[0-255]\s+")
    match = regex.search(text)

    if match:
        return match.group("neighbor_id")
    else:
        return None
