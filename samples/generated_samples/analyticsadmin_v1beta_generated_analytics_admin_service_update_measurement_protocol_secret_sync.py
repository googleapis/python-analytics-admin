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
# Snippet for UpdateMeasurementProtocolSecret
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-analytics-admin


# [START analyticsadmin_v1beta_generated_AnalyticsAdminService_UpdateMeasurementProtocolSecret_sync]
from google.analytics import admin_v1beta


def sample_update_measurement_protocol_secret():
    # Create a client
    client = admin_v1beta.AnalyticsAdminServiceClient()

    # Initialize request argument(s)
    measurement_protocol_secret = admin_v1beta.MeasurementProtocolSecret()
    measurement_protocol_secret.display_name = "display_name_value"

    request = admin_v1beta.UpdateMeasurementProtocolSecretRequest(
        measurement_protocol_secret=measurement_protocol_secret,
    )

    # Make the request
    response = client.update_measurement_protocol_secret(request=request)

    # Handle the response
    print(response)

# [END analyticsadmin_v1beta_generated_AnalyticsAdminService_UpdateMeasurementProtocolSecret_sync]