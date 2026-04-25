import sys

def retry(count: int = 5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = count
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    attempts -= 1
                    continue
                except OSError:
                    attempts -= 1
                    print(f"{func.__name__} raise OsError exception.", file=sys.stdout)
                    continue
            return func(*args, **kwargs)
        return wrapper
    return decorator
