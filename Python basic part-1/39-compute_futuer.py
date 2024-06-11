# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79
# FV = P(1 + r/n)^nt.
# FV = the future value;
# P = the principal;
# r = the annual interest rate expressed as a decimal;
# n = the number of times interest is paid each year;
# t = time in years.

amt = 10000
int = 3.5
years = 7

FV = amt * (1 + int / 100) ** years
print(FV)
