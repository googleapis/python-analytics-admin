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

"""Wrappers for protocol buffer enum types."""

import enum


class IndustryCategory(enum.IntEnum):
    """
    The category selected for this property, used for industry benchmarking.

    Attributes:
      INDUSTRY_CATEGORY_UNSPECIFIED (int): Industry category unspecified
      AUTOMOTIVE (int): Automotive
      BUSINESS_AND_INDUSTRIAL_MARKETS (int): Business and industrial markets
      FINANCE (int): Finance
      HEALTHCARE (int): Healthcare
      TECHNOLOGY (int): Technology
      TRAVEL (int): Travel
      OTHER (int): Other
      ARTS_AND_ENTERTAINMENT (int): Arts and entertainment
      BEAUTY_AND_FITNESS (int): Beauty and fitness
      BOOKS_AND_LITERATURE (int): Books and literature
      FOOD_AND_DRINK (int): Food and drink
      GAMES (int): Games
      HOBBIES_AND_LEISURE (int): Hobbies and leisure
      HOME_AND_GARDEN (int): Home and garden
      INTERNET_AND_TELECOM (int): Internet and telecom
      LAW_AND_GOVERNMENT (int): Law and government
      NEWS (int): News
      ONLINE_COMMUNITIES (int): Online communities
      PEOPLE_AND_SOCIETY (int): People and society
      PETS_AND_ANIMALS (int): Pets and animals
      REAL_ESTATE (int): Real estate
      REFERENCE (int): Reference
      SCIENCE (int): Science
      SPORTS (int): Sports
      JOBS_AND_EDUCATION (int): Jobs and education
      SHOPPING (int): Shopping
    """
    INDUSTRY_CATEGORY_UNSPECIFIED = 0
    AUTOMOTIVE = 1
    BUSINESS_AND_INDUSTRIAL_MARKETS = 2
    FINANCE = 3
    HEALTHCARE = 4
    TECHNOLOGY = 5
    TRAVEL = 6
    OTHER = 7
    ARTS_AND_ENTERTAINMENT = 8
    BEAUTY_AND_FITNESS = 9
    BOOKS_AND_LITERATURE = 10
    FOOD_AND_DRINK = 11
    GAMES = 12
    HOBBIES_AND_LEISURE = 13
    HOME_AND_GARDEN = 14
    INTERNET_AND_TELECOM = 15
    LAW_AND_GOVERNMENT = 16
    NEWS = 17
    ONLINE_COMMUNITIES = 18
    PEOPLE_AND_SOCIETY = 19
    PETS_AND_ANIMALS = 20
    REAL_ESTATE = 21
    REFERENCE = 22
    SCIENCE = 23
    SPORTS = 24
    JOBS_AND_EDUCATION = 25
    SHOPPING = 26


class MaximumUserAccess(enum.IntEnum):
    """
    Maximum access settings that Firebase user receive on the linked Analytics
    property.

    Attributes:
      MAXIMUM_USER_ACCESS_UNSPECIFIED (int): Unspecified maximum user access.
      NO_ACCESS (int): Firebase users have no access to the Analytics property.
      READ_AND_ANALYZE (int): Firebase users have Read & Analyze access to the Analytics property.
      EDITOR_WITHOUT_LINK_MANAGEMENT (int): Firebase users have edit access to the Analytics property, but may not
      manage the Firebase link.
      EDITOR_INCLUDING_LINK_MANAGEMENT (int): Firebase users have edit access to the Analytics property and may manage
      the Firebase link.
    """
    MAXIMUM_USER_ACCESS_UNSPECIFIED = 0
    NO_ACCESS = 1
    READ_AND_ANALYZE = 2
    EDITOR_WITHOUT_LINK_MANAGEMENT = 3
    EDITOR_INCLUDING_LINK_MANAGEMENT = 4
