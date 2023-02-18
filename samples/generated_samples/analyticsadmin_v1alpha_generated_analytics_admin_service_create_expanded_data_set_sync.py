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
# Snippet for CreateExpandedDataSet
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-analytics-admin


# [START analyticsadmin_v1alpha_generated_AnalyticsAdminService_CreateExpandedDataSet_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.analytics import admin_v1alpha


def sample_create_expanded_data_set():
    # Create a client
    client = admin_v1alpha.AnalyticsAdminServiceClient()

    # Initialize request argument(s)
    expanded_data_set = admin_v1alpha.ExpandedDataSet()
    expanded_data_set.display_name = "display_name_value"

    request = admin_v1alpha.CreateExpandedDataSetRequest(
        parent="parent_value",
        expanded_data_set=expanded_data_set,
    )

    # Make the request
    response = client.create_expanded_data_set(request=request)

    # Handle the response
    print(response)

# [END analyticsadmin_v1alpha_generated_AnalyticsAdminService_CreateExpandedDataSet_sync]
