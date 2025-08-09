import json

def read_order_book(filename:str) -> dict:
    """Reads order book from file """
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found") 
        return {}
    except json.JSONDecodeError:
        print("Invalid JSON format") 
        return {}

def calculate_spread(order_book:dict) -> float:
    try:
        best_bid = float(order_book["bids"][0][0])
        best_ask = float(order_book["asks"][0][0])
        return best_ask - best_bid

    except (KeyError, IndexError, ValueError) as e:
        print(f"Error calculating spread: {e}")
        return 0.0

def total_volumen(order_book:dict, side: str) -> float:
    #total = 0.0
    try:  
        # for price, quantity in order_book[side]:
        #     total += float(quantity) 
        # return total
        return sum(float(qty) for _, qty in order_book[side])
    
    except (KeyError, ValueError) as e:
        print(f"Error calculating totalvolumen : {e}")
        return 0.0

def weighted_average_price(order_book: dict, side:str) -> float:
    """
    Calcula el precio promedio ponderado para bids o asks.
    WAP = sum(precio * cantidad) / sum(cantidad)
    """
    try:
        total_volumen = sum(float(quantity) for _, quantity in order_book[side])

        if total_volumen == 0:
            return 0.0

        total_price_quantity = sum(float(quantity) * float(price) for price, quantity in order_book[side])
            
        return total_price_quantity/total_volumen

    except (ValueError, KeyError) as e:
        print ("Error calculating {e}")


def filter_orders_by_min_quantity(order_book: dict, side: str, min_qty: float) -> list:
    """Filtra las órdenes de bids o asks que tengan cantidad >= min_qty
    Devuelve la lista filtrada (misma estructura: [(precio, cantidad), ...]) """
    higher_price_lst = []
    try:
        # for price,_ in order_book[side]:
        #     if float(price) >= min_qty:
        #         higher_price_lst.append(price)
        # return higher_price_lst

        return [price for price,_ in order_book[side] if float(price) >= min_qty]
        # return {price:quantity for price,quantity in order_book[side] if float(price) >= min_qty}.  - if we would like to return a dict
    except KeyError as e:
        print("The side{side} doesn't exists")
        return []
    except ValueError as e:
        print("Error filtering orders{e}")
        return []


def count_orders_by_min_quantity(order_book: dict, side: str, min_qty: float, max_qty: float) -> list:
    """
    Cuenta el número de órdenes cuyo precio está entre min_price y max_price inclusive.
    """
    count = 0
    try:
        # for price,_ in order_book[side]:
        #         if float(price) >= min_qty and float(price) <= max_qty:
        #             count+=1
        return sum(count + 1 for price,_ in order_book[side] if float(price) >= min_qty and float(price) <= max_qty)

    except KeyError as e:
        print("The side{side} doesn't exists")
        return[]
    except ValueError as e:
        print("Error filtering orders{e}")
        return[]


def validate_order_book(order_book: dict) -> bool:
    """
    Verifica que 'bids' y 'asks' existan y no estén vacíos.
    """
    try:
        if "bids" not in order_book or "asks" not in order_book:
            print("Bids or asks missing from the book")
            return False
        if not order_book['bids'] or not order_book['asks']:
            print("Bids or asks are empty")
            return False
        return True

    except Exception as e:
        print(f"Unexpected error validating order book: {e}")
        return False

def sort_orders_by_quantity(order_book: dict, side: str) -> list:
    """
    Ordena las órdenes por cantidad descendente.
    """
    order_book_float_list= []
    try:
        return sorted(order_book[side], key=lambda qty:float(qty[1]), reverse=True)
    except (ValueError, KeyError) as e:
        print("Error trying to sort order_book")

