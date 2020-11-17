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

"""Accesses the google.analytics.admin.v1alpha AnalyticsAdminService API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.analytics.admin.v1alpha.gapic import analytics_admin_service_client_config
from google.analytics.admin.v1alpha.gapic import enums
from google.analytics.admin.v1alpha.gapic.transports import analytics_admin_service_grpc_transport
from google.analytics.admin.v1alpha.proto import analytics_admin_pb2
from google.analytics.admin.v1alpha.proto import analytics_admin_pb2_grpc
from google.analytics.admin.v1alpha.proto import resources_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2



_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    'google-cloud-analytics-admin',
).version


class AnalyticsAdminServiceClient(object):
    """Service Interface for the Analytics Admin API (GA4)."""

    SERVICE_ADDRESS = 'analyticsadmin.googleapis.com:443'
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = 'google.analytics.admin.v1alpha.AnalyticsAdminService'


    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AnalyticsAdminServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename)
        kwargs['credentials'] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file


    @classmethod
    def account_path(cls, account):
        """Return a fully-qualified account string."""
        return google.api_core.path_template.expand(
            'accounts/{account}',
            account=account,
        )

    @classmethod
    def android_app_data_stream_path(cls, property_, android_app_data_stream):
        """Return a fully-qualified android_app_data_stream string."""
        return google.api_core.path_template.expand(
            'properties/{property}/androidAppDataStreams/{android_app_data_stream}',
            property=property_,
            android_app_data_stream=android_app_data_stream,
        )

    @classmethod
    def data_sharing_settings_path(cls, account):
        """Return a fully-qualified data_sharing_settings string."""
        return google.api_core.path_template.expand(
            'accounts/{account}/dataSharingSettings',
            account=account,
        )

    @classmethod
    def enhanced_measurement_settings_path(cls, property_, web_data_stream):
        """Return a fully-qualified enhanced_measurement_settings string."""
        return google.api_core.path_template.expand(
            'properties/{property}/webDataStreams/{web_data_stream}/enhancedMeasurementSettings',
            property=property_,
            web_data_stream=web_data_stream,
        )

    @classmethod
    def firebase_link_path(cls, property_, firebase_link):
        """Return a fully-qualified firebase_link string."""
        return google.api_core.path_template.expand(
            'properties/{property}/firebaseLinks/{firebase_link}',
            property=property_,
            firebase_link=firebase_link,
        )

    @classmethod
    def global_site_tag_path(cls, property_):
        """Return a fully-qualified global_site_tag string."""
        return google.api_core.path_template.expand(
            'properties/{property}/globalSiteTag',
            property=property_,
        )

    @classmethod
    def google_ads_link_path(cls, property_, google_ads_link):
        """Return a fully-qualified google_ads_link string."""
        return google.api_core.path_template.expand(
            'properties/{property}/googleAdsLinks/{google_ads_link}',
            property=property_,
            google_ads_link=google_ads_link,
        )

    @classmethod
    def ios_app_data_stream_path(cls, property_, ios_app_data_stream):
        """Return a fully-qualified ios_app_data_stream string."""
        return google.api_core.path_template.expand(
            'properties/{property}/iosAppDataStreams/{ios_app_data_stream}',
            property=property_,
            ios_app_data_stream=ios_app_data_stream,
        )

    @classmethod
    def property_path(cls, property_):
        """Return a fully-qualified property string."""
        return google.api_core.path_template.expand(
            'properties/{property}',
            property=property_,
        )

    @classmethod
    def user_link_path(cls, account, user_link):
        """Return a fully-qualified user_link string."""
        return google.api_core.path_template.expand(
            'accounts/{account}/userLinks/{user_link}',
            account=account,
            user_link=user_link,
        )

    @classmethod
    def web_data_stream_path(cls, property_, web_data_stream):
        """Return a fully-qualified web_data_stream string."""
        return google.api_core.path_template.expand(
            'properties/{property}/webDataStreams/{web_data_stream}',
            property=property_,
            web_data_stream=web_data_stream,
        )

    def __init__(self, transport=None, channel=None, credentials=None,
            client_config=None, client_info=None, client_options=None):
        """Constructor.

        Args:
            transport (Union[~.AnalyticsAdminServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.AnalyticsAdminServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn('The `client_config` argument is deprecated.',
                          PendingDeprecationWarning, stacklevel=2)
        else:
            client_config = analytics_admin_service_client_config.config

        if channel:
            warnings.warn('The `channel` argument is deprecated; use '
                          '`transport` instead.',
                          PendingDeprecationWarning, stacklevel=2)

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(client_options)
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=analytics_admin_service_grpc_transport.AnalyticsAdminServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        'Received both a transport instance and '
                        'credentials; these are mutually exclusive.'
                    )
                self.transport = transport
        else:
            self.transport = analytics_admin_service_grpc_transport.AnalyticsAdminServiceGrpcTransport(
                address=api_endpoint,
                channel=channel,
                credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config['interfaces'][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def get_account(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Lookup for a single Account.
        Throws "Target not found" if no such account found, or if caller does not
        have permissions to access it.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.account_path('[ACCOUNT]')
            >>>
            >>> response = client.get_account(name)

        Args:
            name (str): Required. The name of the account to lookup.
                Format: accounts/{account}
                Example: "accounts/100"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.Account` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_account' not in self._inner_api_calls:
            self._inner_api_calls['get_account'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_account,
                default_retry=self._method_configs['GetAccount'].retry,
                default_timeout=self._method_configs['GetAccount'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.GetAccountRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_account'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_accounts(
            self,
            page_size=None,
            show_deleted=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Returns all accounts accessible by the caller.

        Note that these accounts might not currently have GA4 properties.
        Soft-deleted (ie: "trashed") accounts are excluded by default.
        Returns an empty list if no relevant accounts are found.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_accounts():
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_accounts().pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            show_deleted (bool): Whether to include soft-deleted (ie: "trashed") Accounts in the
                results. Accounts can be inspected to determine whether they are deleted or
                not.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.analytics.admin.v1alpha.types.Account` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_accounts' not in self._inner_api_calls:
            self._inner_api_calls['list_accounts'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_accounts,
                default_retry=self._method_configs['ListAccounts'].retry,
                default_timeout=self._method_configs['ListAccounts'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.ListAccountsRequest(
            page_size=page_size,
            show_deleted=show_deleted,
        )
        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(self._inner_api_calls['list_accounts'], retry=retry, timeout=timeout, metadata=metadata),
            request=request,
            items_field='accounts',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator

    def delete_account(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Marks target Account as soft-deleted (ie: "trashed") and returns it.

        This API does not have a method to restore soft-deleted accounts.
        However, they can be restored using the Trash Can UI.

        If the accounts are not restored before the expiration time, the account
        and all child resources (eg: Properties, GoogleAdsLinks, Streams,
        UserLinks) will be permanently purged.
        https://support.google.com/analytics/answer/6154772

        Returns an error if the target is not found.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.account_path('[ACCOUNT]')
            >>>
            >>> client.delete_account(name)

        Args:
            name (str): Required. The name of the Account to soft-delete.
                Format: accounts/{account}
                Example: "accounts/100"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_account' not in self._inner_api_calls:
            self._inner_api_calls['delete_account'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_account,
                default_retry=self._method_configs['DeleteAccount'].retry,
                default_timeout=self._method_configs['DeleteAccount'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.DeleteAccountRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['delete_account'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_account(
            self,
            account,
            update_mask=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates an account.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `account`:
            >>> account = {}
            >>>
            >>> response = client.update_account(account)

        Args:
            account (Union[dict, ~google.analytics.admin.v1alpha.types.Account]): Required. The account to update. The account's ``name`` field is
                used to identify the account.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.Account`
            update_mask (Union[dict, ~google.analytics.admin.v1alpha.types.FieldMask]): The list of fields to be updated. Omitted fields will not be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.Account` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_account' not in self._inner_api_calls:
            self._inner_api_calls['update_account'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_account,
                default_retry=self._method_configs['UpdateAccount'].retry,
                default_timeout=self._method_configs['UpdateAccount'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.UpdateAccountRequest(
            account=account,
            update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('account.name', account.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_account'](request, retry=retry, timeout=timeout, metadata=metadata)

    def provision_account_ticket(
            self,
            account=None,
            redirect_uri=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Requests a ticket for creating an account.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> response = client.provision_account_ticket()

        Args:
            account (Union[dict, ~google.analytics.admin.v1alpha.types.Account]): The account to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.Account`
            redirect_uri (str): Redirect URI where the user will be sent after accepting Terms of Service.
                Must be configured in Developers Console as a Redirect URI
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.ProvisionAccountTicketResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'provision_account_ticket' not in self._inner_api_calls:
            self._inner_api_calls['provision_account_ticket'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.provision_account_ticket,
                default_retry=self._method_configs['ProvisionAccountTicket'].retry,
                default_timeout=self._method_configs['ProvisionAccountTicket'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.ProvisionAccountTicketRequest(
            account=account,
            redirect_uri=redirect_uri,
        )
        return self._inner_api_calls['provision_account_ticket'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_account_summaries(
            self,
            page_size=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Returns summaries of all accounts accessible by the caller.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_account_summaries():
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_account_summaries().pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.analytics.admin.v1alpha.types.AccountSummary` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_account_summaries' not in self._inner_api_calls:
            self._inner_api_calls['list_account_summaries'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_account_summaries,
                default_retry=self._method_configs['ListAccountSummaries'].retry,
                default_timeout=self._method_configs['ListAccountSummaries'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.ListAccountSummariesRequest(
            page_size=page_size,
        )
        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(self._inner_api_calls['list_account_summaries'], retry=retry, timeout=timeout, metadata=metadata),
            request=request,
            items_field='account_summaries',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator

    def get_property(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Lookup for a single "GA4" Property.

        Throws "Target not found" if no such property found, if property is not
        of the type "GA4", or if caller does not have permissions to access it.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.property_path('[PROPERTY]')
            >>>
            >>> response = client.get_property(name)

        Args:
            name (str): Required. The name of the property to lookup. Format:
                properties/{property_id} Example: "properties/1000"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.Property` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_property' not in self._inner_api_calls:
            self._inner_api_calls['get_property'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_property,
                default_retry=self._method_configs['GetProperty'].retry,
                default_timeout=self._method_configs['GetProperty'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.GetPropertyRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_property'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_properties(
            self,
            filter_,
            page_size=None,
            show_deleted=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Returns child Properties under the specified parent Account.

        Only "GA4" properties will be returned.
        Properties will be excluded if the caller does not have access.
        Soft-deleted (ie: "trashed") properties are excluded by default.
        Returns an empty list if no relevant properties are found.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `filter_`:
            >>> filter_ = ''
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_properties(filter_):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_properties(filter_).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            filter_ (str): Required. An expression for filtering the results of the request.
                Fields eligible for filtering are: ``parent:``\ (The resource name of
                the parent account) or ``firebase_project:``\ (The id or number of the
                linked firebase project). Some examples of filters:

                \| Filter \| Description \|
                \|-----------------------------|-------------------------------------------\|
                \| parent:accounts/123 \| The account with account id: 123. \| \|
                firebase_project:project-id \| The firebase project with id: project-id.
                \| \| firebase_project:123 \| The firebase project with number: 123. \|
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            show_deleted (bool): Whether to include soft-deleted (ie: "trashed") Properties in the
                results. Properties can be inspected to determine whether they are deleted
                or not.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.analytics.admin.v1alpha.types.Property` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_properties' not in self._inner_api_calls:
            self._inner_api_calls['list_properties'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_properties,
                default_retry=self._method_configs['ListProperties'].retry,
                default_timeout=self._method_configs['ListProperties'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.ListPropertiesRequest(
            filter=filter_,
            page_size=page_size,
            show_deleted=show_deleted,
        )
        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(self._inner_api_calls['list_properties'], retry=retry, timeout=timeout, metadata=metadata),
            request=request,
            items_field='properties',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator

    def create_property(
            self,
            property_,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates an "GA4" property with the specified location and attributes.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `property_`:
            >>> property_ = {}
            >>>
            >>> response = client.create_property(property_)

        Args:
            property_ (Union[dict, ~google.analytics.admin.v1alpha.types.Property]): Required. The property to create.
                Note: the supplied property must specify its parent.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.Property`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.Property` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_property' not in self._inner_api_calls:
            self._inner_api_calls['create_property'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_property,
                default_retry=self._method_configs['CreateProperty'].retry,
                default_timeout=self._method_configs['CreateProperty'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.CreatePropertyRequest(
            property=property_,
        )
        return self._inner_api_calls['create_property'](request, retry=retry, timeout=timeout, metadata=metadata)

    def delete_property(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Marks target Property as soft-deleted (ie: "trashed") and returns it.

        This API does not have a method to restore soft-deleted properties.
        However, they can be restored using the Trash Can UI.

        If the properties are not restored before the expiration time, the Property
        and all child resources (eg: GoogleAdsLinks, Streams, UserLinks)
        will be permanently purged.
        https://support.google.com/analytics/answer/6154772

        Returns an error if the target is not found, or is not an GA4 Property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.property_path('[PROPERTY]')
            >>>
            >>> client.delete_property(name)

        Args:
            name (str): Required. The name of the Property to soft-delete. Format:
                properties/{property_id} Example: "properties/1000"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_property' not in self._inner_api_calls:
            self._inner_api_calls['delete_property'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_property,
                default_retry=self._method_configs['DeleteProperty'].retry,
                default_timeout=self._method_configs['DeleteProperty'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.DeletePropertyRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['delete_property'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_property(
            self,
            property_,
            update_mask=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates a property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `property_`:
            >>> property_ = {}
            >>>
            >>> response = client.update_property(property_)

        Args:
            property_ (Union[dict, ~google.analytics.admin.v1alpha.types.Property]): Required. The property to update. The property's ``name`` field is
                used to identify the property to be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.Property`
            update_mask (Union[dict, ~google.analytics.admin.v1alpha.types.FieldMask]): The list of fields to be updated. Omitted fields will not be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.Property` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_property' not in self._inner_api_calls:
            self._inner_api_calls['update_property'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_property,
                default_retry=self._method_configs['UpdateProperty'].retry,
                default_timeout=self._method_configs['UpdateProperty'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.UpdatePropertyRequest(
            property=property_,
            update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('property.name', property.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_property'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_user_link(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Gets information about a user's link to an account or property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> response = client.get_user_link(name)

        Args:
            name (str): Required. Example format: accounts/1234/userLinks/5678
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.UserLink` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_user_link' not in self._inner_api_calls:
            self._inner_api_calls['get_user_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_user_link,
                default_retry=self._method_configs['GetUserLink'].retry,
                default_timeout=self._method_configs['GetUserLink'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.GetUserLinkRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_user_link'](request, retry=retry, timeout=timeout, metadata=metadata)

    def batch_get_user_links(
            self,
            parent,
            names,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Gets information about multiple users' links to an account or property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.account_path('[ACCOUNT]')
            >>>
            >>> # TODO: Initialize `names`:
            >>> names = []
            >>>
            >>> response = client.batch_get_user_links(parent, names)

        Args:
            parent (str): Required. The account or property that all user links in the request are
                for. The parent of all provided values for the 'names' field must match
                this field.
                Example format: accounts/1234
            names (list[str]): Required. The names of the user links to retrieve.
                A maximum of 1000 user links can be retrieved in a batch.
                Format: accounts/{accountId}/userLinks/{userLinkId}
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.BatchGetUserLinksResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'batch_get_user_links' not in self._inner_api_calls:
            self._inner_api_calls['batch_get_user_links'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_get_user_links,
                default_retry=self._method_configs['BatchGetUserLinks'].retry,
                default_timeout=self._method_configs['BatchGetUserLinks'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.BatchGetUserLinksRequest(
            parent=parent,
            names=names,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['batch_get_user_links'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_user_links(
            self,
            parent,
            page_size=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Lists all user links on an account or property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.account_path('[ACCOUNT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_user_links(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_user_links(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. Example format: accounts/1234
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.analytics.admin.v1alpha.types.UserLink` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_user_links' not in self._inner_api_calls:
            self._inner_api_calls['list_user_links'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_user_links,
                default_retry=self._method_configs['ListUserLinks'].retry,
                default_timeout=self._method_configs['ListUserLinks'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.ListUserLinksRequest(
            parent=parent,
            page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(self._inner_api_calls['list_user_links'], retry=retry, timeout=timeout, metadata=metadata),
            request=request,
            items_field='user_links',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator

    def audit_user_links(
            self,
            parent,
            page_size=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Lists all user links on an account or property, including implicit ones
        that come from effective permissions granted by groups or organization
        admin roles.

        If a returned user link does not have direct permissions, they cannot
        be removed from the account or property directly with the DeleteUserLink
        command. They have to be removed from the group/etc that gives them
        permissions, which is currently only usable/discoverable in the GA or GMP
        UIs.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.account_path('[ACCOUNT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.audit_user_links(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.audit_user_links(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. Example format: accounts/1234
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.analytics.admin.v1alpha.types.AuditUserLink` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'audit_user_links' not in self._inner_api_calls:
            self._inner_api_calls['audit_user_links'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.audit_user_links,
                default_retry=self._method_configs['AuditUserLinks'].retry,
                default_timeout=self._method_configs['AuditUserLinks'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.AuditUserLinksRequest(
            parent=parent,
            page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(self._inner_api_calls['audit_user_links'], retry=retry, timeout=timeout, metadata=metadata),
            request=request,
            items_field='user_links',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator

    def create_user_link(
            self,
            parent,
            user_link,
            notify_new_user=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates a user link on an account or property.

        If the user with the specified email already has permissions on the
        account or property, then the user's existing permissions will be unioned
        with the permissions specified in the new UserLink.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.account_path('[ACCOUNT]')
            >>>
            >>> # TODO: Initialize `user_link`:
            >>> user_link = {}
            >>>
            >>> response = client.create_user_link(parent, user_link)

        Args:
            parent (str): Required. Example format: accounts/1234
            user_link (Union[dict, ~google.analytics.admin.v1alpha.types.UserLink]): Required. The user link to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.UserLink`
            notify_new_user (bool): Optional. If set, then email the new user notifying them that they've been granted
                permissions to the resource.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.UserLink` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_user_link' not in self._inner_api_calls:
            self._inner_api_calls['create_user_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_user_link,
                default_retry=self._method_configs['CreateUserLink'].retry,
                default_timeout=self._method_configs['CreateUserLink'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.CreateUserLinkRequest(
            parent=parent,
            user_link=user_link,
            notify_new_user=notify_new_user,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_user_link'](request, retry=retry, timeout=timeout, metadata=metadata)

    def batch_create_user_links(
            self,
            parent,
            requests,
            notify_new_users=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates information about multiple users' links to an account or property.

        This method is transactional. If any UserLink cannot be created, none of
        the UserLinks will be created.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.account_path('[ACCOUNT]')
            >>>
            >>> # TODO: Initialize `requests`:
            >>> requests = []
            >>>
            >>> response = client.batch_create_user_links(parent, requests)

        Args:
            parent (str): Required. The account or property that all user links in the request are for.
                This field is required. The parent field in the CreateUserLinkRequest
                messages must either be empty or match this field.
                Example format: accounts/1234
            requests (list[Union[dict, ~google.analytics.admin.v1alpha.types.CreateUserLinkRequest]]): Required. The requests specifying the user links to create.
                A maximum of 1000 user links can be created in a batch.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.CreateUserLinkRequest`
            notify_new_users (bool): Optional. If set, then email the new users notifying them that
                they've been granted permissions to the resource. Regardless of whether
                this is set or not, notify_new_user field inside each individual request
                is ignored.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.BatchCreateUserLinksResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'batch_create_user_links' not in self._inner_api_calls:
            self._inner_api_calls['batch_create_user_links'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_create_user_links,
                default_retry=self._method_configs['BatchCreateUserLinks'].retry,
                default_timeout=self._method_configs['BatchCreateUserLinks'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.BatchCreateUserLinksRequest(
            parent=parent,
            requests=requests,
            notify_new_users=notify_new_users,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['batch_create_user_links'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_user_link(
            self,
            user_link,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates a user link on an account or property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `user_link`:
            >>> user_link = {}
            >>>
            >>> response = client.update_user_link(user_link)

        Args:
            user_link (Union[dict, ~google.analytics.admin.v1alpha.types.UserLink]): Required. The user link to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.UserLink`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.UserLink` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_user_link' not in self._inner_api_calls:
            self._inner_api_calls['update_user_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_user_link,
                default_retry=self._method_configs['UpdateUserLink'].retry,
                default_timeout=self._method_configs['UpdateUserLink'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.UpdateUserLinkRequest(
            user_link=user_link,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('user_link.name', user_link.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_user_link'](request, retry=retry, timeout=timeout, metadata=metadata)

    def batch_update_user_links(
            self,
            parent,
            requests,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates information about multiple users' links to an account or property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.account_path('[ACCOUNT]')
            >>>
            >>> # TODO: Initialize `requests`:
            >>> requests = []
            >>>
            >>> response = client.batch_update_user_links(parent, requests)

        Args:
            parent (str): Required. The account or property that all user links in the request are
                for. The parent field in the UpdateUserLinkRequest messages must either be
                empty or match this field.
                Example format: accounts/1234
            requests (list[Union[dict, ~google.analytics.admin.v1alpha.types.UpdateUserLinkRequest]]): Required. The requests specifying the user links to update.
                A maximum of 1000 user links can be updated in a batch.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.UpdateUserLinkRequest`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.BatchUpdateUserLinksResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'batch_update_user_links' not in self._inner_api_calls:
            self._inner_api_calls['batch_update_user_links'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_update_user_links,
                default_retry=self._method_configs['BatchUpdateUserLinks'].retry,
                default_timeout=self._method_configs['BatchUpdateUserLinks'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.BatchUpdateUserLinksRequest(
            parent=parent,
            requests=requests,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['batch_update_user_links'](request, retry=retry, timeout=timeout, metadata=metadata)

    def delete_user_link(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Deletes a user link on an account or property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `name`:
            >>> name = ''
            >>>
            >>> client.delete_user_link(name)

        Args:
            name (str): Required. Example format: accounts/1234/userLinks/5678
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_user_link' not in self._inner_api_calls:
            self._inner_api_calls['delete_user_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_user_link,
                default_retry=self._method_configs['DeleteUserLink'].retry,
                default_timeout=self._method_configs['DeleteUserLink'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.DeleteUserLinkRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['delete_user_link'](request, retry=retry, timeout=timeout, metadata=metadata)

    def batch_delete_user_links(
            self,
            parent,
            requests,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Deletes information about multiple users' links to an account or property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.account_path('[ACCOUNT]')
            >>>
            >>> # TODO: Initialize `requests`:
            >>> requests = []
            >>>
            >>> client.batch_delete_user_links(parent, requests)

        Args:
            parent (str): Required. The account or property that all user links in the request are
                for. The parent of all values for user link names to delete must match this
                field.
                Example format: accounts/1234
            requests (list[Union[dict, ~google.analytics.admin.v1alpha.types.DeleteUserLinkRequest]]): Required. The requests specifying the user links to update.
                A maximum of 1000 user links can be updated in a batch.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.DeleteUserLinkRequest`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'batch_delete_user_links' not in self._inner_api_calls:
            self._inner_api_calls['batch_delete_user_links'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_delete_user_links,
                default_retry=self._method_configs['BatchDeleteUserLinks'].retry,
                default_timeout=self._method_configs['BatchDeleteUserLinks'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.BatchDeleteUserLinksRequest(
            parent=parent,
            requests=requests,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['batch_delete_user_links'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_web_data_stream(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Lookup for a single WebDataStream

        Throws "Target not found" if no such web data stream found, or if the
        caller does not have permissions to access it.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.web_data_stream_path('[PROPERTY]', '[WEB_DATA_STREAM]')
            >>>
            >>> response = client.get_web_data_stream(name)

        Args:
            name (str): Required. The name of the web data stream to lookup. Format:
                properties/{property_id}/webDataStreams/{stream_id} Example:
                "properties/123/webDataStreams/456"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.WebDataStream` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_web_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['get_web_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_web_data_stream,
                default_retry=self._method_configs['GetWebDataStream'].retry,
                default_timeout=self._method_configs['GetWebDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.GetWebDataStreamRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_web_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def delete_web_data_stream(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Deletes a web stream on a property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.web_data_stream_path('[PROPERTY]', '[WEB_DATA_STREAM]')
            >>>
            >>> client.delete_web_data_stream(name)

        Args:
            name (str): Required. The name of the web data stream to delete. Format:
                properties/{property_id}/webDataStreams/{stream_id} Example:
                "properties/123/webDataStreams/456"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_web_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['delete_web_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_web_data_stream,
                default_retry=self._method_configs['DeleteWebDataStream'].retry,
                default_timeout=self._method_configs['DeleteWebDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.DeleteWebDataStreamRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['delete_web_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_web_data_stream(
            self,
            web_data_stream,
            update_mask=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates a web stream on a property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `web_data_stream`:
            >>> web_data_stream = {}
            >>>
            >>> response = client.update_web_data_stream(web_data_stream)

        Args:
            web_data_stream (Union[dict, ~google.analytics.admin.v1alpha.types.WebDataStream]): Required. The web stream to update. The ``name`` field is used to
                identify the web stream to be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.WebDataStream`
            update_mask (Union[dict, ~google.analytics.admin.v1alpha.types.FieldMask]): The list of fields to be updated. Omitted fields will not be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.WebDataStream` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_web_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['update_web_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_web_data_stream,
                default_retry=self._method_configs['UpdateWebDataStream'].retry,
                default_timeout=self._method_configs['UpdateWebDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.UpdateWebDataStreamRequest(
            web_data_stream=web_data_stream,
            update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('web_data_stream.name', web_data_stream.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_web_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def create_web_data_stream(
            self,
            web_data_stream,
            parent,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates a web stream with the specified location and attributes.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `web_data_stream`:
            >>> web_data_stream = {}
            >>> parent = client.property_path('[PROPERTY]')
            >>>
            >>> response = client.create_web_data_stream(web_data_stream, parent)

        Args:
            web_data_stream (Union[dict, ~google.analytics.admin.v1alpha.types.WebDataStream]): Required. The web stream to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.WebDataStream`
            parent (str): Required. The parent resource where this web data stream will be created.
                Format: properties/123
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.WebDataStream` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_web_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['create_web_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_web_data_stream,
                default_retry=self._method_configs['CreateWebDataStream'].retry,
                default_timeout=self._method_configs['CreateWebDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.CreateWebDataStreamRequest(
            web_data_stream=web_data_stream,
            parent=parent,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_web_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_web_data_streams(
            self,
            parent,
            page_size=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Returns child web data streams under the specified parent property.

        Web data streams will be excluded if the caller does not have access.
        Returns an empty list if no relevant web data streams are found.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.property_path('[PROPERTY]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_web_data_streams(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_web_data_streams(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The name of the parent property.
                For example, to list results of web streams under the property with Id
                123: "properties/123"
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.analytics.admin.v1alpha.types.WebDataStream` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_web_data_streams' not in self._inner_api_calls:
            self._inner_api_calls['list_web_data_streams'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_web_data_streams,
                default_retry=self._method_configs['ListWebDataStreams'].retry,
                default_timeout=self._method_configs['ListWebDataStreams'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.ListWebDataStreamsRequest(
            parent=parent,
            page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(self._inner_api_calls['list_web_data_streams'], retry=retry, timeout=timeout, metadata=metadata),
            request=request,
            items_field='web_data_streams',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator

    def get_ios_app_data_stream(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Lookup for a single IosAppDataStream

        Throws "Target not found" if no such iOS app data stream found, or if the
        caller does not have permissions to access it.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.ios_app_data_stream_path('[PROPERTY]', '[IOS_APP_DATA_STREAM]')
            >>>
            >>> response = client.get_ios_app_data_stream(name)

        Args:
            name (str): Required. The name of the iOS app data stream to lookup. Format:
                properties/{property_id}/iosAppDataStreams/{stream_id} Example:
                "properties/123/iosAppDataStreams/456"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.IosAppDataStream` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_ios_app_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['get_ios_app_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_ios_app_data_stream,
                default_retry=self._method_configs['GetIosAppDataStream'].retry,
                default_timeout=self._method_configs['GetIosAppDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.GetIosAppDataStreamRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_ios_app_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def delete_ios_app_data_stream(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Deletes an iOS app stream on a property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.ios_app_data_stream_path('[PROPERTY]', '[IOS_APP_DATA_STREAM]')
            >>>
            >>> client.delete_ios_app_data_stream(name)

        Args:
            name (str): Required. The name of the iOS app data stream to delete. Format:
                properties/{property_id}/iosAppDataStreams/{stream_id} Example:
                "properties/123/iosAppDataStreams/456"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_ios_app_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['delete_ios_app_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_ios_app_data_stream,
                default_retry=self._method_configs['DeleteIosAppDataStream'].retry,
                default_timeout=self._method_configs['DeleteIosAppDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.DeleteIosAppDataStreamRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['delete_ios_app_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_ios_app_data_stream(
            self,
            ios_app_data_stream,
            update_mask=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates an iOS app stream on a property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `ios_app_data_stream`:
            >>> ios_app_data_stream = {}
            >>>
            >>> response = client.update_ios_app_data_stream(ios_app_data_stream)

        Args:
            ios_app_data_stream (Union[dict, ~google.analytics.admin.v1alpha.types.IosAppDataStream]): Required. The iOS app stream to update. The ``name`` field is used
                to identify the iOS app stream to be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.IosAppDataStream`
            update_mask (Union[dict, ~google.analytics.admin.v1alpha.types.FieldMask]): The list of fields to be updated. Omitted fields will not be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.IosAppDataStream` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_ios_app_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['update_ios_app_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_ios_app_data_stream,
                default_retry=self._method_configs['UpdateIosAppDataStream'].retry,
                default_timeout=self._method_configs['UpdateIosAppDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.UpdateIosAppDataStreamRequest(
            ios_app_data_stream=ios_app_data_stream,
            update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('ios_app_data_stream.name', ios_app_data_stream.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_ios_app_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def create_ios_app_data_stream(
            self,
            ios_app_data_stream,
            parent,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates an iOS app data stream with the specified location and attributes.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `ios_app_data_stream`:
            >>> ios_app_data_stream = {}
            >>> parent = client.property_path('[PROPERTY]')
            >>>
            >>> response = client.create_ios_app_data_stream(ios_app_data_stream, parent)

        Args:
            ios_app_data_stream (Union[dict, ~google.analytics.admin.v1alpha.types.IosAppDataStream]): Required. The iOS app data stream to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.IosAppDataStream`
            parent (str): Required. The parent resource where this ios app data stream will be created.
                Format: properties/123
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.IosAppDataStream` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_ios_app_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['create_ios_app_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_ios_app_data_stream,
                default_retry=self._method_configs['CreateIosAppDataStream'].retry,
                default_timeout=self._method_configs['CreateIosAppDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.CreateIosAppDataStreamRequest(
            ios_app_data_stream=ios_app_data_stream,
            parent=parent,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_ios_app_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_ios_app_data_streams(
            self,
            parent,
            page_size=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Returns child iOS app data streams under the specified parent property.

        iOS app data streams will be excluded if the caller does not have access.
        Returns an empty list if no relevant iOS app data streams are found.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.property_path('[PROPERTY]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_ios_app_data_streams(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_ios_app_data_streams(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The name of the parent property.
                For example, to list results of app streams under the property with Id
                123: "properties/123"
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.analytics.admin.v1alpha.types.IosAppDataStream` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_ios_app_data_streams' not in self._inner_api_calls:
            self._inner_api_calls['list_ios_app_data_streams'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_ios_app_data_streams,
                default_retry=self._method_configs['ListIosAppDataStreams'].retry,
                default_timeout=self._method_configs['ListIosAppDataStreams'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.ListIosAppDataStreamsRequest(
            parent=parent,
            page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(self._inner_api_calls['list_ios_app_data_streams'], retry=retry, timeout=timeout, metadata=metadata),
            request=request,
            items_field='ios_app_data_streams',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator

    def get_android_app_data_stream(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Lookup for a single AndroidAppDataStream

        Throws "Target not found" if no such android app data stream found, or if
        the caller does not have permissions to access it.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.android_app_data_stream_path('[PROPERTY]', '[ANDROID_APP_DATA_STREAM]')
            >>>
            >>> response = client.get_android_app_data_stream(name)

        Args:
            name (str): Required. The name of the android app data stream to lookup. Format:
                properties/{property_id}/androidAppDataStreams/{stream_id} Example:
                "properties/123/androidAppDataStreams/456"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.AndroidAppDataStream` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_android_app_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['get_android_app_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_android_app_data_stream,
                default_retry=self._method_configs['GetAndroidAppDataStream'].retry,
                default_timeout=self._method_configs['GetAndroidAppDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.GetAndroidAppDataStreamRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_android_app_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def delete_android_app_data_stream(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Deletes an android app stream on a property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.android_app_data_stream_path('[PROPERTY]', '[ANDROID_APP_DATA_STREAM]')
            >>>
            >>> client.delete_android_app_data_stream(name)

        Args:
            name (str): Required. The name of the android app data stream to delete. Format:
                properties/{property_id}/androidAppDataStreams/{stream_id} Example:
                "properties/123/androidAppDataStreams/456"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_android_app_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['delete_android_app_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_android_app_data_stream,
                default_retry=self._method_configs['DeleteAndroidAppDataStream'].retry,
                default_timeout=self._method_configs['DeleteAndroidAppDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.DeleteAndroidAppDataStreamRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['delete_android_app_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_android_app_data_stream(
            self,
            android_app_data_stream,
            update_mask=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates an android app stream on a property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `android_app_data_stream`:
            >>> android_app_data_stream = {}
            >>>
            >>> response = client.update_android_app_data_stream(android_app_data_stream)

        Args:
            android_app_data_stream (Union[dict, ~google.analytics.admin.v1alpha.types.AndroidAppDataStream]): Required. The android app stream to update. The ``name`` field is
                used to identify the android app stream to be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.AndroidAppDataStream`
            update_mask (Union[dict, ~google.analytics.admin.v1alpha.types.FieldMask]): The list of fields to be updated. Omitted fields will not be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.AndroidAppDataStream` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_android_app_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['update_android_app_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_android_app_data_stream,
                default_retry=self._method_configs['UpdateAndroidAppDataStream'].retry,
                default_timeout=self._method_configs['UpdateAndroidAppDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.UpdateAndroidAppDataStreamRequest(
            android_app_data_stream=android_app_data_stream,
            update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('android_app_data_stream.name', android_app_data_stream.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_android_app_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def create_android_app_data_stream(
            self,
            android_app_data_stream,
            parent,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates an android app stream with the specified location and attributes.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `android_app_data_stream`:
            >>> android_app_data_stream = {}
            >>> parent = client.property_path('[PROPERTY]')
            >>>
            >>> response = client.create_android_app_data_stream(android_app_data_stream, parent)

        Args:
            android_app_data_stream (Union[dict, ~google.analytics.admin.v1alpha.types.AndroidAppDataStream]): Required. The android app stream to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.AndroidAppDataStream`
            parent (str): Required. The parent resource where this android app data stream will be created.
                Format: properties/123
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.AndroidAppDataStream` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_android_app_data_stream' not in self._inner_api_calls:
            self._inner_api_calls['create_android_app_data_stream'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_android_app_data_stream,
                default_retry=self._method_configs['CreateAndroidAppDataStream'].retry,
                default_timeout=self._method_configs['CreateAndroidAppDataStream'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.CreateAndroidAppDataStreamRequest(
            android_app_data_stream=android_app_data_stream,
            parent=parent,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_android_app_data_stream'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_android_app_data_streams(
            self,
            parent,
            page_size=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Returns child android app streams under the specified parent property.

        Android app streams will be excluded if the caller does not have access.
        Returns an empty list if no relevant android app streams are found.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.property_path('[PROPERTY]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_android_app_data_streams(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_android_app_data_streams(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The name of the parent property.
                For example, to limit results to app streams under the property with Id
                123: "properties/123"
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.analytics.admin.v1alpha.types.AndroidAppDataStream` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_android_app_data_streams' not in self._inner_api_calls:
            self._inner_api_calls['list_android_app_data_streams'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_android_app_data_streams,
                default_retry=self._method_configs['ListAndroidAppDataStreams'].retry,
                default_timeout=self._method_configs['ListAndroidAppDataStreams'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.ListAndroidAppDataStreamsRequest(
            parent=parent,
            page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(self._inner_api_calls['list_android_app_data_streams'], retry=retry, timeout=timeout, metadata=metadata),
            request=request,
            items_field='android_app_data_streams',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator

    def get_enhanced_measurement_settings(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Returns the singleton enhanced measurement settings for this web stream.
        Note that the stream must enable enhanced measurement for these settings to
        take effect.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.enhanced_measurement_settings_path('[PROPERTY]', '[WEB_DATA_STREAM]')
            >>>
            >>> response = client.get_enhanced_measurement_settings(name)

        Args:
            name (str): Required. The name of the settings to lookup. Format:

                properties/{property_id}/webDataStreams/{stream_id}/enhancedMeasurementSettings
                Example:
                "properties/1000/webDataStreams/2000/enhancedMeasurementSettings"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.EnhancedMeasurementSettings` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_enhanced_measurement_settings' not in self._inner_api_calls:
            self._inner_api_calls['get_enhanced_measurement_settings'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_enhanced_measurement_settings,
                default_retry=self._method_configs['GetEnhancedMeasurementSettings'].retry,
                default_timeout=self._method_configs['GetEnhancedMeasurementSettings'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.GetEnhancedMeasurementSettingsRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_enhanced_measurement_settings'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_enhanced_measurement_settings(
            self,
            enhanced_measurement_settings,
            update_mask=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates the singleton enhanced measurement settings for this web stream.
        Note that the stream must enable enhanced measurement for these settings to
        take effect.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `enhanced_measurement_settings`:
            >>> enhanced_measurement_settings = {}
            >>>
            >>> response = client.update_enhanced_measurement_settings(enhanced_measurement_settings)

        Args:
            enhanced_measurement_settings (Union[dict, ~google.analytics.admin.v1alpha.types.EnhancedMeasurementSettings]): Required. The settings to update. The ``name`` field is used to
                identify the settings to be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.EnhancedMeasurementSettings`
            update_mask (Union[dict, ~google.analytics.admin.v1alpha.types.FieldMask]): The list of fields to be updated. Omitted fields will not be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.EnhancedMeasurementSettings` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_enhanced_measurement_settings' not in self._inner_api_calls:
            self._inner_api_calls['update_enhanced_measurement_settings'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_enhanced_measurement_settings,
                default_retry=self._method_configs['UpdateEnhancedMeasurementSettings'].retry,
                default_timeout=self._method_configs['UpdateEnhancedMeasurementSettings'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.UpdateEnhancedMeasurementSettingsRequest(
            enhanced_measurement_settings=enhanced_measurement_settings,
            update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('enhanced_measurement_settings.name', enhanced_measurement_settings.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_enhanced_measurement_settings'](request, retry=retry, timeout=timeout, metadata=metadata)

    def create_firebase_link(
            self,
            parent,
            firebase_link,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates a FirebaseLink.

        Properties can have at most one FirebaseLink.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.property_path('[PROPERTY]')
            >>>
            >>> # TODO: Initialize `firebase_link`:
            >>> firebase_link = {}
            >>>
            >>> response = client.create_firebase_link(parent, firebase_link)

        Args:
            parent (str): Required. Format: properties/{property_id} Example: properties/1234
            firebase_link (Union[dict, ~google.analytics.admin.v1alpha.types.FirebaseLink]): Required. The Firebase link to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.FirebaseLink`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.FirebaseLink` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_firebase_link' not in self._inner_api_calls:
            self._inner_api_calls['create_firebase_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_firebase_link,
                default_retry=self._method_configs['CreateFirebaseLink'].retry,
                default_timeout=self._method_configs['CreateFirebaseLink'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.CreateFirebaseLinkRequest(
            parent=parent,
            firebase_link=firebase_link,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_firebase_link'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_firebase_link(
            self,
            firebase_link,
            update_mask=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates a FirebaseLink on a property

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> # TODO: Initialize `firebase_link`:
            >>> firebase_link = {}
            >>>
            >>> response = client.update_firebase_link(firebase_link)

        Args:
            firebase_link (Union[dict, ~google.analytics.admin.v1alpha.types.FirebaseLink]): Required. The Firebase link to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.FirebaseLink`
            update_mask (Union[dict, ~google.analytics.admin.v1alpha.types.FieldMask]): The list of fields to be updated. Omitted fields will not be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.FirebaseLink` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_firebase_link' not in self._inner_api_calls:
            self._inner_api_calls['update_firebase_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_firebase_link,
                default_retry=self._method_configs['UpdateFirebaseLink'].retry,
                default_timeout=self._method_configs['UpdateFirebaseLink'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.UpdateFirebaseLinkRequest(
            firebase_link=firebase_link,
            update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('firebase_link.name', firebase_link.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_firebase_link'](request, retry=retry, timeout=timeout, metadata=metadata)

    def delete_firebase_link(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Deletes a FirebaseLink on a property

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.firebase_link_path('[PROPERTY]', '[FIREBASE_LINK]')
            >>>
            >>> client.delete_firebase_link(name)

        Args:
            name (str): Required. Format:
                properties/{property_id}/firebaseLinks/{firebase_link_id} Example:
                properties/1234/firebaseLinks/5678
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_firebase_link' not in self._inner_api_calls:
            self._inner_api_calls['delete_firebase_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_firebase_link,
                default_retry=self._method_configs['DeleteFirebaseLink'].retry,
                default_timeout=self._method_configs['DeleteFirebaseLink'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.DeleteFirebaseLinkRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['delete_firebase_link'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_firebase_links(
            self,
            parent,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Lists FirebaseLinks on a property.
        Properties can have at most one FirebaseLink.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.property_path('[PROPERTY]')
            >>>
            >>> response = client.list_firebase_links(parent)

        Args:
            parent (str): Required. Format: properties/{property_id} Example: properties/1234
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.ListFirebaseLinksResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_firebase_links' not in self._inner_api_calls:
            self._inner_api_calls['list_firebase_links'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_firebase_links,
                default_retry=self._method_configs['ListFirebaseLinks'].retry,
                default_timeout=self._method_configs['ListFirebaseLinks'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.ListFirebaseLinksRequest(
            parent=parent,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['list_firebase_links'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_global_site_tag(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Returns the Site Tag for the specified web stream.
        Site Tags are immutable singletons.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.global_site_tag_path('[PROPERTY]')
            >>>
            >>> response = client.get_global_site_tag(name)

        Args:
            name (str): Required. The name of the site tag to lookup. Note that site tags
                are singletons and do not have unique IDs. Format:
                properties/{property_id}/webDataStreams/{stream_id}/globalSiteTag
                Example: "properties/123/webDataStreams/456/globalSiteTag"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.GlobalSiteTag` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_global_site_tag' not in self._inner_api_calls:
            self._inner_api_calls['get_global_site_tag'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_global_site_tag,
                default_retry=self._method_configs['GetGlobalSiteTag'].retry,
                default_timeout=self._method_configs['GetGlobalSiteTag'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.GetGlobalSiteTagRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_global_site_tag'](request, retry=retry, timeout=timeout, metadata=metadata)

    def create_google_ads_link(
            self,
            parent,
            google_ads_link,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates a GoogleAdsLink.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.property_path('[PROPERTY]')
            >>>
            >>> # TODO: Initialize `google_ads_link`:
            >>> google_ads_link = {}
            >>>
            >>> response = client.create_google_ads_link(parent, google_ads_link)

        Args:
            parent (str): Required. Example format: properties/1234
            google_ads_link (Union[dict, ~google.analytics.admin.v1alpha.types.GoogleAdsLink]): Required. The GoogleAdsLink to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.GoogleAdsLink`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.GoogleAdsLink` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_google_ads_link' not in self._inner_api_calls:
            self._inner_api_calls['create_google_ads_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_google_ads_link,
                default_retry=self._method_configs['CreateGoogleAdsLink'].retry,
                default_timeout=self._method_configs['CreateGoogleAdsLink'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.CreateGoogleAdsLinkRequest(
            parent=parent,
            google_ads_link=google_ads_link,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_google_ads_link'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_google_ads_link(
            self,
            google_ads_link=None,
            update_mask=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates a GoogleAdsLink on a property

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> response = client.update_google_ads_link()

        Args:
            google_ads_link (Union[dict, ~google.analytics.admin.v1alpha.types.GoogleAdsLink]): The GoogleAdsLink to update

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.GoogleAdsLink`
            update_mask (Union[dict, ~google.analytics.admin.v1alpha.types.FieldMask]): The list of fields to be updated. Omitted fields will not be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.analytics.admin.v1alpha.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.GoogleAdsLink` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_google_ads_link' not in self._inner_api_calls:
            self._inner_api_calls['update_google_ads_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_google_ads_link,
                default_retry=self._method_configs['UpdateGoogleAdsLink'].retry,
                default_timeout=self._method_configs['UpdateGoogleAdsLink'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.UpdateGoogleAdsLinkRequest(
            google_ads_link=google_ads_link,
            update_mask=update_mask,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('google_ads_link.name', google_ads_link.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_google_ads_link'](request, retry=retry, timeout=timeout, metadata=metadata)

    def delete_google_ads_link(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Deletes a GoogleAdsLink on a property

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.google_ads_link_path('[PROPERTY]', '[GOOGLE_ADS_LINK]')
            >>>
            >>> client.delete_google_ads_link(name)

        Args:
            name (str): Required. Example format: properties/1234/googleAdsLinks/5678
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_google_ads_link' not in self._inner_api_calls:
            self._inner_api_calls['delete_google_ads_link'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_google_ads_link,
                default_retry=self._method_configs['DeleteGoogleAdsLink'].retry,
                default_timeout=self._method_configs['DeleteGoogleAdsLink'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.DeleteGoogleAdsLinkRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['delete_google_ads_link'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_google_ads_links(
            self,
            parent,
            page_size=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Lists GoogleAdsLinks on a property.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> parent = client.property_path('[PROPERTY]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_google_ads_links(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_google_ads_links(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. Example format: properties/1234
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.analytics.admin.v1alpha.types.GoogleAdsLink` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_google_ads_links' not in self._inner_api_calls:
            self._inner_api_calls['list_google_ads_links'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_google_ads_links,
                default_retry=self._method_configs['ListGoogleAdsLinks'].retry,
                default_timeout=self._method_configs['ListGoogleAdsLinks'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.ListGoogleAdsLinksRequest(
            parent=parent,
            page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(self._inner_api_calls['list_google_ads_links'], retry=retry, timeout=timeout, metadata=metadata),
            request=request,
            items_field='google_ads_links',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator

    def get_data_sharing_settings(
            self,
            name,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Get data sharing settings on an account.
        Data sharing settings are singletons.

        Example:
            >>> from google.analytics.admin import v1alpha
            >>>
            >>> client = v1alpha.AnalyticsAdminServiceClient()
            >>>
            >>> name = client.data_sharing_settings_path('[ACCOUNT]')
            >>>
            >>> response = client.get_data_sharing_settings(name)

        Args:
            name (str): Required. The name of the settings to lookup.
                Format: accounts/{account}/dataSharingSettings
                Example: "accounts/1000/dataSharingSettings"
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.analytics.admin.v1alpha.types.DataSharingSettings` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_data_sharing_settings' not in self._inner_api_calls:
            self._inner_api_calls['get_data_sharing_settings'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_data_sharing_settings,
                default_retry=self._method_configs['GetDataSharingSettings'].retry,
                default_timeout=self._method_configs['GetDataSharingSettings'].timeout,
                client_info=self._client_info,
            )

        request = analytics_admin_pb2.GetDataSharingSettingsRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_data_sharing_settings'](request, retry=retry, timeout=timeout, metadata=metadata)
