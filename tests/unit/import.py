from unittest import TestCase

from should import should

from micromocker import Mocker, call, calls


class TestImport(TestCase):
  def test_imports(self) -> None:
    """Check that is imported."""

    should(Mocker).be_callable()
    should(call).be_callable()
    should(calls).be_callable()
