# *micro:Mocker*

A lightweight lib for mocking things on **micro:Pytest** and **MicroPython**.


## Install

```bash
micropython -m mip install github:micropytest/micromocker
```


## Usage

```python
from micromocker import Mocker

mocker = Mocker()
```


## Creating a function mock

Creation:

```python
fn = mocker.fn("sum", result=4)
fn(12, 34)  # returns 4
```

Prototype:

```python
def fn(
  self,
  name="mock",
  *,
  result: Any = None,
  results: Iterable[Any] | None = None
) -> FnMock:
  """Creates a function mock.

  Args:
    name: Function mock name.
    result: Value to return in every call.
    results: Values to return. First call returns index 0; and so on.
  
  Returns:
    Function mock to use.
  
  Raises:
    TypeError: If result and results set. Only one allowed.
  """
```

If a result value is an ***`Exception`*** instance, the call will raise this error.

### Accessing to the function mock calls

For getting the info of the calls performed on the function mock, we have to use **`calls()`**.
Example:

```python
from micromocker import Mocker, call, calls

# ...

should(calls(fn)).have_len(2)
should(calls(fn)).be_eq(
  [
    call((1, 2), returned=4),
    call((3, 4), returned=8)
  ]
)
```

**`calls`** is a ***`list[call]`***.
For creating a ***`call`*** in an assertion, we must use its constructor:

```python
def __init__(
  self,
  args: tuple = (),
  kwargs: dict = {},
  returned: Any = None,
  raised: Any = None
):
  """
  Args:
    args: Positional arguments passed to the call.
    kwargs: Named arguments passed to the call.
    returned: Value returned by the function mock in the call.
    raised: Value raised by the function mock in the call.
  """
```

**`calls`** contains the following methods:

```python
def returned(self, value: Any) -> bool:
  """Checks whether some call returned a given value."""

def raised(self, value: Any) -> bool:
  """Checks whether some call raised a given value."""
```


## Creating an instance mock

Creation:

```python
p = mocker.mock(
  attrs={"x": 12, "y": 34},
  meths={"xy": lambda: "1234"},
)

print(i.x)      # returns 12
print(i.y)      # returns 34
print(i.z)      # raises AttributeError
print(i.xy())   # returns "1234"
```

Prototype:

```python
def mock(
  self,
  attrs: dict[str, Any] = {},
  meths: dict[str, Callable] = {},
) -> InstanceMock:
  """Creates an instance mock.

  Args:
    attrs: Mocked attributes.
    meths: Mocked methods.
  
  Returns:
    Mocked object to use.
  """
```

When **`"*"`** used as key, the mock returns the given value for the unknown members.
The mock searches a member as follows:

01. Search in **`attrs`**, without considering **`*`**.

02. Search in **`meths`**, without considering **`*`**.

03. Search if **`attrs`** defines **`*`**.

04. Search if **`meths`** defines **`*`**.

05. ***`AttributeError`*** raised if not found.

Example:

```python
point = mocker.mock(attrs={"x": 12, "*": 34})
```


## Creating a class mock

Creation:

```python
C = mocker.cls("ClassName", result=mocker.mock())
c = C()
```
