# Copyright 2021 Google LLC All Rights Reserved.
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

import pytest

import properties_data_streams_measurement_protocol_secrets_update

FAKE_PROPERTY_ID = "1"
FAKE_STREAM_ID = "1"
FAKE_SECRET_ID = "1"


def test_properties_data_streams_measurement_protocol_secrets_update():
    transports = ["grpc", "rest"]
    for transport in transports:
        # This test ensures that the call is valid and reaches the server, even
        # though the operation does not succeed due to permission error.
        with pytest.raises(Exception, match="The caller does not have permission"):
            properties_data_streams_measurement_protocol_secrets_update.update_measurement_protocol_secret(
                FAKE_PROPERTY_ID, FAKE_STREAM_ID, FAKE_SECRET_ID, transport=transport
            )
