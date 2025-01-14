from hamcrest import assert_that
from allure_commons_test.report import has_test_case


def test_unicode_function_name(executed_docstring_source):
    """
    >>> def test_unicode_func_déjà_vu():
    ...     pass
    """

    assert_that(executed_docstring_source.allure_report,
                has_test_case("test_unicode_func_déjà_vu")
                )


def test_unicode_method_name(executed_docstring_source):
    """
    >>> class TestCase:
    ...     def test_unicode_method_例子(self):
    ...         pass
    """

    assert_that(executed_docstring_source.allure_report,
                has_test_case("test_unicode_method_例子")
                )


def test_unicode_class_name(executed_docstring_source):
    """
    >>> class TestCaseПервый:
    ...     def test_method(self):
    ...         pass
    """

    assert_that(executed_docstring_source.allure_report,
                has_test_case("TestCaseПервый#test_method")
                )
