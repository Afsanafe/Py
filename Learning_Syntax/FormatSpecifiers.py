# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify 
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator

def run():
    price1 = 3.141459
    price2 = -987.65
    price3 = 12.34
    price4 = 45849305
    price5 = -234985424.324234

    print(f"Price 1 is ${price1:.2f}") # displays 2 decimals
    print(f"Price 2 is ${price2:.3f}")  # displays 3 decimals
    print(f"Price 3 is ${price3:.1f}") # displays 1 decimal


    print(f"Price 3 is ${price3:10}") # displays 10 spaces, so 5 spaces are added in front

     # basic rounding
    print(f"Price 1 (2dp)      : ${price1:.2f}")
    print(f"Price 2 (3dp)      : ${price2:.3f}")
    print(f"Price 3 (1dp)      : ${price3:.1f}")


    print(f"Price 1 (2dp)      : ${price1:.2f}")
    print(f"Price 2 (3dp)      : ${price2:.3f}")
    print(f"Price 3 (1dp)      : ${price3:.1f}")


    print(f"Price 4 (1dp)      : ${price4:,}") # adds a comma seperator for all values
    print(f"Price 5 (1dp)      : ${price5:,.2f}") # you can combine format specifiers


    # column formatting
    print(f"Right‑aligned width10 : ${price3:>10.2f}")
    print(f"Left‑aligned width10  : ${price3:<10.2f}")
    print(f"Center width10        : ${price3:^10.2f}")

    # zero‑padding & sign control
    print(f"Zero‑pad width10      : ${price1:010.2f}")   # 0000003.14
    print(f"Always show sign      : ${price1:+.2f}")    # +3.14
    print(f"Always show sign      : ${price2:+.2f}")    # -987.65
    print(f"Space for positives   : ${price2: .2f}")    # -9876.50
    print(f"Space for positives   : ${price1: .2f}")
                                                    # (positive would have leading space)

    # thousands separator
    print(f"With commas           : ${price2:,.2f}")    # -9,876.50


