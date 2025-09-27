from typing import Any


class InitLoggerMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        cls_name = self.__class__.__name__
        params: list[str] = []
        if args:
            params.extend(repr(a) for a in args)
        if kwargs:
            params.extend(f"{k}={v!r}" for k, v in kwargs.items() if k != "__class__")
        print(f"{cls_name} создан с параметрами: {', '.join(params)}")
