# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.analytics.admin_v1alpha.types import analytics_admin
from google.analytics.admin_v1alpha.types import resources
from google.protobuf import empty_pb2 as empty  # type: ignore

from .base import AnalyticsAdminServiceTransport, DEFAULT_CLIENT_INFO


class AnalyticsAdminServiceGrpcTransport(AnalyticsAdminServiceTransport):
    """gRPC backend transport for AnalyticsAdminService.

    Service Interface for the Analytics Admin API (GA4).

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "analyticsadmin.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._ssl_channel_credentials = ssl_channel_credentials

        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        elif api_mtls_endpoint:
            warnings.warn(
                "api_mtls_endpoint and client_cert_source are deprecated",
                DeprecationWarning,
            )

            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            self._ssl_channel_credentials = ssl_credentials
        else:
            host = host if ":" in host else host + ":443"

            if credentials is None:
                credentials, _ = auth.default(
                    scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id
                )

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_channel_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        self._stubs = {}  # type: Dict[str, Callable]

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

    @classmethod
    def create_channel(
        cls,
        host: str = "analyticsadmin.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def get_account(
        self,
    ) -> Callable[[analytics_admin.GetAccountRequest], resources.Account]:
        r"""Return a callable for the get account method over gRPC.

        Lookup for a single Account.

        Returns:
            Callable[[~.GetAccountRequest],
                    ~.Account]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_account" not in self._stubs:
            self._stubs["get_account"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/GetAccount",
                request_serializer=analytics_admin.GetAccountRequest.serialize,
                response_deserializer=resources.Account.deserialize,
            )
        return self._stubs["get_account"]

    @property
    def list_accounts(
        self,
    ) -> Callable[
        [analytics_admin.ListAccountsRequest], analytics_admin.ListAccountsResponse
    ]:
        r"""Return a callable for the list accounts method over gRPC.

        Returns all accounts accessible by the caller.
        Note that these accounts might not currently have GA4
        properties. Soft-deleted (ie: "trashed") accounts are
        excluded by default. Returns an empty list if no
        relevant accounts are found.

        Returns:
            Callable[[~.ListAccountsRequest],
                    ~.ListAccountsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_accounts" not in self._stubs:
            self._stubs["list_accounts"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/ListAccounts",
                request_serializer=analytics_admin.ListAccountsRequest.serialize,
                response_deserializer=analytics_admin.ListAccountsResponse.deserialize,
            )
        return self._stubs["list_accounts"]

    @property
    def delete_account(
        self,
    ) -> Callable[[analytics_admin.DeleteAccountRequest], empty.Empty]:
        r"""Return a callable for the delete account method over gRPC.

        Marks target Account as soft-deleted (ie: "trashed")
        and returns it.
        This API does not have a method to restore soft-deleted
        accounts. However, they can be restored using the Trash
        Can UI.
        If the accounts are not restored before the expiration
        time, the account and all child resources (eg:
        Properties, GoogleAdsLinks, Streams, UserLinks) will be
        permanently purged.
        https://support.google.com/analytics/answer/6154772
        Returns an error if the target is not found.

        Returns:
            Callable[[~.DeleteAccountRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_account" not in self._stubs:
            self._stubs["delete_account"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/DeleteAccount",
                request_serializer=analytics_admin.DeleteAccountRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_account"]

    @property
    def update_account(
        self,
    ) -> Callable[[analytics_admin.UpdateAccountRequest], resources.Account]:
        r"""Return a callable for the update account method over gRPC.

        Updates an account.

        Returns:
            Callable[[~.UpdateAccountRequest],
                    ~.Account]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_account" not in self._stubs:
            self._stubs["update_account"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/UpdateAccount",
                request_serializer=analytics_admin.UpdateAccountRequest.serialize,
                response_deserializer=resources.Account.deserialize,
            )
        return self._stubs["update_account"]

    @property
    def provision_account_ticket(
        self,
    ) -> Callable[
        [analytics_admin.ProvisionAccountTicketRequest],
        analytics_admin.ProvisionAccountTicketResponse,
    ]:
        r"""Return a callable for the provision account ticket method over gRPC.

        Requests a ticket for creating an account.

        Returns:
            Callable[[~.ProvisionAccountTicketRequest],
                    ~.ProvisionAccountTicketResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "provision_account_ticket" not in self._stubs:
            self._stubs["provision_account_ticket"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/ProvisionAccountTicket",
                request_serializer=analytics_admin.ProvisionAccountTicketRequest.serialize,
                response_deserializer=analytics_admin.ProvisionAccountTicketResponse.deserialize,
            )
        return self._stubs["provision_account_ticket"]

    @property
    def list_account_summaries(
        self,
    ) -> Callable[
        [analytics_admin.ListAccountSummariesRequest],
        analytics_admin.ListAccountSummariesResponse,
    ]:
        r"""Return a callable for the list account summaries method over gRPC.

        Returns summaries of all accounts accessible by the
        caller.

        Returns:
            Callable[[~.ListAccountSummariesRequest],
                    ~.ListAccountSummariesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_account_summaries" not in self._stubs:
            self._stubs["list_account_summaries"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/ListAccountSummaries",
                request_serializer=analytics_admin.ListAccountSummariesRequest.serialize,
                response_deserializer=analytics_admin.ListAccountSummariesResponse.deserialize,
            )
        return self._stubs["list_account_summaries"]

    @property
    def get_property(
        self,
    ) -> Callable[[analytics_admin.GetPropertyRequest], resources.Property]:
        r"""Return a callable for the get property method over gRPC.

        Lookup for a single "GA4" Property.

        Returns:
            Callable[[~.GetPropertyRequest],
                    ~.Property]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_property" not in self._stubs:
            self._stubs["get_property"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/GetProperty",
                request_serializer=analytics_admin.GetPropertyRequest.serialize,
                response_deserializer=resources.Property.deserialize,
            )
        return self._stubs["get_property"]

    @property
    def list_properties(
        self,
    ) -> Callable[
        [analytics_admin.ListPropertiesRequest], analytics_admin.ListPropertiesResponse
    ]:
        r"""Return a callable for the list properties method over gRPC.

        Returns child Properties under the specified parent
        Account.
        Only "GA4" properties will be returned.
        Properties will be excluded if the caller does not have
        access. Soft-deleted (ie: "trashed") properties are
        excluded by default. Returns an empty list if no
        relevant properties are found.

        Returns:
            Callable[[~.ListPropertiesRequest],
                    ~.ListPropertiesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_properties" not in self._stubs:
            self._stubs["list_properties"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/ListProperties",
                request_serializer=analytics_admin.ListPropertiesRequest.serialize,
                response_deserializer=analytics_admin.ListPropertiesResponse.deserialize,
            )
        return self._stubs["list_properties"]

    @property
    def create_property(
        self,
    ) -> Callable[[analytics_admin.CreatePropertyRequest], resources.Property]:
        r"""Return a callable for the create property method over gRPC.

        Creates an "GA4" property with the specified location
        and attributes.

        Returns:
            Callable[[~.CreatePropertyRequest],
                    ~.Property]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_property" not in self._stubs:
            self._stubs["create_property"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/CreateProperty",
                request_serializer=analytics_admin.CreatePropertyRequest.serialize,
                response_deserializer=resources.Property.deserialize,
            )
        return self._stubs["create_property"]

    @property
    def delete_property(
        self,
    ) -> Callable[[analytics_admin.DeletePropertyRequest], empty.Empty]:
        r"""Return a callable for the delete property method over gRPC.

        Marks target Property as soft-deleted (ie: "trashed")
        and returns it.
        This API does not have a method to restore soft-deleted
        properties. However, they can be restored using the
        Trash Can UI.
        If the properties are not restored before the expiration
        time, the Property and all child resources (eg:
        GoogleAdsLinks, Streams, UserLinks) will be permanently
        purged.
        https://support.google.com/analytics/answer/6154772
        Returns an error if the target is not found, or is not
        an GA4 Property.

        Returns:
            Callable[[~.DeletePropertyRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_property" not in self._stubs:
            self._stubs["delete_property"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/DeleteProperty",
                request_serializer=analytics_admin.DeletePropertyRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_property"]

    @property
    def update_property(
        self,
    ) -> Callable[[analytics_admin.UpdatePropertyRequest], resources.Property]:
        r"""Return a callable for the update property method over gRPC.

        Updates a property.

        Returns:
            Callable[[~.UpdatePropertyRequest],
                    ~.Property]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_property" not in self._stubs:
            self._stubs["update_property"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/UpdateProperty",
                request_serializer=analytics_admin.UpdatePropertyRequest.serialize,
                response_deserializer=resources.Property.deserialize,
            )
        return self._stubs["update_property"]

    @property
    def get_user_link(
        self,
    ) -> Callable[[analytics_admin.GetUserLinkRequest], resources.UserLink]:
        r"""Return a callable for the get user link method over gRPC.

        Gets information about a user's link to an account or
        property.

        Returns:
            Callable[[~.GetUserLinkRequest],
                    ~.UserLink]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_user_link" not in self._stubs:
            self._stubs["get_user_link"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/GetUserLink",
                request_serializer=analytics_admin.GetUserLinkRequest.serialize,
                response_deserializer=resources.UserLink.deserialize,
            )
        return self._stubs["get_user_link"]

    @property
    def batch_get_user_links(
        self,
    ) -> Callable[
        [analytics_admin.BatchGetUserLinksRequest],
        analytics_admin.BatchGetUserLinksResponse,
    ]:
        r"""Return a callable for the batch get user links method over gRPC.

        Gets information about multiple users' links to an
        account or property.

        Returns:
            Callable[[~.BatchGetUserLinksRequest],
                    ~.BatchGetUserLinksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_get_user_links" not in self._stubs:
            self._stubs["batch_get_user_links"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/BatchGetUserLinks",
                request_serializer=analytics_admin.BatchGetUserLinksRequest.serialize,
                response_deserializer=analytics_admin.BatchGetUserLinksResponse.deserialize,
            )
        return self._stubs["batch_get_user_links"]

    @property
    def list_user_links(
        self,
    ) -> Callable[
        [analytics_admin.ListUserLinksRequest], analytics_admin.ListUserLinksResponse
    ]:
        r"""Return a callable for the list user links method over gRPC.

        Lists all user links on an account or property.

        Returns:
            Callable[[~.ListUserLinksRequest],
                    ~.ListUserLinksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_user_links" not in self._stubs:
            self._stubs["list_user_links"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/ListUserLinks",
                request_serializer=analytics_admin.ListUserLinksRequest.serialize,
                response_deserializer=analytics_admin.ListUserLinksResponse.deserialize,
            )
        return self._stubs["list_user_links"]

    @property
    def audit_user_links(
        self,
    ) -> Callable[
        [analytics_admin.AuditUserLinksRequest], analytics_admin.AuditUserLinksResponse
    ]:
        r"""Return a callable for the audit user links method over gRPC.

        Lists all user links on an account or property,
        including implicit ones that come from effective
        permissions granted by groups or organization admin
        roles.

        If a returned user link does not have direct
        permissions, they cannot be removed from the account or
        property directly with the DeleteUserLink command. They
        have to be removed from the group/etc that gives them
        permissions, which is currently only usable/discoverable
        in the GA or GMP UIs.

        Returns:
            Callable[[~.AuditUserLinksRequest],
                    ~.AuditUserLinksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "audit_user_links" not in self._stubs:
            self._stubs["audit_user_links"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/AuditUserLinks",
                request_serializer=analytics_admin.AuditUserLinksRequest.serialize,
                response_deserializer=analytics_admin.AuditUserLinksResponse.deserialize,
            )
        return self._stubs["audit_user_links"]

    @property
    def create_user_link(
        self,
    ) -> Callable[[analytics_admin.CreateUserLinkRequest], resources.UserLink]:
        r"""Return a callable for the create user link method over gRPC.

        Creates a user link on an account or property.
        If the user with the specified email already has
        permissions on the account or property, then the user's
        existing permissions will be unioned with the
        permissions specified in the new UserLink.

        Returns:
            Callable[[~.CreateUserLinkRequest],
                    ~.UserLink]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_user_link" not in self._stubs:
            self._stubs["create_user_link"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/CreateUserLink",
                request_serializer=analytics_admin.CreateUserLinkRequest.serialize,
                response_deserializer=resources.UserLink.deserialize,
            )
        return self._stubs["create_user_link"]

    @property
    def batch_create_user_links(
        self,
    ) -> Callable[
        [analytics_admin.BatchCreateUserLinksRequest],
        analytics_admin.BatchCreateUserLinksResponse,
    ]:
        r"""Return a callable for the batch create user links method over gRPC.

        Creates information about multiple users' links to an
        account or property.
        This method is transactional. If any UserLink cannot be
        created, none of the UserLinks will be created.

        Returns:
            Callable[[~.BatchCreateUserLinksRequest],
                    ~.BatchCreateUserLinksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_create_user_links" not in self._stubs:
            self._stubs["batch_create_user_links"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/BatchCreateUserLinks",
                request_serializer=analytics_admin.BatchCreateUserLinksRequest.serialize,
                response_deserializer=analytics_admin.BatchCreateUserLinksResponse.deserialize,
            )
        return self._stubs["batch_create_user_links"]

    @property
    def update_user_link(
        self,
    ) -> Callable[[analytics_admin.UpdateUserLinkRequest], resources.UserLink]:
        r"""Return a callable for the update user link method over gRPC.

        Updates a user link on an account or property.

        Returns:
            Callable[[~.UpdateUserLinkRequest],
                    ~.UserLink]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_user_link" not in self._stubs:
            self._stubs["update_user_link"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/UpdateUserLink",
                request_serializer=analytics_admin.UpdateUserLinkRequest.serialize,
                response_deserializer=resources.UserLink.deserialize,
            )
        return self._stubs["update_user_link"]

    @property
    def batch_update_user_links(
        self,
    ) -> Callable[
        [analytics_admin.BatchUpdateUserLinksRequest],
        analytics_admin.BatchUpdateUserLinksResponse,
    ]:
        r"""Return a callable for the batch update user links method over gRPC.

        Updates information about multiple users' links to an
        account or property.

        Returns:
            Callable[[~.BatchUpdateUserLinksRequest],
                    ~.BatchUpdateUserLinksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_update_user_links" not in self._stubs:
            self._stubs["batch_update_user_links"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/BatchUpdateUserLinks",
                request_serializer=analytics_admin.BatchUpdateUserLinksRequest.serialize,
                response_deserializer=analytics_admin.BatchUpdateUserLinksResponse.deserialize,
            )
        return self._stubs["batch_update_user_links"]

    @property
    def delete_user_link(
        self,
    ) -> Callable[[analytics_admin.DeleteUserLinkRequest], empty.Empty]:
        r"""Return a callable for the delete user link method over gRPC.

        Deletes a user link on an account or property.

        Returns:
            Callable[[~.DeleteUserLinkRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_user_link" not in self._stubs:
            self._stubs["delete_user_link"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/DeleteUserLink",
                request_serializer=analytics_admin.DeleteUserLinkRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_user_link"]

    @property
    def batch_delete_user_links(
        self,
    ) -> Callable[[analytics_admin.BatchDeleteUserLinksRequest], empty.Empty]:
        r"""Return a callable for the batch delete user links method over gRPC.

        Deletes information about multiple users' links to an
        account or property.

        Returns:
            Callable[[~.BatchDeleteUserLinksRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_delete_user_links" not in self._stubs:
            self._stubs["batch_delete_user_links"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/BatchDeleteUserLinks",
                request_serializer=analytics_admin.BatchDeleteUserLinksRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["batch_delete_user_links"]

    @property
    def get_web_data_stream(
        self,
    ) -> Callable[[analytics_admin.GetWebDataStreamRequest], resources.WebDataStream]:
        r"""Return a callable for the get web data stream method over gRPC.

        Lookup for a single WebDataStream

        Returns:
            Callable[[~.GetWebDataStreamRequest],
                    ~.WebDataStream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_web_data_stream" not in self._stubs:
            self._stubs["get_web_data_stream"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/GetWebDataStream",
                request_serializer=analytics_admin.GetWebDataStreamRequest.serialize,
                response_deserializer=resources.WebDataStream.deserialize,
            )
        return self._stubs["get_web_data_stream"]

    @property
    def delete_web_data_stream(
        self,
    ) -> Callable[[analytics_admin.DeleteWebDataStreamRequest], empty.Empty]:
        r"""Return a callable for the delete web data stream method over gRPC.

        Deletes a web stream on a property.

        Returns:
            Callable[[~.DeleteWebDataStreamRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_web_data_stream" not in self._stubs:
            self._stubs["delete_web_data_stream"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/DeleteWebDataStream",
                request_serializer=analytics_admin.DeleteWebDataStreamRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_web_data_stream"]

    @property
    def update_web_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.UpdateWebDataStreamRequest], resources.WebDataStream
    ]:
        r"""Return a callable for the update web data stream method over gRPC.

        Updates a web stream on a property.

        Returns:
            Callable[[~.UpdateWebDataStreamRequest],
                    ~.WebDataStream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_web_data_stream" not in self._stubs:
            self._stubs["update_web_data_stream"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/UpdateWebDataStream",
                request_serializer=analytics_admin.UpdateWebDataStreamRequest.serialize,
                response_deserializer=resources.WebDataStream.deserialize,
            )
        return self._stubs["update_web_data_stream"]

    @property
    def create_web_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.CreateWebDataStreamRequest], resources.WebDataStream
    ]:
        r"""Return a callable for the create web data stream method over gRPC.

        Creates a web stream with the specified location and
        attributes.

        Returns:
            Callable[[~.CreateWebDataStreamRequest],
                    ~.WebDataStream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_web_data_stream" not in self._stubs:
            self._stubs["create_web_data_stream"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/CreateWebDataStream",
                request_serializer=analytics_admin.CreateWebDataStreamRequest.serialize,
                response_deserializer=resources.WebDataStream.deserialize,
            )
        return self._stubs["create_web_data_stream"]

    @property
    def list_web_data_streams(
        self,
    ) -> Callable[
        [analytics_admin.ListWebDataStreamsRequest],
        analytics_admin.ListWebDataStreamsResponse,
    ]:
        r"""Return a callable for the list web data streams method over gRPC.

        Returns child web data streams under the specified
        parent property.
        Web data streams will be excluded if the caller does not
        have access. Returns an empty list if no relevant web
        data streams are found.

        Returns:
            Callable[[~.ListWebDataStreamsRequest],
                    ~.ListWebDataStreamsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_web_data_streams" not in self._stubs:
            self._stubs["list_web_data_streams"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/ListWebDataStreams",
                request_serializer=analytics_admin.ListWebDataStreamsRequest.serialize,
                response_deserializer=analytics_admin.ListWebDataStreamsResponse.deserialize,
            )
        return self._stubs["list_web_data_streams"]

    @property
    def get_ios_app_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.GetIosAppDataStreamRequest], resources.IosAppDataStream
    ]:
        r"""Return a callable for the get ios app data stream method over gRPC.

        Lookup for a single IosAppDataStream

        Returns:
            Callable[[~.GetIosAppDataStreamRequest],
                    ~.IosAppDataStream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_ios_app_data_stream" not in self._stubs:
            self._stubs["get_ios_app_data_stream"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/GetIosAppDataStream",
                request_serializer=analytics_admin.GetIosAppDataStreamRequest.serialize,
                response_deserializer=resources.IosAppDataStream.deserialize,
            )
        return self._stubs["get_ios_app_data_stream"]

    @property
    def delete_ios_app_data_stream(
        self,
    ) -> Callable[[analytics_admin.DeleteIosAppDataStreamRequest], empty.Empty]:
        r"""Return a callable for the delete ios app data stream method over gRPC.

        Deletes an iOS app stream on a property.

        Returns:
            Callable[[~.DeleteIosAppDataStreamRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_ios_app_data_stream" not in self._stubs:
            self._stubs["delete_ios_app_data_stream"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/DeleteIosAppDataStream",
                request_serializer=analytics_admin.DeleteIosAppDataStreamRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_ios_app_data_stream"]

    @property
    def update_ios_app_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.UpdateIosAppDataStreamRequest], resources.IosAppDataStream
    ]:
        r"""Return a callable for the update ios app data stream method over gRPC.

        Updates an iOS app stream on a property.

        Returns:
            Callable[[~.UpdateIosAppDataStreamRequest],
                    ~.IosAppDataStream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_ios_app_data_stream" not in self._stubs:
            self._stubs["update_ios_app_data_stream"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/UpdateIosAppDataStream",
                request_serializer=analytics_admin.UpdateIosAppDataStreamRequest.serialize,
                response_deserializer=resources.IosAppDataStream.deserialize,
            )
        return self._stubs["update_ios_app_data_stream"]

    @property
    def create_ios_app_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.CreateIosAppDataStreamRequest], resources.IosAppDataStream
    ]:
        r"""Return a callable for the create ios app data stream method over gRPC.

        Creates an iOS app data stream with the specified
        location and attributes.

        Returns:
            Callable[[~.CreateIosAppDataStreamRequest],
                    ~.IosAppDataStream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_ios_app_data_stream" not in self._stubs:
            self._stubs["create_ios_app_data_stream"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/CreateIosAppDataStream",
                request_serializer=analytics_admin.CreateIosAppDataStreamRequest.serialize,
                response_deserializer=resources.IosAppDataStream.deserialize,
            )
        return self._stubs["create_ios_app_data_stream"]

    @property
    def list_ios_app_data_streams(
        self,
    ) -> Callable[
        [analytics_admin.ListIosAppDataStreamsRequest],
        analytics_admin.ListIosAppDataStreamsResponse,
    ]:
        r"""Return a callable for the list ios app data streams method over gRPC.

        Returns child iOS app data streams under the
        specified parent property.
        iOS app data streams will be excluded if the caller does
        not have access. Returns an empty list if no relevant
        iOS app data streams are found.

        Returns:
            Callable[[~.ListIosAppDataStreamsRequest],
                    ~.ListIosAppDataStreamsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_ios_app_data_streams" not in self._stubs:
            self._stubs["list_ios_app_data_streams"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/ListIosAppDataStreams",
                request_serializer=analytics_admin.ListIosAppDataStreamsRequest.serialize,
                response_deserializer=analytics_admin.ListIosAppDataStreamsResponse.deserialize,
            )
        return self._stubs["list_ios_app_data_streams"]

    @property
    def get_android_app_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.GetAndroidAppDataStreamRequest], resources.AndroidAppDataStream
    ]:
        r"""Return a callable for the get android app data stream method over gRPC.

        Lookup for a single AndroidAppDataStream

        Returns:
            Callable[[~.GetAndroidAppDataStreamRequest],
                    ~.AndroidAppDataStream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_android_app_data_stream" not in self._stubs:
            self._stubs["get_android_app_data_stream"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/GetAndroidAppDataStream",
                request_serializer=analytics_admin.GetAndroidAppDataStreamRequest.serialize,
                response_deserializer=resources.AndroidAppDataStream.deserialize,
            )
        return self._stubs["get_android_app_data_stream"]

    @property
    def delete_android_app_data_stream(
        self,
    ) -> Callable[[analytics_admin.DeleteAndroidAppDataStreamRequest], empty.Empty]:
        r"""Return a callable for the delete android app data stream method over gRPC.

        Deletes an android app stream on a property.

        Returns:
            Callable[[~.DeleteAndroidAppDataStreamRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_android_app_data_stream" not in self._stubs:
            self._stubs[
                "delete_android_app_data_stream"
            ] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/DeleteAndroidAppDataStream",
                request_serializer=analytics_admin.DeleteAndroidAppDataStreamRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_android_app_data_stream"]

    @property
    def update_android_app_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.UpdateAndroidAppDataStreamRequest],
        resources.AndroidAppDataStream,
    ]:
        r"""Return a callable for the update android app data stream method over gRPC.

        Updates an android app stream on a property.

        Returns:
            Callable[[~.UpdateAndroidAppDataStreamRequest],
                    ~.AndroidAppDataStream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_android_app_data_stream" not in self._stubs:
            self._stubs[
                "update_android_app_data_stream"
            ] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/UpdateAndroidAppDataStream",
                request_serializer=analytics_admin.UpdateAndroidAppDataStreamRequest.serialize,
                response_deserializer=resources.AndroidAppDataStream.deserialize,
            )
        return self._stubs["update_android_app_data_stream"]

    @property
    def create_android_app_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.CreateAndroidAppDataStreamRequest],
        resources.AndroidAppDataStream,
    ]:
        r"""Return a callable for the create android app data stream method over gRPC.

        Creates an android app stream with the specified
        location and attributes.

        Returns:
            Callable[[~.CreateAndroidAppDataStreamRequest],
                    ~.AndroidAppDataStream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_android_app_data_stream" not in self._stubs:
            self._stubs[
                "create_android_app_data_stream"
            ] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/CreateAndroidAppDataStream",
                request_serializer=analytics_admin.CreateAndroidAppDataStreamRequest.serialize,
                response_deserializer=resources.AndroidAppDataStream.deserialize,
            )
        return self._stubs["create_android_app_data_stream"]

    @property
    def list_android_app_data_streams(
        self,
    ) -> Callable[
        [analytics_admin.ListAndroidAppDataStreamsRequest],
        analytics_admin.ListAndroidAppDataStreamsResponse,
    ]:
        r"""Return a callable for the list android app data streams method over gRPC.

        Returns child android app streams under the specified
        parent property.
        Android app streams will be excluded if the caller does
        not have access. Returns an empty list if no relevant
        android app streams are found.

        Returns:
            Callable[[~.ListAndroidAppDataStreamsRequest],
                    ~.ListAndroidAppDataStreamsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_android_app_data_streams" not in self._stubs:
            self._stubs[
                "list_android_app_data_streams"
            ] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/ListAndroidAppDataStreams",
                request_serializer=analytics_admin.ListAndroidAppDataStreamsRequest.serialize,
                response_deserializer=analytics_admin.ListAndroidAppDataStreamsResponse.deserialize,
            )
        return self._stubs["list_android_app_data_streams"]

    @property
    def get_enhanced_measurement_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetEnhancedMeasurementSettingsRequest],
        resources.EnhancedMeasurementSettings,
    ]:
        r"""Return a callable for the get enhanced measurement
        settings method over gRPC.

        Returns the singleton enhanced measurement settings
        for this web stream. Note that the stream must enable
        enhanced measurement for these settings to take effect.

        Returns:
            Callable[[~.GetEnhancedMeasurementSettingsRequest],
                    ~.EnhancedMeasurementSettings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_enhanced_measurement_settings" not in self._stubs:
            self._stubs[
                "get_enhanced_measurement_settings"
            ] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/GetEnhancedMeasurementSettings",
                request_serializer=analytics_admin.GetEnhancedMeasurementSettingsRequest.serialize,
                response_deserializer=resources.EnhancedMeasurementSettings.deserialize,
            )
        return self._stubs["get_enhanced_measurement_settings"]

    @property
    def update_enhanced_measurement_settings(
        self,
    ) -> Callable[
        [analytics_admin.UpdateEnhancedMeasurementSettingsRequest],
        resources.EnhancedMeasurementSettings,
    ]:
        r"""Return a callable for the update enhanced measurement
        settings method over gRPC.

        Updates the singleton enhanced measurement settings
        for this web stream. Note that the stream must enable
        enhanced measurement for these settings to take effect.

        Returns:
            Callable[[~.UpdateEnhancedMeasurementSettingsRequest],
                    ~.EnhancedMeasurementSettings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_enhanced_measurement_settings" not in self._stubs:
            self._stubs[
                "update_enhanced_measurement_settings"
            ] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/UpdateEnhancedMeasurementSettings",
                request_serializer=analytics_admin.UpdateEnhancedMeasurementSettingsRequest.serialize,
                response_deserializer=resources.EnhancedMeasurementSettings.deserialize,
            )
        return self._stubs["update_enhanced_measurement_settings"]

    @property
    def create_firebase_link(
        self,
    ) -> Callable[[analytics_admin.CreateFirebaseLinkRequest], resources.FirebaseLink]:
        r"""Return a callable for the create firebase link method over gRPC.

        Creates a FirebaseLink.
        Properties can have at most one FirebaseLink.

        Returns:
            Callable[[~.CreateFirebaseLinkRequest],
                    ~.FirebaseLink]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_firebase_link" not in self._stubs:
            self._stubs["create_firebase_link"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/CreateFirebaseLink",
                request_serializer=analytics_admin.CreateFirebaseLinkRequest.serialize,
                response_deserializer=resources.FirebaseLink.deserialize,
            )
        return self._stubs["create_firebase_link"]

    @property
    def update_firebase_link(
        self,
    ) -> Callable[[analytics_admin.UpdateFirebaseLinkRequest], resources.FirebaseLink]:
        r"""Return a callable for the update firebase link method over gRPC.

        Updates a FirebaseLink on a property

        Returns:
            Callable[[~.UpdateFirebaseLinkRequest],
                    ~.FirebaseLink]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_firebase_link" not in self._stubs:
            self._stubs["update_firebase_link"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/UpdateFirebaseLink",
                request_serializer=analytics_admin.UpdateFirebaseLinkRequest.serialize,
                response_deserializer=resources.FirebaseLink.deserialize,
            )
        return self._stubs["update_firebase_link"]

    @property
    def delete_firebase_link(
        self,
    ) -> Callable[[analytics_admin.DeleteFirebaseLinkRequest], empty.Empty]:
        r"""Return a callable for the delete firebase link method over gRPC.

        Deletes a FirebaseLink on a property

        Returns:
            Callable[[~.DeleteFirebaseLinkRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_firebase_link" not in self._stubs:
            self._stubs["delete_firebase_link"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/DeleteFirebaseLink",
                request_serializer=analytics_admin.DeleteFirebaseLinkRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_firebase_link"]

    @property
    def list_firebase_links(
        self,
    ) -> Callable[
        [analytics_admin.ListFirebaseLinksRequest],
        analytics_admin.ListFirebaseLinksResponse,
    ]:
        r"""Return a callable for the list firebase links method over gRPC.

        Lists FirebaseLinks on a property.
        Properties can have at most one FirebaseLink.

        Returns:
            Callable[[~.ListFirebaseLinksRequest],
                    ~.ListFirebaseLinksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_firebase_links" not in self._stubs:
            self._stubs["list_firebase_links"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/ListFirebaseLinks",
                request_serializer=analytics_admin.ListFirebaseLinksRequest.serialize,
                response_deserializer=analytics_admin.ListFirebaseLinksResponse.deserialize,
            )
        return self._stubs["list_firebase_links"]

    @property
    def get_global_site_tag(
        self,
    ) -> Callable[[analytics_admin.GetGlobalSiteTagRequest], resources.GlobalSiteTag]:
        r"""Return a callable for the get global site tag method over gRPC.

        Returns the Site Tag for the specified web stream.
        Site Tags are immutable singletons.

        Returns:
            Callable[[~.GetGlobalSiteTagRequest],
                    ~.GlobalSiteTag]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_global_site_tag" not in self._stubs:
            self._stubs["get_global_site_tag"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/GetGlobalSiteTag",
                request_serializer=analytics_admin.GetGlobalSiteTagRequest.serialize,
                response_deserializer=resources.GlobalSiteTag.deserialize,
            )
        return self._stubs["get_global_site_tag"]

    @property
    def create_google_ads_link(
        self,
    ) -> Callable[
        [analytics_admin.CreateGoogleAdsLinkRequest], resources.GoogleAdsLink
    ]:
        r"""Return a callable for the create google ads link method over gRPC.

        Creates a GoogleAdsLink.

        Returns:
            Callable[[~.CreateGoogleAdsLinkRequest],
                    ~.GoogleAdsLink]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_google_ads_link" not in self._stubs:
            self._stubs["create_google_ads_link"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/CreateGoogleAdsLink",
                request_serializer=analytics_admin.CreateGoogleAdsLinkRequest.serialize,
                response_deserializer=resources.GoogleAdsLink.deserialize,
            )
        return self._stubs["create_google_ads_link"]

    @property
    def update_google_ads_link(
        self,
    ) -> Callable[
        [analytics_admin.UpdateGoogleAdsLinkRequest], resources.GoogleAdsLink
    ]:
        r"""Return a callable for the update google ads link method over gRPC.

        Updates a GoogleAdsLink on a property

        Returns:
            Callable[[~.UpdateGoogleAdsLinkRequest],
                    ~.GoogleAdsLink]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_google_ads_link" not in self._stubs:
            self._stubs["update_google_ads_link"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/UpdateGoogleAdsLink",
                request_serializer=analytics_admin.UpdateGoogleAdsLinkRequest.serialize,
                response_deserializer=resources.GoogleAdsLink.deserialize,
            )
        return self._stubs["update_google_ads_link"]

    @property
    def delete_google_ads_link(
        self,
    ) -> Callable[[analytics_admin.DeleteGoogleAdsLinkRequest], empty.Empty]:
        r"""Return a callable for the delete google ads link method over gRPC.

        Deletes a GoogleAdsLink on a property

        Returns:
            Callable[[~.DeleteGoogleAdsLinkRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_google_ads_link" not in self._stubs:
            self._stubs["delete_google_ads_link"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/DeleteGoogleAdsLink",
                request_serializer=analytics_admin.DeleteGoogleAdsLinkRequest.serialize,
                response_deserializer=empty.Empty.FromString,
            )
        return self._stubs["delete_google_ads_link"]

    @property
    def list_google_ads_links(
        self,
    ) -> Callable[
        [analytics_admin.ListGoogleAdsLinksRequest],
        analytics_admin.ListGoogleAdsLinksResponse,
    ]:
        r"""Return a callable for the list google ads links method over gRPC.

        Lists GoogleAdsLinks on a property.

        Returns:
            Callable[[~.ListGoogleAdsLinksRequest],
                    ~.ListGoogleAdsLinksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_google_ads_links" not in self._stubs:
            self._stubs["list_google_ads_links"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/ListGoogleAdsLinks",
                request_serializer=analytics_admin.ListGoogleAdsLinksRequest.serialize,
                response_deserializer=analytics_admin.ListGoogleAdsLinksResponse.deserialize,
            )
        return self._stubs["list_google_ads_links"]

    @property
    def get_data_sharing_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetDataSharingSettingsRequest], resources.DataSharingSettings
    ]:
        r"""Return a callable for the get data sharing settings method over gRPC.

        Get data sharing settings on an account.
        Data sharing settings are singletons.

        Returns:
            Callable[[~.GetDataSharingSettingsRequest],
                    ~.DataSharingSettings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_data_sharing_settings" not in self._stubs:
            self._stubs["get_data_sharing_settings"] = self.grpc_channel.unary_unary(
                "/google.analytics.admin.v1alpha.AnalyticsAdminService/GetDataSharingSettings",
                request_serializer=analytics_admin.GetDataSharingSettingsRequest.serialize,
                response_deserializer=resources.DataSharingSettings.deserialize,
            )
        return self._stubs["get_data_sharing_settings"]


__all__ = ("AnalyticsAdminServiceGrpcTransport",)
