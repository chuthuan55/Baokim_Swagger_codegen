# coding: utf-8

"""
    Collection payments

    <img src=\"https://devtest.baokim.vn/collection/core_ctt/image/Picture1.png\" class=\"image-collection-payment\" /> <p><strong>Note:</strong></p> <p>+ In case PARTNER want to use collect via Virtual Account, PARTNER will need to buid:</p> <p style=\"padding-left: 50px;\">     - <a href=\"#operations-Virtual_Account_4\\.0-8442c69ffbaf4b3677a52fa3ebcef6d4\">Register virtual account</a> <br>     - <a href=\"#operations-Virtual_Account_4\\.0-1796c61005edee3976097a607fe9dbaa\">Update virtual account informations</a> <br>     - <a href=\"#operations-tag-Notice_of_collection_transaction\">Notice of collection transaction</a> <br> </p>  # noqa: E501

    OpenAPI spec version: 2.3 and 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Collection payments",
    author_email="",
    url="",
    keywords=["Swagger", "Collection payments"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    &lt;img src&#x3D;\&quot;https://devtest.baokim.vn/collection/core_ctt/image/Picture1.png\&quot; class&#x3D;\&quot;image-collection-payment\&quot; /&gt; &lt;p&gt;&lt;strong&gt;Note:&lt;/strong&gt;&lt;/p&gt; &lt;p&gt;+ In case PARTNER want to use collect via Virtual Account, PARTNER will need to buid:&lt;/p&gt; &lt;p style&#x3D;\&quot;padding-left: 50px;\&quot;&gt;     - &lt;a href&#x3D;\&quot;#operations-Virtual_Account_4\\.0-8442c69ffbaf4b3677a52fa3ebcef6d4\&quot;&gt;Register virtual account&lt;/a&gt; &lt;br&gt;     - &lt;a href&#x3D;\&quot;#operations-Virtual_Account_4\\.0-1796c61005edee3976097a607fe9dbaa\&quot;&gt;Update virtual account informations&lt;/a&gt; &lt;br&gt;     - &lt;a href&#x3D;\&quot;#operations-tag-Notice_of_collection_transaction\&quot;&gt;Notice of collection transaction&lt;/a&gt; &lt;br&gt; &lt;/p&gt;  # noqa: E501
    """
)
