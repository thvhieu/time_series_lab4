from pathlib import Path
import hashlib
import json
import h5py
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
def main():
    meta = json.loads((ROOT/'data/traffic/manifest.json').read_text(encoding='utf-8'))
    path = ROOT/meta['path']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == meta['sha256'], 'Raw hash mismatch'
    with h5py.File(path,'r') as f:
        values = f['df/block0_values'][:]
        times = f['df/axis1'][:]
        sensors = f['df/axis0'][:]
        assert values.shape == tuple(meta['shape']) == (34272,207)
        assert len(sensors) == 207 and len(set(sensors)) == 207
        assert len(times) == 34272 and np.all(np.diff(times) == 300_000_000_000)
        assert np.isfinite(values).all()
        assert int(np.count_nonzero(values == 0)) == meta['zero_values']
    print('DATA_OK: METR-LA.h5; shape=34272x207; step=5min; hash=PASS; original_bytes=KEPT')
if __name__ == '__main__':
    main()
