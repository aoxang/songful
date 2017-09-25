#!/usr/local/bin/python2.7
# encoding: utf-8

# import traceback
# cs = None
#
# def _get_client():
#     from servicemgrclient.v1 import client
#     username = 'host'
#     password = 'host@Cloud365'
#     project_name = 'services'
#     # auth_uri = 'http://192.168.6.31:35357/v2.0'
#     auth_uri = 'http://192.168.6.31:35357/v3'
#     service_type = 'host'
#     region_name = 'RegionOne'
#
#     return client.Client(username=username,
#                          password=password,
#                          # api_key=api_key,
#                          # project_id=project_id,
#                          project_name=project_name,
#                          auth_url=auth_uri,
#                          # servicemgr_url=servicemgr_url,
#                          # endpoint_type=endpoint_type,
#                          # endpoint_override=endpoint_override,
#                          service_type=service_type,
#                          region_name=region_name,
#                          user_domain_id='default',
#                          project_domain_id='default'
#                          # input_auth_token=input_auth_token,
#                          # session=session,
#                          # auth_type=auth_type,
#                          # auth_token=auth_token,
#                          # api_version=api_version
#                          )
#
#
# def test_list():
#     cs = _get_client()
#     try:
#         monitor_list = cs.monitor.list()
#         if not monitor_list:
#             return
#         print monitor_list
#     except:
#         print "error : ", traceback.format_exc()
#         return False
#     return True
#
# if __name__ == '__main__':
#     test_list()


from keystoneauth1 import loading
from keystoneauth1 import identity
from keystoneauth1 import session
from neutronclient.v2_0 import client as neutron_client
from novaclient import client as nova_client
from glanceclient import Client as glance_client
from autoscalingclient import client as autoscaling_client

class AscencloudClient(object):
    def __init__(self):
        self.user_name = CONF.keystone_authtoken.admin_user
        self.password = CONF.keystone_authtoken.admin_password
        self.project_name = CONF.keystone_authtoken.admin_tenant_name
        self.auth_url = CONF.keystone_authtoken.auth_uri
        self.project_domain_id = 'default'
        self.user_domain_id = 'default'

    def get_nova_client(self):
        """
        init novaclient for tags.

        :return: nova client.
        """
        version = CONF.client_version.nova_version.split('v')[1]
        loader = loading.get_plugin_loader('password')
        auth = loader.load_from_options(auth_url=self.auth_url,
                                        username=self.user_name,
                                        password=self.password,
                                        project_name=self.project_name,
                                        project_domain_id='default',
                                        user_domain_id='default')
        sess = session.Session(auth=auth)
        nova_c = nova_client.Client(version, session=sess)
        return nova_c

def get_nova_client(self):
    """
    init novaclient for tags.

    :return: nova client.
    """
    version = CONF.client_version.nova_version.split('v')[1]
    loader = loading.get_plugin_loader('password')
    auth = loader.load_from_options(auth_url=self.auth_url,
                                    username=self.user_name,
                                    password=self.password,
                                    project_name=self.project_name,
                                    project_domain_id='default',
                                    user_domain_id='default')
    sess = session.Session(auth=auth)
    nova_c = nova_client.Client(version, session=sess)
    return nova_c