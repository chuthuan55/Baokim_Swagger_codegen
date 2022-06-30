# coding: utf-8

# flake8: noqa

"""
    Collection payments

    <img src=\"https://devtest.baokim.vn/collection/core_ctt/image/Picture1.png\" class=\"image-collection-payment\" /> <p><strong>Note:</strong></p> <p>+ In case PARTNER want to use collect via Virtual Account, PARTNER will need to buid:</p> <p style=\"padding-left: 50px;\">     - <a href=\"#operations-Virtual_Account_4\\.0-8442c69ffbaf4b3677a52fa3ebcef6d4\">Register virtual account</a> <br>     - <a href=\"#operations-Virtual_Account_4\\.0-1796c61005edee3976097a607fe9dbaa\">Update virtual account informations</a> <br>     - <a href=\"#operations-tag-Notice_of_collection_transaction\">Notice of collection transaction</a> <br> </p>  # noqa: E501

    OpenAPI spec version: 2.3 and 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.notice_of_collection_transaction_api import NoticeOfCollectionTransactionApi
from swagger_client.api.response_code_api import ResponseCodeApi
from swagger_client.api.virtual_account_4_0_api import VirtualAccount40Api
from swagger_client.api.virtual_account_version_2_3_api import VirtualAccountVersion23Api
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.body import Body
from swagger_client.models.inline_response101 import InlineResponse101
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.sandbox_collection_body import SandboxCollectionBody
from swagger_client.models.v4_create_body import V4CreateBody
from swagger_client.models.v4_update_body import V4UpdateBody