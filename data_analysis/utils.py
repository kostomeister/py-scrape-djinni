import ast


def parse_technologies(x):
    try:
        return ast.literal_eval(x)
    except (SyntaxError, ValueError):
        return []
