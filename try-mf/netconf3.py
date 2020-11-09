from ncclient import manager
from lxml import etree

cisco_device01 ={"host":"192.168.1.94",
                     "port":"830",
                     "username":"admin",
                     "password":"cisco123",
                     "hostkey_verify":False,
                     "device_params":{"name":"iosxe"}}

#system-type iosxe iosxr nxos
device = manager.connect(**cisco_device01)

get_interface1 = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
         <interface/>
     </interfaces>
</filter>
"""

config=device.get(get_interface1)
print(config)
print(etree.tostring(config.data_ele,pretty_print=True))
print(device)
print(type(device))
print(get_interface1)
print(type(get_interface1))

