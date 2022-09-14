# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
# Generated code. DO NOT EDIT!
#
# Snippet for GetMeasurementProtocolSecret
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-analytics-admin


# [START analyticsadmin_v1beta_generated_AnalyticsAdminService_GetMeasurementProtocolSecret_sync_87b1b3de]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.analytics import admin_v1beta


def sample_get_measurement_protocol_secret():
    # Create a client
    client = admin_v1beta.AnalyticsAdminServiceClient()

    # Initialize request argument(s)
    request = admin_v1beta.GetMeasurementProtocolSecretRequest(
        name="name_value",
    )

    # Make the request
    response = client.get_measurement_protocol_secret(request=request)

    # Handle the response
    print(response)

# [END analyticsadmin_v1beta_generated_AnalyticsAdminService_GetMeasurementProtocolSecret_sync_87b1b3de]
