
def calculate_gst(amount, gst_rate):
    gst = amount * gst_rate / 100
    total = amount + gst
    return gst, total

price = float(input("Enter the product price: "))
rate = float(input("Enter GST rate (%): "))

gst_amnt,final_price = calculate_gst(price, rate)

print("GST Amount =", gst_amnt)
print("Total Price =", final_price)