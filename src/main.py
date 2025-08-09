from sales_processing import sales_processing 
from sales_processing import sales_utils
from api_connection import *
from order_book_processing import *

#read data

#call clean methos

#write data

if __name__== "__main__":
    # symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    # limit = input("Enter limit (default 5): ")
    # try:
    #     limit = int(limit)
    # except ValueError:
    #     limit = 5

    # try:
    #     symbol = str(symbol)
    # except ValueError:
    #     symbol = "BTCUSDT"

    limit = 5
    symbol = "BTCUSDT"

    data = fetch_order_book(symbol, limit)
    order_book = read_order_book("data/raw/order_book.json")
    print(f"Spread: {calculate_spread(order_book)}")
    print(f"Bid volume: {total_volumen(order_book, 'bids')}")
    print(f"Ask volume: {total_volumen(order_book, 'asks')}")

    print("Spread in order_book: " + str(calculate_spread(order_book)))
    print("total volumne for asks is: " + str(total_volumen(order_book, "asks")))
    print("precio promedio ponderado: " + str(weighted_average_price(order_book, "asks")))
    print("Filter by min quantity: " + str(filter_orders_by_min_quantity(order_book, "asks", 116676.91000000)))
    print("Count orders between min and max quantity: " + str(count_orders_by_min_quantity(order_book, "asks", 116676.91000000,116677.76000000)))
    print("Sort orders based inquantity: " + str(sort_orders_by_quantity(order_book, "asks")))