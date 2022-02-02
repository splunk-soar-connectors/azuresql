# File: microsoftazuresql_connector.py
#
# Copyright (c) 2019-2021 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
#
DEFAULT_TIMEOUT = 30

CONNECTION_STRING = "Driver={driver};Server={host},1433;Database={database};Uid={uid};Pwd={pwd};Encrypt=no;" \
                    "TrustServerCertificate={trust_server};Trusted_Connection=no;Connection Timeout=30;"
