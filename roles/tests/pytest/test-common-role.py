import subprocess
import pytest

def run_command(cmd):
    """Run a shell command and return stdout as list of lines."""
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout.splitlines()

@pytest.fixture(scope="module")
def ufw_status():
    """Return lines of `ufw status` output."""
    return run_command(["ufw", "status"])

@pytest.fixture(scope="module")
def ufw_verbose():
    """Return lines of `ufw status verbose` output."""
    return run_command(["ufw", "status", "verbose"])

def test_ufw_is_active(ufw_status):
    """Assert UFW is enabled and running."""
    assert any("Status: active" in line for line in ufw_status), "UFW is NOT enabled!"
    print("UFW is enabled and running.")

def test_ufw_default_incoming_deny(ufw_verbose):
    """Assert default incoming policy is deny."""
    assert any("Default: deny (incoming)" in line for line in ufw_verbose), "Default incoming policy is NOT deny!"
    print("Default incoming policy is deny.")

def test_ufw_allows_ssh(ufw_verbose):
    """Assert SSH (port 22) is allowed."""
    assert any("22/tcp" in line for line in ufw_verbose), "SSH (port 22) is NOT allowed in UFW!"
    print("SSH (port 22) is allowed in UFW.")

def test_ufw_allows_http(ufw_verbose):
    """Assert HTTP (port 80) is allowed."""
    assert any("80/tcp" in line for line in ufw_verbose), "HTTP (port 80) is NOT allowed in UFW!"
    print("HTTP (port 80) is allowed in UFW.")

def test_test_complete():
    """Final test message."""
    print("common/main.yml test complete and PASSED.")
