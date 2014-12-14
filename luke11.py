def sumOfPrimes(N):
        isPrime, primes = (N + 1)*[True], []
        for i in xrange(3, N + 1, 2):
                if not isPrime[i]:
                        continue
                primes.append(i)
                for j in xrange(i*i, N + 1, i):
                        isPrime[j] = False
        s = [(sum(primes[0:7]),   0, 0,   7), (sum(primes[0:17]),  0, 1,  17), (sum(primes[0:41]),  0, 2,  41), (sum(primes[0:541]), 0, 3, 541)]
        while True:
                allEqual = True
                for a in s:
                        if a[0] != s[0][0]:
                                allEqual = False
                                break
                if allEqual and s[0][0] <= N and isPrime[s[0][0]]: return s[0][0]
                m = min(s)
                if m[0] > N or m[3] == len(primes)-1: return None
                s[m[2]] = (m[0] - primes[m[1]] + primes[m[1] + m[3]], m[1] + 1, m[2], m[3])
 
print sumOfPrimes(10000000)