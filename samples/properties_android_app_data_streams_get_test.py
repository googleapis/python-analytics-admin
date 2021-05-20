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

import os

import properties_android_app_data_streams_get


TEST_PROPERTY_ID = os.getenv("GA_TEST_PROPERTY_ID")
TEST_ANDROID_APP_DATA_STREAM_ID = os.getenv("GA_TEST_ANDROID_APP_DATA_STREAM_ID")


def test_properties_android_app_data_streams_get(capsys):
    properties_android_app_data_streams_get.get_android_app_data_stream(
        TEST_PROPERTY_ID, TEST_ANDROID_APP_DATA_STREAM_ID
    )
    out, _ = capsys.readouterr()
    assert "Result" in out
