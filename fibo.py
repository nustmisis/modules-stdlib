def fib(n):
    """Return n-th Fibonacci number, fib(0) = 0."""
    cur, nxt = 0, 1
    for _ in range(n):
        cur, nxt = nxt, cur + nxt
    return cur


def fibs(n):
    """Return first n elements of Fibonacci series."""
    result = [0, 1]
    if n <= 2:
        return result[:n]
    for _ in range(n - 2):
        result.append(result[-1] + result[-2])
    return result


def _say(message):
    print('fibo says: "' + message + '"')


_say("I am imported")


if __name__ == "__main__":
    _say("I am executed")
