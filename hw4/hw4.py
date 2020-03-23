import datetime as dt


def main():
    year = input("Which year are you born? ")
    month = input("Which month?  1-12 ")
    born = dt.datetime.strptime(year+"-"+month, "%Y-%m")
    print("you are born on %s, %s" %
          (born.strftime("%Y"), born.strftime("%b")))
    print("you are %s years old." % (
        round((dt.datetime.today()-born).days/365)
    ))


if __name__ == "__main__":
    while True:
        main()
        if "Y" == input("Continue?(Y/N)"):
            break
