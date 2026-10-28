#!/usr/bin/python3
"""Checks every Python file in a folder against the project requirements"""
import ast
import os
import subprocess
import sys

SHEBANG = "#!/usr/bin/python3"
MIN_DOC_WORDS = 3
MIN_DOC_CHARS = 15


def check_doc(node, label, problems):
    """Adds a problem when a node has a missing or too short docstring"""
    doc = ast.get_docstring(node)
    if not doc:
        problems.append("{} has no documentation".format(label))
    elif len(doc.split()) < MIN_DOC_WORDS or len(doc) < MIN_DOC_CHARS:
        problems.append("{} documentation is too short".format(label))


def check_style(path, problems):
    """Runs pycodestyle on a file and records any style errors."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pycodestyle", path],
            capture_output=True, text=True)
    except OSError as err:
        problems.append("could not run pycodestyle: {}".format(err))
        return
    if "No module named pycodestyle" in result.stderr:
        problems.append("pycodestyle is not installed (pip3 install "
                        "pycodestyle)")
    elif result.returncode != 0:
        for line in result.stdout.strip().splitlines():
            problems.append("pycodestyle: {}".format(line))


def check_file(path):
    """Returns the list of problems found in one Python file."""
    problems = []
    with open(path, "rb") as f:
        data = f.read()

    first_line = data.split(b"\n", 1)[0].decode("utf-8", "replace")
    if first_line != SHEBANG:
        problems.append("first line must be exactly {}".format(SHEBANG))
    if not data.endswith(b"\n"):
        problems.append("file does not end with a new line")
    if not os.access(path, os.X_OK):
        problems.append("file is not executable (chmod +x)")

    try:
        tree = ast.parse(data.decode("utf-8"), filename=path)
    except SyntaxError as err:
        problems.append("syntax error: {}".format(err))
        return problems

    check_doc(tree, "module", problems)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            check_doc(node, "class {}".format(node.name), problems)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            check_doc(node, "function {}".format(node.name), problems)
        elif isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Attribute) and func.attr == "execute":
                problems.append(
                    "line {}: execute is not allowed".format(node.lineno))

    check_style(path, problems)
    return problems


def main():
    """Checks all .py files in the given folder and prints a summary"""
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    failed = {}

    readme = os.path.join(folder, "README.md")
    if not os.path.isfile(readme):
        failed["README.md"] = ["README.md is missing at the project root"]

    names = sorted(n for n in os.listdir(folder) if n.endswith(".py"))
    if not names:
        print("No .py files found in {}".format(folder))
    for name in names:
        problems = check_file(os.path.join(folder, name))
        if problems:
            failed[name] = problems
            print("[FAIL] {}".format(name))
        else:
            print("[ OK ] {}".format(name))

    if failed:
        print("\n{} item(s) failed:\n".format(len(failed)))
        for name, problems in failed.items():
            print(name)
            for problem in problems:
                print("  - {}".format(problem))
        sys.exit(1)
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
