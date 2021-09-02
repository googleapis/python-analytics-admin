TEST_CONFIG_OVERRIDE = {
    "gcloud_project_env": "BUILD_SPECIFIC_GCLOUD_PROJECT",
    # 'gcloud_project_env': 'BUILD_SPECIFIC_GCLOUD_PROJECT',
    # A dictionary you want to inject into your test. Don't put any
    # secrets here. These values will override predefined values.
    "envs": {
        "GA_TEST_PROPERTY_ID": "276206997",
        "GA_TEST_ACCOUNT_ID": "199820965",
        "GA_TEST_USER_LINK_ID": "123",
        "GA_TEST_ANDROID_APP_DATA_STREAM_ID": "123",
        "GA_TEST_IOS_APP_DATA_STREAM_ID": "123",
        "GA_TEST_WEB_DATA_STREAM_ID": "123",
    },
}
