from ._call import call, calls
from ._mock import Mock

TYPE_CHECKING = False
if TYPE_CHECKING:
  from typing import Any, Iterable


class FnMock(Mock):
  """A mock for simulating a function.
  If result or results contains an error, this will be raised.

  Attributes:
    _result: Value to return in every call.
    _results: Values to return. For the 1st call, the value with index 0; and so on.
    calls: Calls performed on the mock.

  Raises:
    TypeError: If result and results configured at the same time.
  """

  def __init__(self, name: str, result: Any = None, results: Iterable[Any] | None = None):
    # (1) pre
    if result is not None and results is not None:
      raise TypeError("'result' and 'results' can't be set at the same time. Only one allowed.")

    # (2) initialize
    super().__init__(name)

    self.__name__ = name
    self._mock_result = result
    self._mock_results = list(results) if results is not None else None
    self._mock_calls = calls()

  def __call__(self, *args, **kwargs) -> Any:
    # (1) determine value to return
    if (r := self._mock_results) is not None:
      value = r[len(self._mock_calls)]
    else:
      value = self._mock_result

    # (2) return value or raise error
    if isinstance(value, Exception):
      self._mock_calls.append(call(args, kwargs, raised=value))
      raise value
    else:
      self._mock_calls.append(call(args, kwargs, returned=value))
      return value
