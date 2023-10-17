def main():
     v = feet2meter(input("Сколько футов:"))
     print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
     s = v.rstrip("ft")
     n = float(s)
     c = 0.3048
     r = n * c
     return r


main()