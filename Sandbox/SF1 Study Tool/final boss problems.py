


def calculate_subtotal(items):
    """
    Calculate subtotal (sum) of an e-commerce order.
    
    Args:
        items: List of tuples (price, quantity, discount)

    Returns:   
        float: Subtotal of order
    """
    subtotal = 0
    for item in items:
        price = item[0]
        quantity = item[1]
        discount = item[2] if len(item) > 2 else 0
        subtotal += (price * quantity) * (1 - discount)
    return subtotal

def process_checkout(items, shipping_address):
    """
    Process an e-commerce checkout with items and shipping address.
    
    Args:
        items: List of tuples (price, quantity, discount)
        shipping_address (str): Destination address

    Returns:
        float: Total cost of order including tax and delivery

    Shipping addresses:
        Montreal: 10 km, 14.975% tax
        Toronto: 542 km, 13% tax
        Vancouver: 4924 km, 12% tax
        Edmonton: 3584 km, 5% tax
        Charlottetown: 1149 km, 15% tax

    Delivery cost: 1.80$ per 100 km = 0.018$ per km
    """
    addresses = [("Montreal", 10, 14.975), ("Toronto", 542, 13), ("Vancouver", 4924, 12), ("Edmonton", 3584, 5), ("Charlottetown", 1149, 15)]
    subtotal = calculate_subtotal(items)
    address = None
    for addr in addresses:
        if addr[0] == shipping_address:
            address = addr
    distance = address[1]
    tax_rate = address[2]
    delivery_cost = (distance / 100) * 1.80
    tax = subtotal * (tax_rate / 100)
    final_cost = subtotal + delivery_cost + tax
    return final_cost











def calculate_pizza_price(size, toppings):
    """
    Calculate price of a single pizza.
    
    Args:
        size (str): 'S', 'M', or 'L'
        toppings (list): List of toppings
        
    Returns:
        float: Price of pizza
        
    Base prices:
    - Small: $8
    - Medium: $10 
    - Large: $12
    Each topping: $1.50
    """
    pizza_prices = [('S', 8), ('M', 10), ('L', 12)]

    base_price = 0
    for size_price in pizza_prices:
        if size_price[0] == size:
            base_price = size_price[1]
    toppings_price = len(toppings) * 1.50
    return base_price + toppings_price

def calculate_order_total(pizzas):
    """
    Calculate total order cost with deals applied.
    
    Args:
        pizzas: List of tuples (size, [toppings])
        
    Returns:
        float: Total order cost after deals
        
    Deals:
    - Order 2+ pizzas: 10% off
    - Large pizza with 3+ toppings: $2 off
    """
    total = 0
    
    for size, toppings in pizzas:
        pizza_price = calculate_pizza_price(size, toppings)
        
        # Apply large pizza deal
        if size == 'L' and len(toppings) >= 3:
            pizza_price -= 2
            
        total += pizza_price
    
    # Apply multiple pizza deal    
    if len(pizzas) >= 2:
        total *= 0.9
        
    return round(total, 2)










def calculate_session_points(kills, time_alive, position):
    """
    Calculate points earned in a battle royale game session.
    
    Args:
        kills (int): Number of eliminations
        time_alive (int): Survival time in minutes
        position (int): Final placement (1-100)
        
    Returns:
        int: Points earned this session
        
    Points system:
    - Each kill: 50 points
    - Every minute survived: 10 points
    - Top 10 placement bonus: 300 points
    - Victory bonus: 500 points
    """
        
    points = (kills * 50) + (time_alive * 10)
    
    # Placement bonuses
    if position == 1:
        points += 500 
    elif position <= 10:
        points += 300  
        
    return points

def update_player_rank(current_rank, recent_sessions):
    """
    Update player rank based on recent game sessions.
    
    Args:
        current_rank (str): Current rank EG: ('Bronze')
        recent_sessions: List of tuples (kills, time_alive, position)
        
    Returns:
        str: New rank after calculating the average of points aquired in recent performances
        
    Ranks: Bronze (0-999), Silver (1000-1999),
    Gold (2000-2999), Diamond (3000+)
    """
    ranks = ['Bronze', 'Silver', 'Gold', 'Diamond']
    total_points = 0
    
    for kills, time_alive, position in recent_sessions:
        session_points = calculate_session_points(kills, time_alive, position)
        total_points += session_points
    
    # Calculate new rank based on average points
    avg_points = total_points // len(recent_sessions)
    
    if avg_points >= 3000:
        new_rank = 'Diamond'
    elif avg_points >= 2000:
        new_rank = 'Gold'
    elif avg_points >= 1000:
        new_rank = 'Silver'
    else:
        new_rank = 'Bronze'
        
    return new_rank