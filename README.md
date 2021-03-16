# timestamp

The `datetime` package of Python cannot deal with negative timestamp. This package can convert between datetime and timestamp safely.

## datetime to timestamp

```python
from datetime import datetime
import timestamp

d = datetime.now()
stamp = timestamp.to_timestamp(d)
```

## timestamp to datetime

```python
import timestamp

stamp = 1615895930
d = timestamp.to_datetime(stamp)
```

## timestamp to midnight

```python
import timestamp

stamp = 1615895930
stamp = timestamp.to_midnight(stamp)
```
