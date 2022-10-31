import socket


def get_local_ip():
    """Получаем локальный IP"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    ans = sock.getsockname()
    sock.close()
    return ans[0]
