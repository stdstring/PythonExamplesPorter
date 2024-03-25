import collections
import pathlib
import sys
import typing


TEST_HEADER = "======================================================================"
SKIPPED_ERROR = "NotImplementedError:"


def filter_test_output(source: str, dest: str) -> None:
    source_path = pathlib.Path(source)
    if not source_path.exists():
        raise ValueError("Bad source")
    source_text = source_path.read_text(encoding="utf-8")
    source_lines = list(map(lambda line: line.strip(), source_text.split("\n")))
    dest_lines = []
    skipped_error_reasons = []
    index = 0
    total_errors = 0
    while index < len(source_lines):
        current_line = source_lines[index]
        if current_line.startswith(TEST_HEADER):
            portion = process_portion(source_lines, index, skipped_error_reasons)
            index = portion.Index
            dest_lines.extend(portion.Data)
            if len(portion.Data) > 0:
                dest_lines.append("")
        total_errors += 1
        index += 1
    dest_text = "\r\n".join(dest_lines)
    dest_text += "\r\nNotImplementedError reasons:\r\n"
    reasons_lines = map(lambda entry: f"{entry[0]} - {entry[1]} times", collections.Counter(skipped_error_reasons).most_common())
    dest_text += "\r\n".join(reasons_lines)
    not_implemented_errors = len(skipped_error_reasons)
    dest_text += f"\r\n\r\nTotal errors = {total_errors}, NotImplemented errors = {not_implemented_errors}, other errors = {total_errors - not_implemented_errors}"
    dest_path = pathlib.Path(dest)
    dest_path.write_text(dest_text)


class Portion(typing.NamedTuple):

    Index: int
    Data: typing.List[str]


def process_portion(lines: typing.List[str], index: int, skipped_error_reasons: typing.List[str]) -> Portion:
    portion = []
    skip_portion = False
    while (index < len(lines)) and (len(lines[index]) > 0):
        if lines[index].startswith(SKIPPED_ERROR):
            skipped_error_reason = lines[index].removeprefix(SKIPPED_ERROR).strip()
            skipped_error_reasons.append(skipped_error_reason)
            skip_portion = True
        portion.append(lines[index])
        index += 1
    return Portion(index, [] if skip_portion else portion)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ValueError("Bad usage of CLI")
    filter_test_output(sys.argv[1], sys.argv[2])