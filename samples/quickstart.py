# This application demonstrates the usage of the Analytics Admin API using
# service account credentials. For more information on service accounts, see
#
# https://cloud.google.com/iam/docs/understanding-service-accounts
#
# The following document provides instructions on setting service account
# credentials for your application:
#
#   https://cloud.google.com/docs/authentication/production
#
# In a nutshell, you need to:
# 1. Create a service account and download the key JSON file.
#
# https://cloud.google.com/docs/authentication/production#creating_a_service_account
#
# 2. Provide service account credentials using one of the following options:
# - set the GOOGLE_APPLICATION_CREDENTIALS environment variable, the API
# client will use the value of this variable to find the service account key
# JSON file.
#
# https://cloud.google.com/docs/authentication/production#setting_the_environment_variable
#
# OR
# - manually pass the path to the service account key JSON file to the API client
# by specifying the keyFilename parameter in the constructor:
# https://cloud.google.com/docs/authentication/production#passing_the_path_to_the_service_account_key_in_code

# To install the latest published package dependency, execute the following:
#   pip install google-analytics-admin
from google.analytics.admin import AnalyticsAdminServiceClient


def main():
  # Using a default constructor instructs the client to use the credentials
  # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
  client = AnalyticsAdminServiceClient()

  # Displays the configuration information for all Google Analytics accounts
  # available to the authenticated user.
  for account in client.list_accounts():
    print(account)


if __name__ == "__main__":
  main()
