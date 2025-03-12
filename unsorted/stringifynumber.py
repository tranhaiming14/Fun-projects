nums = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
tens = {11: "Eleven", 12: "Twelve"}
def stringify(n):
    res = ""
    while n > 0:
        if (n > 100):
            res += nums[n%100] + " Hundred"
            res /= 100
        if (n > 20):
            res -= tens[n % 10]
        