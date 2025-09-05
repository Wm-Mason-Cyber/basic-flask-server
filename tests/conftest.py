import os
import shutil
import subprocess
import time
import pytest


def docker_available():
    try:
        subprocess.run(["docker", "ps"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False


@pytest.fixture(scope='session')
def docker_skip(request):
    if not docker_available():
        pytest.skip("Docker not available — skipping integration fixtures")
