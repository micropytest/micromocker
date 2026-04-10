from abc import ABC


class Mock(ABC):
  """An object for simulating another.

  Attributes:
    _mock_name: Mock name such as, for example, the function name.
  """

  def __init__(self, name: str):
    self._mock_name = name
