def cache_v2(filename: str, use_kwargs: bool = False):
    def decorator(func):
        cache_dict = {}

        # пробуем загрузить кеш из файла
        try:
            with open(filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if ' : ' in line:
                        k_str, v_str = line.split(' : ', 1)
                        key = tuple(eval(k_str))  # строку обратно в tuple
                        val = eval(v_str)         # строку обратно в значение
                        cache_dict[key] = val
        except FileNotFoundError:
            pass

        def wrapper(*args, **kwargs):
            if use_kwargs:
                key = tuple(sorted(kwargs.items()))
            else:
                key = args

            if key in cache_dict:
                return cache_dict[key]

            result = func(*args, **kwargs)
            cache_dict[key] = result

            # перезаписываем весь файл
            with open(filename, 'w') as f:
                for k, v in cache_dict.items():
                    f.write(f"{k} : {v}\n")

            return result

        return wrapper
    return decorator


@cache_v2(filename="fact_cache.txt", use_kwargs=False)
def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n - 1)


if __name__ == "__main__":
    for i in range(0, 100):
        fact(i)
    print(fact(10))
