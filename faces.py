def main():
    s = input()
    sn = convert(s)
    print(sn)

def convert(s):
        s2 = s.replace(":)", "🙂")
        s3 = s2.replace(":(", "🙁")
        return s3
main()