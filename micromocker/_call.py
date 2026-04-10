TYPE_CHECKING = False
if TYPE_CHECKING:
  from typing import Any


class call:
  """Information of a function call.

  Attributes:
    args: Positional arguments.
    kwargs: Named arguments.
    returned: Value returned.
    raised: Value raised.
  """

  def __init__(
    self,
    args: tuple = (),
    kwargs: dict[str, Any] | None = None,
    *,
    returned: Any = None,
    raised: Any = None,
  ):
    self.args = args
    self.kwargs = kwargs if kwargs is not None else {}
    self.returned = returned
    self.raised = raised

  def __eq__(self, o: Any) -> bool:
    return (
      self.args == o.args
      and self.kwargs == o.kwargs
      and self.returned == o.returned
      and self.raised == o.raised
    )

  def __repr__(self) -> str:
    return (
      f"call(args={self.args}, kwargs={self.kwargs}, "
      f"returned={self.returned}, raised={self.raised})"
    )


class calls(list):
  """A list of mock calls."""

  def __init__(self, mock=None):
    super().__init__()

    if mock is not None and hasattr(mock, "_mock_calls"):
      for call in mock._mock_calls:
        self.append(call)

  def returned(self, value: Any) -> bool:
    """Checks whether the list contains some call returning a given value."""

    for call in self:
      if call.returned == value:
        return True

    return False

  def raised(self, value: Any) -> bool:
    """Checks whether the list contains some call raising a given error."""

    for call in self:
      if call.raised == value:
        return True

    return False
