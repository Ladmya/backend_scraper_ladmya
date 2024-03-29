import pytest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from main import app

@pytest.fixture
async def app():

    yield app