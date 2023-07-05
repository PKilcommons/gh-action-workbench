import time

import pytest
from filelock import FileLock


def test_lock(worker_id: str, tmp_path_factory: pytest.TempPathFactory):
    container_name = "test-container"
    file = tmp_path_factory.getbasetemp().parent / f"hivo-docker-{container_name}.lock"
    lock = FileLock(file, timeout=10)
    with lock:
        print(f"Acquired by {worker_id}")
        time.sleep(5)
    print(f"Released by {worker_id}")


def test_lock2(worker_id: str, tmp_path_factory: pytest.TempPathFactory):
    container_name = "test-container"
    file = tmp_path_factory.getbasetemp().parent / f"hivo-docker-{container_name}.lock"
    lock = FileLock(file, timeout=10)
    with lock:
        print(f"Acquired by {worker_id}")
        time.sleep(5)
    print(f"Released by {worker_id}")
