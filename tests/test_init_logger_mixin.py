from src.product.init_logger_mixin import InitLoggerMixin


def test_init_logger_args_only(capsys):
    # Тест на содержание args
    class OnlyArgs(InitLoggerMixin):
        def __init__(self, x, y):
            super().__init__(x, y)

    OnlyArgs(5, 6)
    captured = capsys.readouterr()
    assert "5" in captured.out
    assert "6" in captured.out


def test_init_logger_kwargs_only(capsys):
    # Тест на содержание kwargs
    class OnlyKwargs(InitLoggerMixin):
        def __init__(self, x=1, y=2):
            super().__init__(x=x, y=y)

    OnlyKwargs(x=7, y=8)
    captured = capsys.readouterr()
    assert "x=7" in captured.out
    assert "y=8" in captured.out


def test_init_logger_mixin_prints_params(capsys):
    # Тест на вывод имени класса и всех параметры
    class ExampleClass(InitLoggerMixin):
        def __init__(self, a, b, c=None):
            super().__init__(a, b, c=c)
            self.a = a
            self.b = b
            self.c = c

    obj = ExampleClass(1, "two", c=3)
    captured = capsys.readouterr()
    assert "ExampleClass создан с параметрами:" in captured.out
    assert "1" in captured.out
    assert "two" in captured.out
    assert "c=3" in captured.out
