class fibonacci:

    def __init__(self):
        self.d = dict()
        self.d[0] = 0
        self.d[1] = 1
        self.d[2] = 1

    def fib_recursive(self, n):

        if n <= 2:
            f = 1
        else:
            f = self.fib_recursive(n-1) + self.fib_recursive(n-2)

        return f

    def fib_memoized_DP(self, n):

        if n in self.d:
            return self.d[n]

        if n <= 2:
            f = 1
        else:
            f = self.fib_memoized_DP(n-1) + self.fib_memoized_DP(n-2)
        self.d[n] = f
        return f

    def fib_bottomup_DP(self, n):
        for i in range(2,n+1):
            if i <=2:
                f = 1
            else:
                f = self.d[i-1] + self.d[i-2]
            self.d[n] = f
        return self.d[n]



o = fibonacci()
x = o.fib_recursive(6)
print x
x = o.fib_memoized_DP(6)
print x
x = o.fib_bottomup_DP(6)
print x
