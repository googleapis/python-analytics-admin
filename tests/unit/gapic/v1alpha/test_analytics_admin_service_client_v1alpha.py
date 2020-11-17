# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests."""

import mock
import pytest

from google.analytics.admin import v1alpha
from google.analytics.admin.v1alpha.proto import analytics_admin_pb2
from google.analytics.admin.v1alpha.proto import resources_pb2
from google.protobuf import empty_pb2



class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""
    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""
    def __init__(self, responses = []):
        self.responses = responses
        self.requests = []

    def unary_unary(
            self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestAnalyticsAdminServiceClient(object):

    def test_get_account(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        display_name = 'displayName1615086568'
        country_code = 'countryCode1481071862'
        deleted = False
        expected_response = {'name': name_2, 'display_name': display_name, 'country_code': country_code, 'deleted': deleted}
        expected_response = resources_pb2.Account(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.account_path('[ACCOUNT]')

        response = client.get_account(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.GetAccountRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_account_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.account_path('[ACCOUNT]')

        with pytest.raises(CustomException):
            client.get_account(name)

    def test_list_accounts(self):
        # Setup Expected Response
        next_page_token = ''
        accounts_element = {}
        accounts = [accounts_element]
        expected_response = {'next_page_token': next_page_token, 'accounts': accounts}
        expected_response = analytics_admin_pb2.ListAccountsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        paged_list_response = client.list_accounts()
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.accounts[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.ListAccountsRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_accounts_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        paged_list_response = client.list_accounts()
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_delete_account(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.account_path('[ACCOUNT]')

        client.delete_account(name)

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.DeleteAccountRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_account_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.account_path('[ACCOUNT]')

        with pytest.raises(CustomException):
            client.delete_account(name)

    def test_update_account(self):
        # Setup Expected Response
        name = 'name3373707'
        display_name = 'displayName1615086568'
        country_code = 'countryCode1481071862'
        deleted = False
        expected_response = {'name': name, 'display_name': display_name, 'country_code': country_code, 'deleted': deleted}
        expected_response = resources_pb2.Account(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        account = {}

        response = client.update_account(account)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.UpdateAccountRequest(account=account)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_account_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        account = {}

        with pytest.raises(CustomException):
            client.update_account(account)

    def test_provision_account_ticket(self):
        # Setup Expected Response
        account_ticket_id = 'accountTicketId-442102884'
        expected_response = {'account_ticket_id': account_ticket_id}
        expected_response = analytics_admin_pb2.ProvisionAccountTicketResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        response = client.provision_account_ticket()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.ProvisionAccountTicketRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_provision_account_ticket_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        with pytest.raises(CustomException):
            client.provision_account_ticket()

    def test_list_account_summaries(self):
        # Setup Expected Response
        next_page_token = ''
        account_summaries_element = {}
        account_summaries = [account_summaries_element]
        expected_response = {'next_page_token': next_page_token, 'account_summaries': account_summaries}
        expected_response = analytics_admin_pb2.ListAccountSummariesResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        paged_list_response = client.list_account_summaries()
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.account_summaries[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.ListAccountSummariesRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_account_summaries_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        paged_list_response = client.list_account_summaries()
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_property(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        parent = 'parent-995424086'
        display_name = 'displayName1615086568'
        time_zone = 'timeZone36848094'
        currency_code = 'currencyCode1108728155'
        deleted = False
        expected_response = {'name': name_2, 'parent': parent, 'display_name': display_name, 'time_zone': time_zone, 'currency_code': currency_code, 'deleted': deleted}
        expected_response = resources_pb2.Property(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.property_path('[PROPERTY]')

        response = client.get_property(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.GetPropertyRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_property_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.property_path('[PROPERTY]')

        with pytest.raises(CustomException):
            client.get_property(name)

    def test_list_properties(self):
        # Setup Expected Response
        next_page_token = ''
        properties_element = {}
        properties = [properties_element]
        expected_response = {'next_page_token': next_page_token, 'properties': properties}
        expected_response = analytics_admin_pb2.ListPropertiesResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        filter_ = 'filter-1274492040'

        paged_list_response = client.list_properties(filter_)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.properties[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.ListPropertiesRequest(filter=filter_)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_properties_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        filter_ = 'filter-1274492040'

        paged_list_response = client.list_properties(filter_)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_create_property(self):
        # Setup Expected Response
        name = 'name3373707'
        parent = 'parent-995424086'
        display_name = 'displayName1615086568'
        time_zone = 'timeZone36848094'
        currency_code = 'currencyCode1108728155'
        deleted = False
        expected_response = {'name': name, 'parent': parent, 'display_name': display_name, 'time_zone': time_zone, 'currency_code': currency_code, 'deleted': deleted}
        expected_response = resources_pb2.Property(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        property_ = {}

        response = client.create_property(property_)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.CreatePropertyRequest(property=property_)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_property_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        property_ = {}

        with pytest.raises(CustomException):
            client.create_property(property_)

    def test_delete_property(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.property_path('[PROPERTY]')

        client.delete_property(name)

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.DeletePropertyRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_property_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.property_path('[PROPERTY]')

        with pytest.raises(CustomException):
            client.delete_property(name)

    def test_update_property(self):
        # Setup Expected Response
        name = 'name3373707'
        parent = 'parent-995424086'
        display_name = 'displayName1615086568'
        time_zone = 'timeZone36848094'
        currency_code = 'currencyCode1108728155'
        deleted = False
        expected_response = {'name': name, 'parent': parent, 'display_name': display_name, 'time_zone': time_zone, 'currency_code': currency_code, 'deleted': deleted}
        expected_response = resources_pb2.Property(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        property_ = {}

        response = client.update_property(property_)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.UpdatePropertyRequest(property=property_)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_property_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        property_ = {}

        with pytest.raises(CustomException):
            client.update_property(property_)

    def test_get_user_link(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        email_address = 'emailAddress-769510831'
        expected_response = {'name': name_2, 'email_address': email_address}
        expected_response = resources_pb2.UserLink(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = 'name3373707'

        response = client.get_user_link(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.GetUserLinkRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_user_link_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = 'name3373707'

        with pytest.raises(CustomException):
            client.get_user_link(name)

    def test_batch_get_user_links(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = analytics_admin_pb2.BatchGetUserLinksResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.account_path('[ACCOUNT]')
        names = []

        response = client.batch_get_user_links(parent, names)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.BatchGetUserLinksRequest(parent=parent, names=names)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_batch_get_user_links_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.account_path('[ACCOUNT]')
        names = []

        with pytest.raises(CustomException):
            client.batch_get_user_links(parent, names)

    def test_list_user_links(self):
        # Setup Expected Response
        next_page_token = ''
        user_links_element = {}
        user_links = [user_links_element]
        expected_response = {'next_page_token': next_page_token, 'user_links': user_links}
        expected_response = analytics_admin_pb2.ListUserLinksResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.account_path('[ACCOUNT]')

        paged_list_response = client.list_user_links(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.user_links[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.ListUserLinksRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_user_links_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.account_path('[ACCOUNT]')

        paged_list_response = client.list_user_links(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_audit_user_links(self):
        # Setup Expected Response
        next_page_token = ''
        user_links_element = {}
        user_links = [user_links_element]
        expected_response = {'next_page_token': next_page_token, 'user_links': user_links}
        expected_response = analytics_admin_pb2.AuditUserLinksResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.account_path('[ACCOUNT]')

        paged_list_response = client.audit_user_links(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.user_links[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.AuditUserLinksRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_audit_user_links_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.account_path('[ACCOUNT]')

        paged_list_response = client.audit_user_links(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_create_user_link(self):
        # Setup Expected Response
        name = 'name3373707'
        email_address = 'emailAddress-769510831'
        expected_response = {'name': name, 'email_address': email_address}
        expected_response = resources_pb2.UserLink(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.account_path('[ACCOUNT]')
        user_link = {}

        response = client.create_user_link(parent, user_link)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.CreateUserLinkRequest(parent=parent, user_link=user_link)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_user_link_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.account_path('[ACCOUNT]')
        user_link = {}

        with pytest.raises(CustomException):
            client.create_user_link(parent, user_link)

    def test_batch_create_user_links(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = analytics_admin_pb2.BatchCreateUserLinksResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.account_path('[ACCOUNT]')
        requests = []

        response = client.batch_create_user_links(parent, requests)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.BatchCreateUserLinksRequest(parent=parent, requests=requests)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_batch_create_user_links_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.account_path('[ACCOUNT]')
        requests = []

        with pytest.raises(CustomException):
            client.batch_create_user_links(parent, requests)

    def test_update_user_link(self):
        # Setup Expected Response
        name = 'name3373707'
        email_address = 'emailAddress-769510831'
        expected_response = {'name': name, 'email_address': email_address}
        expected_response = resources_pb2.UserLink(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        user_link = {}

        response = client.update_user_link(user_link)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.UpdateUserLinkRequest(user_link=user_link)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_user_link_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        user_link = {}

        with pytest.raises(CustomException):
            client.update_user_link(user_link)

    def test_batch_update_user_links(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = analytics_admin_pb2.BatchUpdateUserLinksResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.account_path('[ACCOUNT]')
        requests = []

        response = client.batch_update_user_links(parent, requests)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.BatchUpdateUserLinksRequest(parent=parent, requests=requests)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_batch_update_user_links_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.account_path('[ACCOUNT]')
        requests = []

        with pytest.raises(CustomException):
            client.batch_update_user_links(parent, requests)

    def test_delete_user_link(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = 'name3373707'

        client.delete_user_link(name)

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.DeleteUserLinkRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_user_link_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = 'name3373707'

        with pytest.raises(CustomException):
            client.delete_user_link(name)

    def test_batch_delete_user_links(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.account_path('[ACCOUNT]')
        requests = []

        client.batch_delete_user_links(parent, requests)

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.BatchDeleteUserLinksRequest(parent=parent, requests=requests)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_batch_delete_user_links_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.account_path('[ACCOUNT]')
        requests = []

        with pytest.raises(CustomException):
            client.batch_delete_user_links(parent, requests)

    def test_get_web_data_stream(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        measurement_id = 'measurementId-223204226'
        firebase_app_id = 'firebaseAppId605863217'
        default_uri = 'defaultUri-436616594'
        display_name = 'displayName1615086568'
        expected_response = {'name': name_2, 'measurement_id': measurement_id, 'firebase_app_id': firebase_app_id, 'default_uri': default_uri, 'display_name': display_name}
        expected_response = resources_pb2.WebDataStream(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.web_data_stream_path('[PROPERTY]', '[WEB_DATA_STREAM]')

        response = client.get_web_data_stream(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.GetWebDataStreamRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_web_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.web_data_stream_path('[PROPERTY]', '[WEB_DATA_STREAM]')

        with pytest.raises(CustomException):
            client.get_web_data_stream(name)

    def test_delete_web_data_stream(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.web_data_stream_path('[PROPERTY]', '[WEB_DATA_STREAM]')

        client.delete_web_data_stream(name)

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.DeleteWebDataStreamRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_web_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.web_data_stream_path('[PROPERTY]', '[WEB_DATA_STREAM]')

        with pytest.raises(CustomException):
            client.delete_web_data_stream(name)

    def test_update_web_data_stream(self):
        # Setup Expected Response
        name = 'name3373707'
        measurement_id = 'measurementId-223204226'
        firebase_app_id = 'firebaseAppId605863217'
        default_uri = 'defaultUri-436616594'
        display_name = 'displayName1615086568'
        expected_response = {'name': name, 'measurement_id': measurement_id, 'firebase_app_id': firebase_app_id, 'default_uri': default_uri, 'display_name': display_name}
        expected_response = resources_pb2.WebDataStream(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        web_data_stream = {}

        response = client.update_web_data_stream(web_data_stream)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.UpdateWebDataStreamRequest(web_data_stream=web_data_stream)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_web_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        web_data_stream = {}

        with pytest.raises(CustomException):
            client.update_web_data_stream(web_data_stream)

    def test_create_web_data_stream(self):
        # Setup Expected Response
        name = 'name3373707'
        measurement_id = 'measurementId-223204226'
        firebase_app_id = 'firebaseAppId605863217'
        default_uri = 'defaultUri-436616594'
        display_name = 'displayName1615086568'
        expected_response = {'name': name, 'measurement_id': measurement_id, 'firebase_app_id': firebase_app_id, 'default_uri': default_uri, 'display_name': display_name}
        expected_response = resources_pb2.WebDataStream(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        web_data_stream = {}
        parent = client.property_path('[PROPERTY]')

        response = client.create_web_data_stream(web_data_stream, parent)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.CreateWebDataStreamRequest(web_data_stream=web_data_stream, parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_web_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        web_data_stream = {}
        parent = client.property_path('[PROPERTY]')

        with pytest.raises(CustomException):
            client.create_web_data_stream(web_data_stream, parent)

    def test_list_web_data_streams(self):
        # Setup Expected Response
        next_page_token = ''
        web_data_streams_element = {}
        web_data_streams = [web_data_streams_element]
        expected_response = {'next_page_token': next_page_token, 'web_data_streams': web_data_streams}
        expected_response = analytics_admin_pb2.ListWebDataStreamsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.property_path('[PROPERTY]')

        paged_list_response = client.list_web_data_streams(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.web_data_streams[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.ListWebDataStreamsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_web_data_streams_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.property_path('[PROPERTY]')

        paged_list_response = client.list_web_data_streams(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_ios_app_data_stream(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        firebase_app_id = 'firebaseAppId605863217'
        bundle_id = 'bundleId-1479583240'
        display_name = 'displayName1615086568'
        expected_response = {'name': name_2, 'firebase_app_id': firebase_app_id, 'bundle_id': bundle_id, 'display_name': display_name}
        expected_response = resources_pb2.IosAppDataStream(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.ios_app_data_stream_path('[PROPERTY]', '[IOS_APP_DATA_STREAM]')

        response = client.get_ios_app_data_stream(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.GetIosAppDataStreamRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_ios_app_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.ios_app_data_stream_path('[PROPERTY]', '[IOS_APP_DATA_STREAM]')

        with pytest.raises(CustomException):
            client.get_ios_app_data_stream(name)

    def test_delete_ios_app_data_stream(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.ios_app_data_stream_path('[PROPERTY]', '[IOS_APP_DATA_STREAM]')

        client.delete_ios_app_data_stream(name)

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.DeleteIosAppDataStreamRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_ios_app_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.ios_app_data_stream_path('[PROPERTY]', '[IOS_APP_DATA_STREAM]')

        with pytest.raises(CustomException):
            client.delete_ios_app_data_stream(name)

    def test_update_ios_app_data_stream(self):
        # Setup Expected Response
        name = 'name3373707'
        firebase_app_id = 'firebaseAppId605863217'
        bundle_id = 'bundleId-1479583240'
        display_name = 'displayName1615086568'
        expected_response = {'name': name, 'firebase_app_id': firebase_app_id, 'bundle_id': bundle_id, 'display_name': display_name}
        expected_response = resources_pb2.IosAppDataStream(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        ios_app_data_stream = {}

        response = client.update_ios_app_data_stream(ios_app_data_stream)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.UpdateIosAppDataStreamRequest(ios_app_data_stream=ios_app_data_stream)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_ios_app_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        ios_app_data_stream = {}

        with pytest.raises(CustomException):
            client.update_ios_app_data_stream(ios_app_data_stream)

    def test_create_ios_app_data_stream(self):
        # Setup Expected Response
        name = 'name3373707'
        firebase_app_id = 'firebaseAppId605863217'
        bundle_id = 'bundleId-1479583240'
        display_name = 'displayName1615086568'
        expected_response = {'name': name, 'firebase_app_id': firebase_app_id, 'bundle_id': bundle_id, 'display_name': display_name}
        expected_response = resources_pb2.IosAppDataStream(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        ios_app_data_stream = {}
        parent = client.property_path('[PROPERTY]')

        response = client.create_ios_app_data_stream(ios_app_data_stream, parent)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.CreateIosAppDataStreamRequest(ios_app_data_stream=ios_app_data_stream, parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_ios_app_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        ios_app_data_stream = {}
        parent = client.property_path('[PROPERTY]')

        with pytest.raises(CustomException):
            client.create_ios_app_data_stream(ios_app_data_stream, parent)

    def test_list_ios_app_data_streams(self):
        # Setup Expected Response
        next_page_token = ''
        ios_app_data_streams_element = {}
        ios_app_data_streams = [ios_app_data_streams_element]
        expected_response = {'next_page_token': next_page_token, 'ios_app_data_streams': ios_app_data_streams}
        expected_response = analytics_admin_pb2.ListIosAppDataStreamsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.property_path('[PROPERTY]')

        paged_list_response = client.list_ios_app_data_streams(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.ios_app_data_streams[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.ListIosAppDataStreamsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_ios_app_data_streams_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.property_path('[PROPERTY]')

        paged_list_response = client.list_ios_app_data_streams(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_android_app_data_stream(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        firebase_app_id = 'firebaseAppId605863217'
        package_name = 'packageName-1877165340'
        display_name = 'displayName1615086568'
        expected_response = {'name': name_2, 'firebase_app_id': firebase_app_id, 'package_name': package_name, 'display_name': display_name}
        expected_response = resources_pb2.AndroidAppDataStream(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.android_app_data_stream_path('[PROPERTY]', '[ANDROID_APP_DATA_STREAM]')

        response = client.get_android_app_data_stream(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.GetAndroidAppDataStreamRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_android_app_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.android_app_data_stream_path('[PROPERTY]', '[ANDROID_APP_DATA_STREAM]')

        with pytest.raises(CustomException):
            client.get_android_app_data_stream(name)

    def test_delete_android_app_data_stream(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.android_app_data_stream_path('[PROPERTY]', '[ANDROID_APP_DATA_STREAM]')

        client.delete_android_app_data_stream(name)

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.DeleteAndroidAppDataStreamRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_android_app_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.android_app_data_stream_path('[PROPERTY]', '[ANDROID_APP_DATA_STREAM]')

        with pytest.raises(CustomException):
            client.delete_android_app_data_stream(name)

    def test_update_android_app_data_stream(self):
        # Setup Expected Response
        name = 'name3373707'
        firebase_app_id = 'firebaseAppId605863217'
        package_name = 'packageName-1877165340'
        display_name = 'displayName1615086568'
        expected_response = {'name': name, 'firebase_app_id': firebase_app_id, 'package_name': package_name, 'display_name': display_name}
        expected_response = resources_pb2.AndroidAppDataStream(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        android_app_data_stream = {}

        response = client.update_android_app_data_stream(android_app_data_stream)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.UpdateAndroidAppDataStreamRequest(android_app_data_stream=android_app_data_stream)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_android_app_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        android_app_data_stream = {}

        with pytest.raises(CustomException):
            client.update_android_app_data_stream(android_app_data_stream)

    def test_create_android_app_data_stream(self):
        # Setup Expected Response
        name = 'name3373707'
        firebase_app_id = 'firebaseAppId605863217'
        package_name = 'packageName-1877165340'
        display_name = 'displayName1615086568'
        expected_response = {'name': name, 'firebase_app_id': firebase_app_id, 'package_name': package_name, 'display_name': display_name}
        expected_response = resources_pb2.AndroidAppDataStream(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        android_app_data_stream = {}
        parent = client.property_path('[PROPERTY]')

        response = client.create_android_app_data_stream(android_app_data_stream, parent)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.CreateAndroidAppDataStreamRequest(android_app_data_stream=android_app_data_stream, parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_android_app_data_stream_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        android_app_data_stream = {}
        parent = client.property_path('[PROPERTY]')

        with pytest.raises(CustomException):
            client.create_android_app_data_stream(android_app_data_stream, parent)

    def test_list_android_app_data_streams(self):
        # Setup Expected Response
        next_page_token = ''
        android_app_data_streams_element = {}
        android_app_data_streams = [android_app_data_streams_element]
        expected_response = {'next_page_token': next_page_token, 'android_app_data_streams': android_app_data_streams}
        expected_response = analytics_admin_pb2.ListAndroidAppDataStreamsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.property_path('[PROPERTY]')

        paged_list_response = client.list_android_app_data_streams(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.android_app_data_streams[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.ListAndroidAppDataStreamsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_android_app_data_streams_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.property_path('[PROPERTY]')

        paged_list_response = client.list_android_app_data_streams(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_enhanced_measurement_settings(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        stream_enabled = True
        page_views_enabled = True
        scrolls_enabled = True
        outbound_clicks_enabled = True
        content_views_enabled = True
        site_search_enabled = True
        form_interactions_enabled = True
        video_engagement_enabled = False
        file_downloads_enabled = True
        data_tagged_element_clicks_enabled = True
        page_loads_enabled = False
        page_changes_enabled = False
        articles_and_blogs_enabled = False
        products_and_ecommerce_enabled = False
        search_query_parameter = 'searchQueryParameter638048347'
        url_query_parameter = 'urlQueryParameter729598498'
        excluded_domains = 'excludedDomains147054266'
        expected_response = {'name': name_2, 'stream_enabled': stream_enabled, 'page_views_enabled': page_views_enabled, 'scrolls_enabled': scrolls_enabled, 'outbound_clicks_enabled': outbound_clicks_enabled, 'content_views_enabled': content_views_enabled, 'site_search_enabled': site_search_enabled, 'form_interactions_enabled': form_interactions_enabled, 'video_engagement_enabled': video_engagement_enabled, 'file_downloads_enabled': file_downloads_enabled, 'data_tagged_element_clicks_enabled': data_tagged_element_clicks_enabled, 'page_loads_enabled': page_loads_enabled, 'page_changes_enabled': page_changes_enabled, 'articles_and_blogs_enabled': articles_and_blogs_enabled, 'products_and_ecommerce_enabled': products_and_ecommerce_enabled, 'search_query_parameter': search_query_parameter, 'url_query_parameter': url_query_parameter, 'excluded_domains': excluded_domains}
        expected_response = resources_pb2.EnhancedMeasurementSettings(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.enhanced_measurement_settings_path('[PROPERTY]', '[WEB_DATA_STREAM]')

        response = client.get_enhanced_measurement_settings(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.GetEnhancedMeasurementSettingsRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_enhanced_measurement_settings_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.enhanced_measurement_settings_path('[PROPERTY]', '[WEB_DATA_STREAM]')

        with pytest.raises(CustomException):
            client.get_enhanced_measurement_settings(name)

    def test_update_enhanced_measurement_settings(self):
        # Setup Expected Response
        name = 'name3373707'
        stream_enabled = True
        page_views_enabled = True
        scrolls_enabled = True
        outbound_clicks_enabled = True
        content_views_enabled = True
        site_search_enabled = True
        form_interactions_enabled = True
        video_engagement_enabled = False
        file_downloads_enabled = True
        data_tagged_element_clicks_enabled = True
        page_loads_enabled = False
        page_changes_enabled = False
        articles_and_blogs_enabled = False
        products_and_ecommerce_enabled = False
        search_query_parameter = 'searchQueryParameter638048347'
        url_query_parameter = 'urlQueryParameter729598498'
        excluded_domains = 'excludedDomains147054266'
        expected_response = {'name': name, 'stream_enabled': stream_enabled, 'page_views_enabled': page_views_enabled, 'scrolls_enabled': scrolls_enabled, 'outbound_clicks_enabled': outbound_clicks_enabled, 'content_views_enabled': content_views_enabled, 'site_search_enabled': site_search_enabled, 'form_interactions_enabled': form_interactions_enabled, 'video_engagement_enabled': video_engagement_enabled, 'file_downloads_enabled': file_downloads_enabled, 'data_tagged_element_clicks_enabled': data_tagged_element_clicks_enabled, 'page_loads_enabled': page_loads_enabled, 'page_changes_enabled': page_changes_enabled, 'articles_and_blogs_enabled': articles_and_blogs_enabled, 'products_and_ecommerce_enabled': products_and_ecommerce_enabled, 'search_query_parameter': search_query_parameter, 'url_query_parameter': url_query_parameter, 'excluded_domains': excluded_domains}
        expected_response = resources_pb2.EnhancedMeasurementSettings(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        enhanced_measurement_settings = {}

        response = client.update_enhanced_measurement_settings(enhanced_measurement_settings)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.UpdateEnhancedMeasurementSettingsRequest(enhanced_measurement_settings=enhanced_measurement_settings)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_enhanced_measurement_settings_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        enhanced_measurement_settings = {}

        with pytest.raises(CustomException):
            client.update_enhanced_measurement_settings(enhanced_measurement_settings)

    def test_create_firebase_link(self):
        # Setup Expected Response
        name = 'name3373707'
        project = 'project-309310695'
        expected_response = {'name': name, 'project': project}
        expected_response = resources_pb2.FirebaseLink(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.property_path('[PROPERTY]')
        firebase_link = {}

        response = client.create_firebase_link(parent, firebase_link)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.CreateFirebaseLinkRequest(parent=parent, firebase_link=firebase_link)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_firebase_link_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.property_path('[PROPERTY]')
        firebase_link = {}

        with pytest.raises(CustomException):
            client.create_firebase_link(parent, firebase_link)

    def test_update_firebase_link(self):
        # Setup Expected Response
        name = 'name3373707'
        project = 'project-309310695'
        expected_response = {'name': name, 'project': project}
        expected_response = resources_pb2.FirebaseLink(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        firebase_link = {}

        response = client.update_firebase_link(firebase_link)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.UpdateFirebaseLinkRequest(firebase_link=firebase_link)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_firebase_link_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        firebase_link = {}

        with pytest.raises(CustomException):
            client.update_firebase_link(firebase_link)

    def test_delete_firebase_link(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.firebase_link_path('[PROPERTY]', '[FIREBASE_LINK]')

        client.delete_firebase_link(name)

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.DeleteFirebaseLinkRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_firebase_link_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.firebase_link_path('[PROPERTY]', '[FIREBASE_LINK]')

        with pytest.raises(CustomException):
            client.delete_firebase_link(name)

    def test_list_firebase_links(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = analytics_admin_pb2.ListFirebaseLinksResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.property_path('[PROPERTY]')

        response = client.list_firebase_links(parent)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.ListFirebaseLinksRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_firebase_links_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.property_path('[PROPERTY]')

        with pytest.raises(CustomException):
            client.list_firebase_links(parent)

    def test_get_global_site_tag(self):
        # Setup Expected Response
        snippet = 'snippet-2061635299'
        expected_response = {'snippet': snippet}
        expected_response = resources_pb2.GlobalSiteTag(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.global_site_tag_path('[PROPERTY]')

        response = client.get_global_site_tag(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.GetGlobalSiteTagRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_global_site_tag_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.global_site_tag_path('[PROPERTY]')

        with pytest.raises(CustomException):
            client.get_global_site_tag(name)

    def test_create_google_ads_link(self):
        # Setup Expected Response
        name = 'name3373707'
        parent_2 = 'parent21175163357'
        customer_id = 'customerId-1772061412'
        can_manage_clients = False
        email_address = 'emailAddress-769510831'
        expected_response = {'name': name, 'parent': parent_2, 'customer_id': customer_id, 'can_manage_clients': can_manage_clients, 'email_address': email_address}
        expected_response = resources_pb2.GoogleAdsLink(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.property_path('[PROPERTY]')
        google_ads_link = {}

        response = client.create_google_ads_link(parent, google_ads_link)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.CreateGoogleAdsLinkRequest(parent=parent, google_ads_link=google_ads_link)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_google_ads_link_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.property_path('[PROPERTY]')
        google_ads_link = {}

        with pytest.raises(CustomException):
            client.create_google_ads_link(parent, google_ads_link)

    def test_update_google_ads_link(self):
        # Setup Expected Response
        name = 'name3373707'
        parent = 'parent-995424086'
        customer_id = 'customerId-1772061412'
        can_manage_clients = False
        email_address = 'emailAddress-769510831'
        expected_response = {'name': name, 'parent': parent, 'customer_id': customer_id, 'can_manage_clients': can_manage_clients, 'email_address': email_address}
        expected_response = resources_pb2.GoogleAdsLink(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        response = client.update_google_ads_link()
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.UpdateGoogleAdsLinkRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_google_ads_link_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        with pytest.raises(CustomException):
            client.update_google_ads_link()

    def test_delete_google_ads_link(self):
        channel = ChannelStub()
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.google_ads_link_path('[PROPERTY]', '[GOOGLE_ADS_LINK]')

        client.delete_google_ads_link(name)

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.DeleteGoogleAdsLinkRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_google_ads_link_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.google_ads_link_path('[PROPERTY]', '[GOOGLE_ADS_LINK]')

        with pytest.raises(CustomException):
            client.delete_google_ads_link(name)

    def test_list_google_ads_links(self):
        # Setup Expected Response
        next_page_token = ''
        google_ads_links_element = {}
        google_ads_links = [google_ads_links_element]
        expected_response = {'next_page_token': next_page_token, 'google_ads_links': google_ads_links}
        expected_response = analytics_admin_pb2.ListGoogleAdsLinksResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        parent = client.property_path('[PROPERTY]')

        paged_list_response = client.list_google_ads_links(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.google_ads_links[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.ListGoogleAdsLinksRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_google_ads_links_exception(self):
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        parent = client.property_path('[PROPERTY]')

        paged_list_response = client.list_google_ads_links(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_data_sharing_settings(self):
        # Setup Expected Response
        name_2 = 'name2-1052831874'
        sharing_with_google_support_enabled = False
        sharing_with_google_assigned_sales_enabled = False
        sharing_with_google_any_sales_enabled = False
        sharing_with_google_products_enabled = True
        sharing_with_others_enabled = False
        expected_response = {'name': name_2, 'sharing_with_google_support_enabled': sharing_with_google_support_enabled, 'sharing_with_google_assigned_sales_enabled': sharing_with_google_assigned_sales_enabled, 'sharing_with_google_any_sales_enabled': sharing_with_google_any_sales_enabled, 'sharing_with_google_products_enabled': sharing_with_google_products_enabled, 'sharing_with_others_enabled': sharing_with_others_enabled}
        expected_response = resources_pb2.DataSharingSettings(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses = [expected_response])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup Request
        name = client.data_sharing_settings_path('[ACCOUNT]')

        response = client.get_data_sharing_settings(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = analytics_admin_pb2.GetDataSharingSettingsRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_data_sharing_settings_exception(self):
        # Mock the API response
        channel = ChannelStub(responses = [CustomException()])
        patch = mock.patch('google.api_core.grpc_helpers.create_channel')
        with patch as create_channel:
            create_channel.return_value = channel
            client = v1alpha.AnalyticsAdminServiceClient()

        # Setup request
        name = client.data_sharing_settings_path('[ACCOUNT]')

        with pytest.raises(CustomException):
            client.get_data_sharing_settings(name)
