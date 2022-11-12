#! /usr/bin/env python3

"""

"""

import pandas as pd

def main():

    df = pd.read_csv("SpaceX.csv")

    print(df)

    date_list = df["Date"].tolist()

    datetime_list = []

    for item in date_list:
        d, m, y = item.split("-")
        datetime = str(y) + "-" + str(m) + "-" + str(d)
        print (datetime)
        datetime_list.append(datetime)

    print (datetime_list)

    df.insert(1, "DATETIME", datetime_list, True)

    print (df)

    df.to_csv("SPACEX_DATETIME.csv")


if __name__ == "__main__":
    main()

