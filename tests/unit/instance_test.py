from unittest import TestCase

from should import should

from micromocker import Mocker, calls

mocker = Mocker()


class Point2d: ...


class TestInstanceMock(TestCase):
  def test_mocked_attrs(self) -> None:
    """Check that the mocker works ok with attributes."""

    # (1) act
    out = mocker.mock(attrs=dict(x=12, y=34))

    # (2) assessment
    should(out.x).be_eq(12)
    should(out.y).be_eq(34)
    should(lambda: out.z).throw(AttributeError, match="z")

  def test_returns_default_attr(self) -> None:
    """Check that the mocker works ok and returns the default attribute."""

    # (1) act
    out = mocker.mock(attrs={"x": 12, "*": 34})

    # (2) assessment
    should(out.x).be_eq(12)
    should(out.y).be_eq(34)

  def test_mocked_meths(self) -> None:
    """Check that the mocker works ok with methods."""

    # (1) act
    out = mocker.mock(meths=dict(x=lambda: 12, y=lambda: 34))

    # (2) assessment
    should(out.x()).be_eq(12)
    should(out.y()).be_eq(34)
    should(lambda: out.z()).throw(AttributeError, match="z")

  def test_returns_default_meth(self) -> None:
    """Check that the mocker works ok and returns the default method."""

    # (1) act
    out = mocker.mock(meths={"x": lambda: 12, "*": lambda: 34})

    # (2) assessment
    should(out.x()).be_eq(12)
    should(out.y()).be_eq(34)
