from pathlib import Path
import argparse
import ast
import json
import sys
import nbformat
ROOT = Path(__file__).resolve().parents[1]
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todo-only', action='store_true')
    args = parser.parse_args()
    meta = json.loads((ROOT/'docs/project_manifest.json').read_text(encoding='utf-8'))
    assert meta['group_size'] == 6 and meta['dataset'] == 'METR-LA'
    assert set(meta['requirements']) == {f'T{i:02d}' for i in range(1,9)}
    owners = set()
    for relative in meta['notebooks']:
        nb = nbformat.read(ROOT/relative, as_version=4)
        nbformat.validate(nb)
        if 'owner' in nb.metadata.lab4:
            owners.add(nb.metadata.lab4.owner)
        for c in nb.cells:
            if c.cell_type == 'code':
                parsed = ast.parse(c.source)
                if args.todo_only:
                    assert not parsed.body and not c.outputs and c.execution_count is None, relative
                assert not any(o.output_type == 'error' for o in c.outputs), relative
        print('PASS', relative)
    assert owners == {f'TV{i}' for i in range(1,7)}
    print(f'LAB4_OK: notebooks={len(meta["notebooks"])}; dataset=METR-LA; owners=6; TODO_only={args.todo_only}')
    return 0
if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (AssertionError, ValueError, OSError) as e:
        print('FAIL',e,file=sys.stderr)
        raise SystemExit(1)
