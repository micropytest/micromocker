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
    attrs: dict[str, Any] | None = None,
    meths: dict[str, Callable] | None = None,
  ) -> InstanceMock:
    """Returns a mock for simulating an instance."""

    return InstanceMock(
      "mock",
      attrs if attrs is not None else {},
      meths if meths is not None else {},
    )

  def fn(
    self,
    name="mock",
    *,
    result: Any = None,
    results: Iterable[Any] | None = None,
  ) -> FnMock:
    """Returns a mock for simulating a function."""

    return FnMock(name, result, results)
