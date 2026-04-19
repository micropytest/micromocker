from unittest import TestCase

from should import should

from micromocker import Mocker
from micromocker._cls import ClsMock

mocker = Mocker()


class TestClsMock(TestCase):
  def test_mocker_fn(self) -> None:
    """Check that mocker.fn() creates a valid mock."""

    should(mocker.cls("sum", result={})).be_instance_of(ClsMock)
