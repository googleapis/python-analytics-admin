# Changelog

## [0.11.0](https://github.com/googleapis/python-analytics-admin/compare/v0.10.1...v0.11.0) (2022-09-12)


### Features

* Enable REST transport support ([#265](https://github.com/googleapis/python-analytics-admin/issues/265)) ([c220210](https://github.com/googleapis/python-analytics-admin/commit/c220210adf0093a1257d8e91209488c1dec7602b))


### Bug Fixes

* **deps:** require google-api-core>=1.33.0,>=2.8.0 ([c220210](https://github.com/googleapis/python-analytics-admin/commit/c220210adf0093a1257d8e91209488c1dec7602b))
* **deps:** require protobuf >= 3.20.1 ([c220210](https://github.com/googleapis/python-analytics-admin/commit/c220210adf0093a1257d8e91209488c1dec7602b))

## [0.10.1](https://github.com/googleapis/python-analytics-admin/compare/v0.10.0...v0.10.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#250](https://github.com/googleapis/python-analytics-admin/issues/250)) ([84a8df1](https://github.com/googleapis/python-analytics-admin/commit/84a8df140081c5095d71fa9dd99b83549d07c9c6))
* **deps:** require proto-plus >= 1.22.0 ([84a8df1](https://github.com/googleapis/python-analytics-admin/commit/84a8df140081c5095d71fa9dd99b83549d07c9c6))

## [0.10.0](https://github.com/googleapis/python-analytics-admin/compare/v0.9.0...v0.10.0) (2022-08-05)


### Features

* **v1alpha:** add `GetAttributionSettings`, `UpdateAttributionSettings` methods ([6e6b741](https://github.com/googleapis/python-analytics-admin/commit/6e6b74144706ffe6ecd898d11f9eb41e46d77c94))
* **v1alpha:** add `GetAudience`, 'ListAudience', 'CreateAudience', 'UpdateAudience', 'ArchiveAudience' methods ([6e6b741](https://github.com/googleapis/python-analytics-admin/commit/6e6b74144706ffe6ecd898d11f9eb41e46d77c94))
* **v1alpha:** add `RunAccessReport` method ([#246](https://github.com/googleapis/python-analytics-admin/issues/246)) ([6e6b741](https://github.com/googleapis/python-analytics-admin/commit/6e6b74144706ffe6ecd898d11f9eb41e46d77c94))

## [0.9.0](https://github.com/googleapis/python-analytics-admin/compare/v0.8.2...v0.9.0) (2022-07-20)


### Features

* add audience parameter ([dc6107c](https://github.com/googleapis/python-analytics-admin/commit/dc6107cbe784ac6e4dcd2b2a0fd118ed1a2b929e))
* release the Google Analytics Admin API V1 Beta ([dc6107c](https://github.com/googleapis/python-analytics-admin/commit/dc6107cbe784ac6e4dcd2b2a0fd118ed1a2b929e))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#236](https://github.com/googleapis/python-analytics-admin/issues/236)) ([dc6107c](https://github.com/googleapis/python-analytics-admin/commit/dc6107cbe784ac6e4dcd2b2a0fd118ed1a2b929e))
* require python 3.7+ ([#239](https://github.com/googleapis/python-analytics-admin/issues/239)) ([ec0580e](https://github.com/googleapis/python-analytics-admin/commit/ec0580e77d8b7ec395f0a2d0979b336ba44a19fd))

## [0.8.2](https://github.com/googleapis/python-analytics-admin/compare/v0.8.1...v0.8.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#227](https://github.com/googleapis/python-analytics-admin/issues/227)) ([2dc98b3](https://github.com/googleapis/python-analytics-admin/commit/2dc98b354cefb6eeafe2a8065b3d85e60c0c7824))


### Documentation

* fix changelog header to consistent size ([#228](https://github.com/googleapis/python-analytics-admin/issues/228)) ([2385b9b](https://github.com/googleapis/python-analytics-admin/commit/2385b9b9b96abac09b9adebd6d462d8a95afe356))

## [0.8.1](https://github.com/googleapis/python-analytics-admin/compare/v0.8.0...v0.8.1) (2022-05-13)


### Bug Fixes

* CustomDimension and CustomMetric resource configuration ([#222](https://github.com/googleapis/python-analytics-admin/issues/222)) ([79470bd](https://github.com/googleapis/python-analytics-admin/commit/79470bdd437d3fe45cdcf1e89b13f6e1b289bd24))

## [0.8.0](https://github.com/googleapis/python-analytics-admin/compare/v0.7.2...v0.8.0) (2022-03-07)


### Features

* add `CreateDataStream`, `DeleteDataStream`, `UpdateDataStream`, `ListDataStreams` operations to support the new `DataStream` resource ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* add `DISPLAY_VIDEO_360_ADVERTISER_LINK`,  `DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL` fields to `ChangeHistoryResourceType` enum ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* add `restricted_metric_type` field to the `CustomMetric` resource ([aeb64bf](https://github.com/googleapis/python-analytics-admin/commit/aeb64bfc7653de24c84f54f9a921c4dc3f63a31b))
* add api key support ([#185](https://github.com/googleapis/python-analytics-admin/issues/185)) ([2ec0a0b](https://github.com/googleapis/python-analytics-admin/commit/2ec0a0b648edcfb3b76bf847a4463cbb551e1997))
* add the `account` field to the `Property` type ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* add the AcknowledgeUserDataCollection operation ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* add the new resource type `DataStream`, which is planned to eventually replace `WebDataStream`, `IosAppDataStream`, `AndroidAppDataStream` resources ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* move the `GlobalSiteTag` resource from the property level to the data stream level ([aeb64bf](https://github.com/googleapis/python-analytics-admin/commit/aeb64bfc7653de24c84f54f9a921c4dc3f63a31b))
* remove `WebDataStream`, `IosAppDataStream`, `AndroidAppDataStream` resources ([#195](https://github.com/googleapis/python-analytics-admin/issues/195)) ([aeb64bf](https://github.com/googleapis/python-analytics-admin/commit/aeb64bfc7653de24c84f54f9a921c4dc3f63a31b)), closes [#184](https://github.com/googleapis/python-analytics-admin/issues/184)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#194](https://github.com/googleapis/python-analytics-admin/issues/194)) ([f2b9bc3](https://github.com/googleapis/python-analytics-admin/commit/f2b9bc38695697dfadc451eb102cd8b4e4e90c34))
* **deps:** require proto-plus>=1.15.0 ([f2b9bc3](https://github.com/googleapis/python-analytics-admin/commit/f2b9bc38695697dfadc451eb102cd8b4e4e90c34))
* remove `GetEnhancedMeasurementSettings`, `UpdateEnhancedMeasurementSettingsRequest`, `UpdateEnhancedMeasurementSettingsRequest` operations from the API ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))
* resolve DuplicateCredentialArgs error when using credentials_file ([49c8857](https://github.com/googleapis/python-analytics-admin/commit/49c8857d28b7e2a9c563046d0b0cdee39e3b312e))


### Documentation

* add autogenerated code snippets ([323815a](https://github.com/googleapis/python-analytics-admin/commit/323815a140de25fe75e7e9c9f45fdaa45c71ce35))
* update the documentation with a new list of valid values for `UserLink.direct_roles` field ([03abb54](https://github.com/googleapis/python-analytics-admin/commit/03abb54e9a394bb4f69203c98099a5e628116b48))

## [0.7.2](https://www.github.com/googleapis/python-analytics-admin/compare/v0.7.1...v0.7.2) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([be96ebc](https://www.github.com/googleapis/python-analytics-admin/commit/be96ebc5d99e3d3ea1883ce22fafa95847825fb3))
* **deps:** require google-api-core >= 1.28.0 ([be96ebc](https://www.github.com/googleapis/python-analytics-admin/commit/be96ebc5d99e3d3ea1883ce22fafa95847825fb3))


### Documentation

* list oneofs in docstring ([be96ebc](https://www.github.com/googleapis/python-analytics-admin/commit/be96ebc5d99e3d3ea1883ce22fafa95847825fb3))

## [0.7.1](https://www.github.com/googleapis/python-analytics-admin/compare/v0.7.0...v0.7.1) (2021-10-19)


### Documentation

* **samples:** add samples for Measurement Protocol Secrets management methods ([#152](https://www.github.com/googleapis/python-analytics-admin/issues/152)) ([e264571](https://www.github.com/googleapis/python-analytics-admin/commit/e2645719d6fc518857f64482c48f60e1e0963fc7))
* **samples:** add samples for Conversion Event management methods ([#153](https://www.github.com/googleapis/python-analytics-admin/issues/153)) ([126f271](https://www.github.com/googleapis/python-analytics-admin/commit/126f2711c9fdedaa7cddfe8b3c7bdaff03d0297e))

## [0.7.0](https://www.github.com/googleapis/python-analytics-admin/compare/v0.6.0...v0.7.0) (2021-10-12)


### Features

* add support for python 3.10 ([#150](https://www.github.com/googleapis/python-analytics-admin/issues/150)) ([f6d2033](https://www.github.com/googleapis/python-analytics-admin/commit/f6d2033e054e0c13e1134e95ec822a93bf227798))

## [0.6.0](https://www.github.com/googleapis/python-analytics-admin/compare/v0.5.2...v0.6.0) (2021-10-08)


### Features

* add context manager support in client ([#146](https://www.github.com/googleapis/python-analytics-admin/issues/146)) ([f1559b6](https://www.github.com/googleapis/python-analytics-admin/commit/f1559b6074e75e453e0f3c6f32a21bfac487e562))

## [0.5.2](https://www.github.com/googleapis/python-analytics-admin/compare/v0.5.1...v0.5.2) (2021-10-07)


### Bug Fixes

* improper types in pagers generation ([aa076a9](https://www.github.com/googleapis/python-analytics-admin/commit/aa076a9bde90aaa2ceeaaa580c499a42e212b39f))


### Documentation

* add samples for accounts.search_change_history_events() method ([#137](https://www.github.com/googleapis/python-analytics-admin/issues/137)) ([c299b37](https://www.github.com/googleapis/python-analytics-admin/commit/c299b370c42a8684faa86f5bb5f65b3da8a2d0a8))

## [0.5.1](https://www.github.com/googleapis/python-analytics-admin/compare/v0.5.0...v0.5.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([256c880](https://www.github.com/googleapis/python-analytics-admin/commit/256c880c486761e32c00ece8ee40ee3a23d87bdb))

## [0.5.0](https://www.github.com/googleapis/python-analytics-admin/compare/v0.4.3...v0.5.0) (2021-08-25)


### Features

* add `CancelDisplayVideo360AdvertiserLinkProposal` method to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `CreateDisplayVideo360AdvertiserLink`, `DeleteDisplayVideo360AdvertiserLink` methods to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `custom` output only field to `ConversionEvent` type ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `data_retention_settings` fields to `ChangeHistoryChange.resource` oneof field. ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `DeleteDisplayVideo360AdvertiserLinkProposal` method to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `display_video_360_advertiser_link_proposal` fields to `ChangeHistoryChange.resource` oneof field. ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `display_video_360_advertiser_link` fields to `ChangeHistoryChange.resource` oneof field. ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `DisplayVideo360AdvertiserLink`, `LinkProposalState` types to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `GetDataRetentionSettings`, `UpdateDataRetentionSettings` methods to the API ([#119](https://www.github.com/googleapis/python-analytics-admin/issues/119)) ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `GetDisplayVideo360AdvertiserLink`, `ListDisplayVideo360AdvertiserLinks` methods to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `GetDisplayVideo360AdvertiserLinkProposal`, `ListDisplayVideo360AdvertiserLinkProposals` methods to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `LinkProposalInitiatingProduct`, `ServiceLevel`, `DataRetentionSettings` types to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `LinkProposalStatusDetails`, `DisplayVideo360AdvertiserLinkProposal` types to the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* add `service_level` field to `Property` type ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* change `measurement_unit` field to mutable in `CustomMetric` type ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))


### Bug Fixes

* remove `maximum_user_access` field from `FirebaseLink` type ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* remove `MaximumUserAccess` enum from the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* remove `UpdateFirebaseLink` method from the API ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* rename `email_address` field of `GoogleAdsLink` type to `creator_email_address` ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))
* rename `is_deletable` field of `ConversionEvent` type to `deletable` ([2a1c5a0](https://www.github.com/googleapis/python-analytics-admin/commit/2a1c5a098503d075633222a7b926efe2d7026559))

## [0.4.3](https://www.github.com/googleapis/python-analytics-admin/compare/v0.4.2...v0.4.3) (2021-07-27)


### Bug Fixes

* enable self signed jwt for grpc ([#107](https://www.github.com/googleapis/python-analytics-admin/issues/107)) ([dd2235c](https://www.github.com/googleapis/python-analytics-admin/commit/dd2235ca02ff481253dee5e90fa15f6c7bcfc4e8))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#102](https://www.github.com/googleapis/python-analytics-admin/issues/102)) ([99d607c](https://www.github.com/googleapis/python-analytics-admin/commit/99d607c5dc6ea562c4d70cb56c65b01e6c4d9e25))


### Miscellaneous Chores

* release as 0.4.3 ([#108](https://www.github.com/googleapis/python-analytics-admin/issues/108)) ([4dd86a1](https://www.github.com/googleapis/python-analytics-admin/commit/4dd86a139ecfcdab9b1ed847fe7c76fb578ca6af))

## [0.4.2](https://www.github.com/googleapis/python-analytics-admin/compare/v0.4.1...v0.4.2) (2021-07-20)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#101](https://www.github.com/googleapis/python-analytics-admin/issues/101)) ([cde3379](https://www.github.com/googleapis/python-analytics-admin/commit/cde3379e9b40082f69327b46ba0acdabe520c21b))

## [0.4.1](https://www.github.com/googleapis/python-analytics-admin/compare/v0.4.0...v0.4.1) (2021-06-30)


### Bug Fixes

* disable always_use_jwt_access ([5e3df32](https://www.github.com/googleapis/python-analytics-admin/commit/5e3df324aa9d428d63d80816d10ad7d2d7ef41c1))
* disable always_use_jwt_access ([#95](https://www.github.com/googleapis/python-analytics-admin/issues/95)) ([5e3df32](https://www.github.com/googleapis/python-analytics-admin/commit/5e3df324aa9d428d63d80816d10ad7d2d7ef41c1))

## [0.4.0](https://www.github.com/googleapis/python-analytics-admin/compare/v0.3.2...v0.4.0) (2021-06-23)


### Features

* add always_use_jwt_access ([#89](https://www.github.com/googleapis/python-analytics-admin/issues/89)) ([268fdec](https://www.github.com/googleapis/python-analytics-admin/commit/268fdec4dd859a42d1025f94812053311df149ce))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-analytics-admin/issues/1127)) ([#84](https://www.github.com/googleapis/python-analytics-admin/issues/84)) ([6ce863e](https://www.github.com/googleapis/python-analytics-admin/commit/6ce863e147dae3c1da40c27034a0ac42180c6303)), closes [#1126](https://www.github.com/googleapis/python-analytics-admin/issues/1126)

## [0.3.2](https://www.github.com/googleapis/python-analytics-admin/compare/v0.3.1...v0.3.2) (2021-06-16)


### Bug Fixes

* **deps:** add packaging requirement ([#80](https://www.github.com/googleapis/python-analytics-admin/issues/80)) ([6d99bcc](https://www.github.com/googleapis/python-analytics-admin/commit/6d99bcc3e940e4f6bc857e7d4ede53e01537c7ec))

## [0.3.1](https://www.github.com/googleapis/python-analytics-admin/compare/v0.3.0...v0.3.1) (2021-06-16)


### Bug Fixes

* exclude docs and tests from package ([#78](https://www.github.com/googleapis/python-analytics-admin/issues/78)) ([680a695](https://www.github.com/googleapis/python-analytics-admin/commit/680a695e446c979e30542cd4dc563028b126aef5))

## [0.3.0](https://www.github.com/googleapis/python-analytics-admin/compare/v1.0.0...v0.3.0) (2021-06-09)


### Features

* add `ConversionEvent` methods to the API ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `ConversionEvent` type ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `CustomDimension` methods to the API ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `CustomDimension` type ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `CustomMetric` methods to the API ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `CustomMetric` type ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `GetGoogleSignalsSettings`, `UpdateGoogleSignalsSettings` methods to the API ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `GoogleSignalsSettings`  type ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `GoogleSignalsState`, `GoogleSignalsConsent` types ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add `MeasurementProtocolSecret` type ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* add MeasurementProtocolSecret methods to the API ([#71](https://www.github.com/googleapis/python-analytics-admin/issues/71)) ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* extend `ChangeHistoryResourceType` enum ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))


### Bug Fixes

* label `email_address` field of `UserLink` type as immutable ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))
* label `name` field of `UserLink` type as output only ([ab703de](https://www.github.com/googleapis/python-analytics-admin/commit/ab703deccb763ebc3b8be35a09e1cec27b8ef107))


### Documentation

* add Admin API samples for account management methods ([#58](https://www.github.com/googleapis/python-analytics-admin/issues/58)) ([2ecc350](https://www.github.com/googleapis/python-analytics-admin/commit/2ecc350759cfa50f02c0f29f75b647e260cacec0))
* add Admin API samples for account management methods ([#65](https://www.github.com/googleapis/python-analytics-admin/issues/65)) ([a3fecc4](https://www.github.com/googleapis/python-analytics-admin/commit/a3fecc47bb329aeba3706b7d6f0b26196c3a8977))
* add Admin API samples for property stream management methods ([#68](https://www.github.com/googleapis/python-analytics-admin/issues/68)) ([27da97e](https://www.github.com/googleapis/python-analytics-admin/commit/27da97e4574baec81ba3c13be8aece1efa689f75))
* add Admin API samples for property user link management methods ([#67](https://www.github.com/googleapis/python-analytics-admin/issues/67)) ([aa55627](https://www.github.com/googleapis/python-analytics-admin/commit/aa5562777009bbdd21fdc39990b50ac5fb19cc53))
* add samples for Google Analytics property management methods ([#74](https://www.github.com/googleapis/python-analytics-admin/issues/74)) ([bdb85be](https://www.github.com/googleapis/python-analytics-admin/commit/bdb85bee0125db8199d6a2a3cf18fbcbd443070b))


### Miscellaneous Chores

* release 0.3.0 ([#75](https://www.github.com/googleapis/python-analytics-admin/issues/75)) ([243b6c5](https://www.github.com/googleapis/python-analytics-admin/commit/243b6c558078bee738b01220384bc04840d59bbe))

## [0.2.0](https://www.github.com/googleapis/python-analytics-admin/compare/v0.1.0...v0.2.0) (2021-01-20)


### ⚠ BREAKING CHANGES

* `update_mask` field is required for all Update operations
* rename `country_code` field to `region_code` in `Account`
* rename `url_query_parameter` field to `uri_query_parameter` in `EnhancedMeasurementSettings`
* remove `parent` field from `GoogleAdsLink`
* remove unused fields from `EnhancedMeasurementSettings` (#29)

### Features

* add ListAccountSummaries ([#20](https://www.github.com/googleapis/python-analytics-admin/issues/20)) ([04d05d7](https://www.github.com/googleapis/python-analytics-admin/commit/04d05d7436a752dba18cb04d0e6882b1670114d7))
* add pagination support for `ListFirebaseLinks` operation ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))


### Bug Fixes

* `update_mask` field is required for all Update operations ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))
* remove `parent` field from `GoogleAdsLink` ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))
* remove unused fields from `EnhancedMeasurementSettings` ([#29](https://www.github.com/googleapis/python-analytics-admin/issues/29)) ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))
* rename `country_code` field to `region_code` in `Account` ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))
* rename `url_query_parameter` field to `uri_query_parameter` in `EnhancedMeasurementSettings` ([bc756a9](https://www.github.com/googleapis/python-analytics-admin/commit/bc756a9566497ab6ff997d26d7fa35c9a6355ecf))


### Documentation

* added a sample ([#9](https://www.github.com/googleapis/python-analytics-admin/issues/9)) ([60918d8](https://www.github.com/googleapis/python-analytics-admin/commit/60918d8896d37f32a19c3d5724611df5cc4d4619))

## 0.1.0 (2020-07-23)


### Features

* generate v1alpha ([496c679](https://www.github.com/googleapis/python-analytics-admin/commit/496c6792dab14ac680e5b80cc7af1de445023715))
