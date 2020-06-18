import pytest

@pytest.mark.xfail(strict=True)# strict=True делает так что тест который планировался не работать, как заранее ясный,
# что там баг, должен пометиться как сфейлевшийся.
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False