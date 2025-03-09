import sys
import os
import pytest
from pathlib import Path

# Add the parent directory to sys.path to allow importing the package
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))