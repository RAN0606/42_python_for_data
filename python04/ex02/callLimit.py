def callLimit(limit: int):
    """Takes a limit as input and returns a decorator that restricts
    the number of times a decorated function can be called."""
    count = 0

    def callLimiter(function):
        """
        inner function is used to wrap around the target function.
        It tracks the number of times the target function is called,
        and limit the times of excution
        """
        def limit_function(*args: any, **kwds: any):
            try:
                nonlocal count
                if count < limit:
                    count += 1
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)
        return limit_function

    return callLimiter
