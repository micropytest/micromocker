from typing import overload

from ._fn import FnMock
from ._instance import InstanceMock

TYPE_CHECKING = False
if TYPE_CHECKING:
  from typing import Any, Callable, Iterable


class Mocker:
  """An object for creating mocks."""

  def mock(
    self,
    attrs: dict[str, Any] = {},
    meths: dict[str, Callable] = {},
  ) -> InstanceMock:
    """Returns a mock for simulating an instance."""

    return InstanceMock("mock", attrs, meths)

  def fn(
    self,
    name="mock",
    *,
    result: Any = None,
    results: Iterable[Any] | None = None,
  ) -> FnMock:
    """Returns a mock for simulating a function."""

    return FnMock(name, result, results)
