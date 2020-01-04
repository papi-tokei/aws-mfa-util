import os
import json
from aws_mfa_util.util import make_credential_str_list, convert_aws_credential
from aws_mfa_util.credential import AwsCredential


def test_make_credential_str_list():
    response = make_credential_str_list(os.getcwd() + "/tests/sample_credentials")
    require_response = [
        "[testA]\naws_access_key_id=abcde1234\naws_secret_access_key=abcde1234\nregion=ap-northeast-1\nmfa_serial=arn:aws:iam::12345678:mfa/test1\noutput=json\n\n\n",
        "[testB]\naws_access_key_id = abcde1234\naws_secret_access_key = abcde1234\nmfa_serial = arn:aws:iam::12345678:mfa/test2\n\n",
        "[testC]\naws_access_key_id=abcde1234\n",
    ]

    assert response == require_response


def test_convert_aws_credential():
    test_data = [
        "[testA]\naws_access_key_id=abcde1234\naws_secret_access_key=abcde1234\nregion=ap-northeast-1\nmfa_serial=arn:aws:iam::12345678:mfa/test1\noutput=json\n\n\n",
        "[testB]\naws_access_key_id = abcde1234\naws_secret_access_key = abcde1234\nmfa_serial = arn:aws:iam::12345678:mfa/test2\n\n",
        "[testC]\naws_access_key_id=abcde1234\n",
    ]
    require_response = {
        "testA": AwsCredential(
            "testA",
            "abcde1234",
            "abcde1234",
            "ap-northeast-1",
            "arn:aws:iam::12345678:mfa/test1",
            "json",
        ),
        "testB": AwsCredential(
            "testB", "abcde1234", "abcde1234", "", "arn:aws:iam::12345678:mfa/test2", ""
        ),
        "testC": AwsCredential("testC", "abcde1234", "", "", "", ""),
    }
    response = convert_aws_credential(test_data)

    for key in require_response:
        assert require_response[key] == response[key]
    # assert True
    # assert response['testA'] == require_response['testA']
