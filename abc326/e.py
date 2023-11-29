def expected_salary_mod(N, A):
    x = 0
    expected_salary = 0
    modulus = 998244353

    # Calculate the modular inverse of N using Fermat's Little Theorem
    inv_N = pow(N, modulus-2, modulus)

    for y in range(1, N+1):
        if y < x:
            break

        # Calculate the probability of not having rolled any number from y to N in the previous rolls
        prob_not_rolled = pow((1 - y * inv_N) % modulus, y-1, modulus)

        # Calculate the contribution to the expected salary when the dice shows 'y'
        contribution = A[y-1] * prob_not_rolled * inv_N
        expected_salary += contribution
        expected_salary %= modulus
        
        # Update x
        x = y

    return expected_salary


# Input values
N = int(input())
A = list(map(int, input().split()))

a=expected_salary_mod(N, A)
print(a)
