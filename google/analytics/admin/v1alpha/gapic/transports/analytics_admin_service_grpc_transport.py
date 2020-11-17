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


import google.api_core.grpc_helpers

from google.analytics.admin.v1alpha.proto import analytics_admin_pb2_grpc


class AnalyticsAdminServiceGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.analytics.admin.v1alpha AnalyticsAdminService API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = (
        "https://www.googleapis.com/auth/analytics.edit",
        "https://www.googleapis.com/auth/analytics.manage.users",
        "https://www.googleapis.com/auth/analytics.manage.users.readonly",
        "https://www.googleapis.com/auth/analytics.readonly",
    )

    def __init__(
        self,
        channel=None,
        credentials=None,
        address="analyticsadmin.googleapis.com:443",
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive.",
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "analytics_admin_service_stub": analytics_admin_pb2_grpc.AnalyticsAdminServiceStub(
                channel
            ),
        }

    @classmethod
    def create_channel(
        cls, address="analyticsadmin.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def get_account(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.get_account`.

        Lookup for a single Account.
        Throws "Target not found" if no such account found, or if caller does not
        have permissions to access it.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].GetAccount

    @property
    def list_accounts(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.list_accounts`.

        Returns all accounts accessible by the caller.

        Note that these accounts might not currently have GA4 properties.
        Soft-deleted (ie: "trashed") accounts are excluded by default.
        Returns an empty list if no relevant accounts are found.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].ListAccounts

    @property
    def delete_account(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.delete_account`.

        Marks target Account as soft-deleted (ie: "trashed") and returns it.

        This API does not have a method to restore soft-deleted accounts.
        However, they can be restored using the Trash Can UI.

        If the accounts are not restored before the expiration time, the account
        and all child resources (eg: Properties, GoogleAdsLinks, Streams,
        UserLinks) will be permanently purged.
        https://support.google.com/analytics/answer/6154772

        Returns an error if the target is not found.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].DeleteAccount

    @property
    def update_account(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.update_account`.

        Updates an account.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].UpdateAccount

    @property
    def provision_account_ticket(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.provision_account_ticket`.

        Requests a ticket for creating an account.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].ProvisionAccountTicket

    @property
    def list_account_summaries(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.list_account_summaries`.

        Returns summaries of all accounts accessible by the caller.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].ListAccountSummaries

    @property
    def get_property(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.get_property`.

        Lookup for a single "GA4" Property.

        Throws "Target not found" if no such property found, if property is not
        of the type "GA4", or if caller does not have permissions to access it.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].GetProperty

    @property
    def list_properties(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.list_properties`.

        Returns child Properties under the specified parent Account.

        Only "GA4" properties will be returned.
        Properties will be excluded if the caller does not have access.
        Soft-deleted (ie: "trashed") properties are excluded by default.
        Returns an empty list if no relevant properties are found.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].ListProperties

    @property
    def create_property(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.create_property`.

        Creates an "GA4" property with the specified location and attributes.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].CreateProperty

    @property
    def delete_property(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.delete_property`.

        Marks target Property as soft-deleted (ie: "trashed") and returns it.

        This API does not have a method to restore soft-deleted properties.
        However, they can be restored using the Trash Can UI.

        If the properties are not restored before the expiration time, the Property
        and all child resources (eg: GoogleAdsLinks, Streams, UserLinks)
        will be permanently purged.
        https://support.google.com/analytics/answer/6154772

        Returns an error if the target is not found, or is not an GA4 Property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].DeleteProperty

    @property
    def update_property(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.update_property`.

        Updates a property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].UpdateProperty

    @property
    def get_user_link(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.get_user_link`.

        Gets information about a user's link to an account or property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].GetUserLink

    @property
    def batch_get_user_links(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.batch_get_user_links`.

        Gets information about multiple users' links to an account or property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].BatchGetUserLinks

    @property
    def list_user_links(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.list_user_links`.

        Lists all user links on an account or property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].ListUserLinks

    @property
    def audit_user_links(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.audit_user_links`.

        Lists all user links on an account or property, including implicit ones
        that come from effective permissions granted by groups or organization
        admin roles.

        If a returned user link does not have direct permissions, they cannot
        be removed from the account or property directly with the DeleteUserLink
        command. They have to be removed from the group/etc that gives them
        permissions, which is currently only usable/discoverable in the GA or GMP
        UIs.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].AuditUserLinks

    @property
    def create_user_link(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.create_user_link`.

        Creates a user link on an account or property.

        If the user with the specified email already has permissions on the
        account or property, then the user's existing permissions will be unioned
        with the permissions specified in the new UserLink.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].CreateUserLink

    @property
    def batch_create_user_links(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.batch_create_user_links`.

        Creates information about multiple users' links to an account or property.

        This method is transactional. If any UserLink cannot be created, none of
        the UserLinks will be created.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].BatchCreateUserLinks

    @property
    def update_user_link(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.update_user_link`.

        Updates a user link on an account or property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].UpdateUserLink

    @property
    def batch_update_user_links(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.batch_update_user_links`.

        Updates information about multiple users' links to an account or property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].BatchUpdateUserLinks

    @property
    def delete_user_link(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.delete_user_link`.

        Deletes a user link on an account or property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].DeleteUserLink

    @property
    def batch_delete_user_links(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.batch_delete_user_links`.

        Deletes information about multiple users' links to an account or property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].BatchDeleteUserLinks

    @property
    def get_web_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.get_web_data_stream`.

        Lookup for a single WebDataStream

        Throws "Target not found" if no such web data stream found, or if the
        caller does not have permissions to access it.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].GetWebDataStream

    @property
    def delete_web_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.delete_web_data_stream`.

        Deletes a web stream on a property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].DeleteWebDataStream

    @property
    def update_web_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.update_web_data_stream`.

        Updates a web stream on a property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].UpdateWebDataStream

    @property
    def create_web_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.create_web_data_stream`.

        Creates a web stream with the specified location and attributes.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].CreateWebDataStream

    @property
    def list_web_data_streams(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.list_web_data_streams`.

        Returns child web data streams under the specified parent property.

        Web data streams will be excluded if the caller does not have access.
        Returns an empty list if no relevant web data streams are found.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].ListWebDataStreams

    @property
    def get_ios_app_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.get_ios_app_data_stream`.

        Lookup for a single IosAppDataStream

        Throws "Target not found" if no such iOS app data stream found, or if the
        caller does not have permissions to access it.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].GetIosAppDataStream

    @property
    def delete_ios_app_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.delete_ios_app_data_stream`.

        Deletes an iOS app stream on a property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].DeleteIosAppDataStream

    @property
    def update_ios_app_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.update_ios_app_data_stream`.

        Updates an iOS app stream on a property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].UpdateIosAppDataStream

    @property
    def create_ios_app_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.create_ios_app_data_stream`.

        Creates an iOS app data stream with the specified location and attributes.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].CreateIosAppDataStream

    @property
    def list_ios_app_data_streams(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.list_ios_app_data_streams`.

        Returns child iOS app data streams under the specified parent property.

        iOS app data streams will be excluded if the caller does not have access.
        Returns an empty list if no relevant iOS app data streams are found.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].ListIosAppDataStreams

    @property
    def get_android_app_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.get_android_app_data_stream`.

        Lookup for a single AndroidAppDataStream

        Throws "Target not found" if no such android app data stream found, or if
        the caller does not have permissions to access it.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].GetAndroidAppDataStream

    @property
    def delete_android_app_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.delete_android_app_data_stream`.

        Deletes an android app stream on a property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].DeleteAndroidAppDataStream

    @property
    def update_android_app_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.update_android_app_data_stream`.

        Updates an android app stream on a property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].UpdateAndroidAppDataStream

    @property
    def create_android_app_data_stream(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.create_android_app_data_stream`.

        Creates an android app stream with the specified location and attributes.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].CreateAndroidAppDataStream

    @property
    def list_android_app_data_streams(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.list_android_app_data_streams`.

        Returns child android app streams under the specified parent property.

        Android app streams will be excluded if the caller does not have access.
        Returns an empty list if no relevant android app streams are found.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].ListAndroidAppDataStreams

    @property
    def get_enhanced_measurement_settings(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.get_enhanced_measurement_settings`.

        Returns the singleton enhanced measurement settings for this web stream.
        Note that the stream must enable enhanced measurement for these settings to
        take effect.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs[
            "analytics_admin_service_stub"
        ].GetEnhancedMeasurementSettings

    @property
    def update_enhanced_measurement_settings(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.update_enhanced_measurement_settings`.

        Updates the singleton enhanced measurement settings for this web stream.
        Note that the stream must enable enhanced measurement for these settings to
        take effect.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs[
            "analytics_admin_service_stub"
        ].UpdateEnhancedMeasurementSettings

    @property
    def create_firebase_link(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.create_firebase_link`.

        Creates a FirebaseLink.

        Properties can have at most one FirebaseLink.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].CreateFirebaseLink

    @property
    def update_firebase_link(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.update_firebase_link`.

        Updates a FirebaseLink on a property

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].UpdateFirebaseLink

    @property
    def delete_firebase_link(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.delete_firebase_link`.

        Deletes a FirebaseLink on a property

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].DeleteFirebaseLink

    @property
    def list_firebase_links(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.list_firebase_links`.

        Lists FirebaseLinks on a property.
        Properties can have at most one FirebaseLink.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].ListFirebaseLinks

    @property
    def get_global_site_tag(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.get_global_site_tag`.

        Returns the Site Tag for the specified web stream.
        Site Tags are immutable singletons.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].GetGlobalSiteTag

    @property
    def create_google_ads_link(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.create_google_ads_link`.

        Creates a GoogleAdsLink.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].CreateGoogleAdsLink

    @property
    def update_google_ads_link(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.update_google_ads_link`.

        Updates a GoogleAdsLink on a property

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].UpdateGoogleAdsLink

    @property
    def delete_google_ads_link(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.delete_google_ads_link`.

        Deletes a GoogleAdsLink on a property

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].DeleteGoogleAdsLink

    @property
    def list_google_ads_links(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.list_google_ads_links`.

        Lists GoogleAdsLinks on a property.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].ListGoogleAdsLinks

    @property
    def get_data_sharing_settings(self):
        """Return the gRPC stub for :meth:`AnalyticsAdminServiceClient.get_data_sharing_settings`.

        Get data sharing settings on an account.
        Data sharing settings are singletons.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["analytics_admin_service_stub"].GetDataSharingSettings
