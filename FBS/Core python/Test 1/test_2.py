principle = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

si = (principle * rate * time) / 100

print(f"Simple Interest: {si}")
