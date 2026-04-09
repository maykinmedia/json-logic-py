"""
Meta module for json-logic.

This module implements the tooling to convert between JSON and python datastructures
for json-logic expressions. The Python datastructures provide richer introspection
potential to (statically) analyze JSON logic expressions.
"""

from . import operations  # noqa
from .base import Operation, register
from .expressions import JSONLogicExpression, JSONLogicExpressionTree

__all__ = [
    "Operation",
    "JSONLogicExpression",
    "JSONLogicExpressionTree",
    "register",
]
