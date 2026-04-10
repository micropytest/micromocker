from ._mock import Mock

TYPE_CHECKING = False
if TYPE_CHECKING:
  from typing import Any, Callable, Literal


class InstanceMock(Mock):
  """A mock for simulating an instance.

  Attributes:
    _mock_attrs: Mocked attributes.
    _mock_meths: Mocker methods.
  """

  def __init__(
    self,
    name: str,
    attrs: dict[str, Any] = {"*": None},
    meths: dict[str, Callable] = {"*": lambda: None},
  ):
    super().__init__(name)

    self._mock_attrs = attrs
    self._mock_meths = meths

  def __getattr__(self, name: str) -> Any:
    # (1) get the value
    if name in (attrs := self._mock_attrs):
      v = attrs[name]
    elif name in (meths := self._mock_meths):
      v = meths[name]
    elif "*" in attrs:
      v = attrs["*"]
    elif "*" in meths:
      v = meths["*"]
    else:
      raise AttributeError(name)

    # (2) return the value
    return v
