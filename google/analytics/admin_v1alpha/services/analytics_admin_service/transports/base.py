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

import abc
import typing

from google import auth
from google.api_core import exceptions  # type: ignore
from google.auth import credentials  # type: ignore

from google.analytics.admin_v1alpha.types import analytics_admin
from google.analytics.admin_v1alpha.types import resources
from google.protobuf import empty_pb2 as empty  # type: ignore


class AnalyticsAdminServiceTransport(abc.ABC):
    """Abstract transport class for AnalyticsAdminService."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/analytics.edit",
        "https://www.googleapis.com/auth/analytics.manage.users",
        "https://www.googleapis.com/auth/analytics.manage.users.readonly",
        "https://www.googleapis.com/auth/analytics.readonly",
    )

    def __init__(
        self,
        *,
        host: str = "analyticsadmin.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: typing.Optional[str] = None,
        scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
        quota_project_id: typing.Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                credentials_file, scopes=scopes, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = auth.default(
                scopes=scopes, quota_project_id=quota_project_id
            )

        # Save the credentials.
        self._credentials = credentials

    @property
    def get_account(
        self,
    ) -> typing.Callable[
        [analytics_admin.GetAccountRequest],
        typing.Union[resources.Account, typing.Awaitable[resources.Account]],
    ]:
        raise NotImplementedError()

    @property
    def list_accounts(
        self,
    ) -> typing.Callable[
        [analytics_admin.ListAccountsRequest],
        typing.Union[
            analytics_admin.ListAccountsResponse,
            typing.Awaitable[analytics_admin.ListAccountsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_account(
        self,
    ) -> typing.Callable[
        [analytics_admin.DeleteAccountRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_account(
        self,
    ) -> typing.Callable[
        [analytics_admin.UpdateAccountRequest],
        typing.Union[resources.Account, typing.Awaitable[resources.Account]],
    ]:
        raise NotImplementedError()

    @property
    def provision_account_ticket(
        self,
    ) -> typing.Callable[
        [analytics_admin.ProvisionAccountTicketRequest],
        typing.Union[
            analytics_admin.ProvisionAccountTicketResponse,
            typing.Awaitable[analytics_admin.ProvisionAccountTicketResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_property(
        self,
    ) -> typing.Callable[
        [analytics_admin.GetPropertyRequest],
        typing.Union[resources.Property, typing.Awaitable[resources.Property]],
    ]:
        raise NotImplementedError()

    @property
    def list_properties(
        self,
    ) -> typing.Callable[
        [analytics_admin.ListPropertiesRequest],
        typing.Union[
            analytics_admin.ListPropertiesResponse,
            typing.Awaitable[analytics_admin.ListPropertiesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_property(
        self,
    ) -> typing.Callable[
        [analytics_admin.CreatePropertyRequest],
        typing.Union[resources.Property, typing.Awaitable[resources.Property]],
    ]:
        raise NotImplementedError()

    @property
    def delete_property(
        self,
    ) -> typing.Callable[
        [analytics_admin.DeletePropertyRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_property(
        self,
    ) -> typing.Callable[
        [analytics_admin.UpdatePropertyRequest],
        typing.Union[resources.Property, typing.Awaitable[resources.Property]],
    ]:
        raise NotImplementedError()

    @property
    def get_user_link(
        self,
    ) -> typing.Callable[
        [analytics_admin.GetUserLinkRequest],
        typing.Union[resources.UserLink, typing.Awaitable[resources.UserLink]],
    ]:
        raise NotImplementedError()

    @property
    def batch_get_user_links(
        self,
    ) -> typing.Callable[
        [analytics_admin.BatchGetUserLinksRequest],
        typing.Union[
            analytics_admin.BatchGetUserLinksResponse,
            typing.Awaitable[analytics_admin.BatchGetUserLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_user_links(
        self,
    ) -> typing.Callable[
        [analytics_admin.ListUserLinksRequest],
        typing.Union[
            analytics_admin.ListUserLinksResponse,
            typing.Awaitable[analytics_admin.ListUserLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def audit_user_links(
        self,
    ) -> typing.Callable[
        [analytics_admin.AuditUserLinksRequest],
        typing.Union[
            analytics_admin.AuditUserLinksResponse,
            typing.Awaitable[analytics_admin.AuditUserLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_user_link(
        self,
    ) -> typing.Callable[
        [analytics_admin.CreateUserLinkRequest],
        typing.Union[resources.UserLink, typing.Awaitable[resources.UserLink]],
    ]:
        raise NotImplementedError()

    @property
    def batch_create_user_links(
        self,
    ) -> typing.Callable[
        [analytics_admin.BatchCreateUserLinksRequest],
        typing.Union[
            analytics_admin.BatchCreateUserLinksResponse,
            typing.Awaitable[analytics_admin.BatchCreateUserLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_user_link(
        self,
    ) -> typing.Callable[
        [analytics_admin.UpdateUserLinkRequest],
        typing.Union[resources.UserLink, typing.Awaitable[resources.UserLink]],
    ]:
        raise NotImplementedError()

    @property
    def batch_update_user_links(
        self,
    ) -> typing.Callable[
        [analytics_admin.BatchUpdateUserLinksRequest],
        typing.Union[
            analytics_admin.BatchUpdateUserLinksResponse,
            typing.Awaitable[analytics_admin.BatchUpdateUserLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_user_link(
        self,
    ) -> typing.Callable[
        [analytics_admin.DeleteUserLinkRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def batch_delete_user_links(
        self,
    ) -> typing.Callable[
        [analytics_admin.BatchDeleteUserLinksRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_web_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.GetWebDataStreamRequest],
        typing.Union[
            resources.WebDataStream, typing.Awaitable[resources.WebDataStream]
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_web_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.DeleteWebDataStreamRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_web_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.UpdateWebDataStreamRequest],
        typing.Union[
            resources.WebDataStream, typing.Awaitable[resources.WebDataStream]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_web_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.CreateWebDataStreamRequest],
        typing.Union[
            resources.WebDataStream, typing.Awaitable[resources.WebDataStream]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_web_data_streams(
        self,
    ) -> typing.Callable[
        [analytics_admin.ListWebDataStreamsRequest],
        typing.Union[
            analytics_admin.ListWebDataStreamsResponse,
            typing.Awaitable[analytics_admin.ListWebDataStreamsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_ios_app_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.GetIosAppDataStreamRequest],
        typing.Union[
            resources.IosAppDataStream, typing.Awaitable[resources.IosAppDataStream]
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_ios_app_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.DeleteIosAppDataStreamRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_ios_app_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.UpdateIosAppDataStreamRequest],
        typing.Union[
            resources.IosAppDataStream, typing.Awaitable[resources.IosAppDataStream]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_ios_app_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.CreateIosAppDataStreamRequest],
        typing.Union[
            resources.IosAppDataStream, typing.Awaitable[resources.IosAppDataStream]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_ios_app_data_streams(
        self,
    ) -> typing.Callable[
        [analytics_admin.ListIosAppDataStreamsRequest],
        typing.Union[
            analytics_admin.ListIosAppDataStreamsResponse,
            typing.Awaitable[analytics_admin.ListIosAppDataStreamsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_android_app_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.GetAndroidAppDataStreamRequest],
        typing.Union[
            resources.AndroidAppDataStream,
            typing.Awaitable[resources.AndroidAppDataStream],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_android_app_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.DeleteAndroidAppDataStreamRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_android_app_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.UpdateAndroidAppDataStreamRequest],
        typing.Union[
            resources.AndroidAppDataStream,
            typing.Awaitable[resources.AndroidAppDataStream],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_android_app_data_stream(
        self,
    ) -> typing.Callable[
        [analytics_admin.CreateAndroidAppDataStreamRequest],
        typing.Union[
            resources.AndroidAppDataStream,
            typing.Awaitable[resources.AndroidAppDataStream],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_android_app_data_streams(
        self,
    ) -> typing.Callable[
        [analytics_admin.ListAndroidAppDataStreamsRequest],
        typing.Union[
            analytics_admin.ListAndroidAppDataStreamsResponse,
            typing.Awaitable[analytics_admin.ListAndroidAppDataStreamsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_enhanced_measurement_settings(
        self,
    ) -> typing.Callable[
        [analytics_admin.GetEnhancedMeasurementSettingsRequest],
        typing.Union[
            resources.EnhancedMeasurementSettings,
            typing.Awaitable[resources.EnhancedMeasurementSettings],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_enhanced_measurement_settings(
        self,
    ) -> typing.Callable[
        [analytics_admin.UpdateEnhancedMeasurementSettingsRequest],
        typing.Union[
            resources.EnhancedMeasurementSettings,
            typing.Awaitable[resources.EnhancedMeasurementSettings],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_firebase_link(
        self,
    ) -> typing.Callable[
        [analytics_admin.CreateFirebaseLinkRequest],
        typing.Union[resources.FirebaseLink, typing.Awaitable[resources.FirebaseLink]],
    ]:
        raise NotImplementedError()

    @property
    def update_firebase_link(
        self,
    ) -> typing.Callable[
        [analytics_admin.UpdateFirebaseLinkRequest],
        typing.Union[resources.FirebaseLink, typing.Awaitable[resources.FirebaseLink]],
    ]:
        raise NotImplementedError()

    @property
    def delete_firebase_link(
        self,
    ) -> typing.Callable[
        [analytics_admin.DeleteFirebaseLinkRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_firebase_links(
        self,
    ) -> typing.Callable[
        [analytics_admin.ListFirebaseLinksRequest],
        typing.Union[
            analytics_admin.ListFirebaseLinksResponse,
            typing.Awaitable[analytics_admin.ListFirebaseLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_global_site_tag(
        self,
    ) -> typing.Callable[
        [analytics_admin.GetGlobalSiteTagRequest],
        typing.Union[
            resources.GlobalSiteTag, typing.Awaitable[resources.GlobalSiteTag]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_google_ads_link(
        self,
    ) -> typing.Callable[
        [analytics_admin.CreateGoogleAdsLinkRequest],
        typing.Union[
            resources.GoogleAdsLink, typing.Awaitable[resources.GoogleAdsLink]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_google_ads_link(
        self,
    ) -> typing.Callable[
        [analytics_admin.UpdateGoogleAdsLinkRequest],
        typing.Union[
            resources.GoogleAdsLink, typing.Awaitable[resources.GoogleAdsLink]
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_google_ads_link(
        self,
    ) -> typing.Callable[
        [analytics_admin.DeleteGoogleAdsLinkRequest],
        typing.Union[empty.Empty, typing.Awaitable[empty.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_google_ads_links(
        self,
    ) -> typing.Callable[
        [analytics_admin.ListGoogleAdsLinksRequest],
        typing.Union[
            analytics_admin.ListGoogleAdsLinksResponse,
            typing.Awaitable[analytics_admin.ListGoogleAdsLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_data_sharing_settings(
        self,
    ) -> typing.Callable[
        [analytics_admin.GetDataSharingSettingsRequest],
        typing.Union[
            resources.DataSharingSettings,
            typing.Awaitable[resources.DataSharingSettings],
        ],
    ]:
        raise NotImplementedError()


__all__ = ("AnalyticsAdminServiceTransport",)
