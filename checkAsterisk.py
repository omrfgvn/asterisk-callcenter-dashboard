import subprocess

def get_status_peers():
    try:
        result = subprocess.run(
            ['asterisk', '-rx', 'sip show peers'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except Exception as e:
        return str(e)

