import pytest
from src.string_utils import StringUtils
from  contextlib import nullcontext

class TestStringUtils:
    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("abs", nullcontext()),
            (124, pytest.raises(TypeError)),
            (None, pytest.raises(TypeError)),
            ("123", nullcontext())

        ]
    )
    def test_reverse_string_errors(self, input_str, expected):
        utils = StringUtils()
        with expected:
            utils.reverse_string(input_str)

    # def test_reverse_string(self, input_str, expected):
    #     utils = StringUtils()
    #     assert utils.reverse_string(input_str) == expected


    @pytest.mark.parametrize(
        "full_name, expected",
        [
            ("Лапшин Александр", "ЛА"),
            ("Иван Иванов", "ИИ"),
            ("", pytest.raises(ValueError)),
            (124, pytest.raises(TypeError)),
            (None, pytest.raises(TypeError))
        ]
    )
    def test_get_initials(self, full_name, expected):
        utils = StringUtils()
        if isinstance(expected, str):
            assert utils.get_initials(full_name) == expected
        else:
            with expected:
                utils.get_initials(full_name)