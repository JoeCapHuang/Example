import pytest


def mobile():
    return pytest.mark.MOBILE


def tablet():
    return pytest.mark.TABLET


def android():
    return pytest.mark.ANDROID


def ios():
    return pytest.mark.IOS
