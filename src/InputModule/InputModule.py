import ast
import operator as op
import re


def normalize_german_expr(expr: str) -> str:
    """
    Converts numbers from German notation to standard notation.
    For example, '1.000,50' becomes '1000.50'.
    """
    # Pattern to match German-formatted numbers:
    # It matches numbers with optional thousands separators and an optional decimal part.
    number_pattern = re.compile(r"\d{1,3}(?:\.\d{3})*(?:,\d+)?|\d+(?:,\d+)?")

    def replacer(match: re.Match) -> str:
        number_str = match.group(0)
        # Remove thousands separators (dots) and replace comma with dot.
        normalized = number_str.replace(".", "").replace(",", ".")
        return normalized

    return number_pattern.sub(replacer, expr)


# Mapping of AST operators to functions.
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}


def calc(expr: str) -> float:
    """
    German-friendly calculator.
    - Normalizes German number notation to standard notation.
    - Converts '^' to '**' for power operations.
    - Evaluates expressions with correct operator precedence.
    - Raises ZeroDivisionError on division by zero.
    """
    # Normalize the expression to standard numeric notation.
    normalized_expr = normalize_german_expr(expr)
    # Replace '^' with Python's power operator '**'
    normalized_expr = normalized_expr.replace("^", "**")

    def eval_node(node):
        if isinstance(node, ast.Constant):  # For Python 3.8+ numbers.
            return node.value
        elif isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            operator_func = operators.get(type(node.op))
            if operator_func is None:
                raise TypeError(f"Unsupported operator: {node.op}")
            return operator_func(left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = eval_node(node.operand)
            operator_func = operators.get(type(node.op))
            if operator_func is None:
                raise TypeError(f"Unsupported operator: {node.op}")
            return operator_func(operand)
        else:
            raise TypeError(f"Unsupported expression: {node}")

    parsed_expr = ast.parse(normalized_expr, mode="eval")
    return eval_node(parsed_expr.body)
