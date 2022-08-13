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
# Snippet for CreateAudience
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-analytics-admin


# [START analyticsadmin_v1alpha_generated_AnalyticsAdminService_CreateAudience_async]
from google.analytics import admin_v1alpha


async def sample_create_audience():
    # Create a client
    client = admin_v1alpha.AnalyticsAdminServiceAsyncClient()

    # Initialize request argument(s)
    audience = admin_v1alpha.Audience()
    audience.display_name = "display_name_value"
    audience.description = "description_value"
    audience.membership_duration_days = 2561
    audience.filter_clauses.simple_filter.scope = "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS"
    audience.filter_clauses.clause_type = "EXCLUDE"

    request = admin_v1alpha.CreateAudienceRequest(
        parent="parent_value",
        audience=audience,
    )

    # Make the request
    response = await client.create_audience(request=request)

    # Handle the response
    print(response)

# [END analyticsadmin_v1alpha_generated_AnalyticsAdminService_CreateAudience_async]
