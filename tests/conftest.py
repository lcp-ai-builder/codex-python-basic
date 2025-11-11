"""Pytest configuration helpers.

中文说明：将项目根目录加入 sys.path，确保 `import src` 在任何执行路径下都可用。
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
