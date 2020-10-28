class e(Exception):
    "n and p should be non-negative"


class Calculator():
    def power(self, n, p):
        try:
            if n | p < 0:
                raise e

            else:
                return (n ** p)
        except e:
            return ("n and p should be non-negative")