from unittest import TestCase

from should import should  # type: ignore

from micromocker import Mocker, call, calls
from micromocker._fn import FnMock

mocker = Mocker()


class TestFnMock(TestCase):
  def test_mocker_fn(self) -> None:
    """Check that mocker.fn() creates a valid mock."""

    # (1) act
    out = mocker.fn("sum", result=4)

    # (2) assessment
    should(out).be_instance_of(FnMock)
    should(out._mock_name).be_eq("sum")
    should(out._mock_result).be_eq(4)
    should(out._mock_results).be_none()

  def test_mocker_fn_raises_error_if_result_and_results(self) -> None:
    """Check that mocker.fn() creates a valid mock."""

    should(lambda: mocker.fn("sum", result=4, results=[4])).throw(
      TypeError,
      match="'result' and 'results' can't be set at the same time. Only one allowed.",
    )

  def test_mocker_fn_raises_index_error_if_unavailable_result(self) -> None:
    """Check that mocker.fn() raises IndexError if results ended."""

    should(lambda: mocker.fn("sum", results=[])()).throw(
      IndexError,
      match="Mock 'sum' called more times than results configured.",
    )

  def test_fn_mock_calls(self) -> None:
    """Check that the fn mock works ok when called."""

    # (1) arrange
    fn = mocker.fn("sum", results=[4, 8, 12])

    # (2) act
    out = [fn(1, 2), fn(3, 4)]

    # (3) assessment
    should(out).be_eq([4, 8])

    out = calls(fn)
    should(out).be_eq([call((1, 2), returned=4), call((3, 4), returned=8)])
    should(out.returned(8)).be_true()

  def test_fn_mock_call_raises_error(self) -> None:
    """Check that the fn mock raises error when error set as result."""

    # (1) arrange
    fn = mocker.fn("throw", result=TypeError("Invalid type."))

    # (2) act and assert
    should(lambda: fn()).throw(TypeError, match="Invalid type.")
    should(calls(fn)).have_len(1)
