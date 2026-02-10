from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# In-memory storage for orders
orders = []

@api_view(['GET', 'POST', 'DELETE'])
def order_list(request):
    global orders  # declare global at the very top

    if request.method == 'GET':
        # Return all orders
        return Response(orders, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        # Validate required fields
        if not all(k in data for k in ("orderId", "bookId", "quantity")):
            return Response(
                {"error": "orderId, bookId, and quantity are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Add order to list
        orders.append(data)
        return Response(
            {**data, "status": "Order created successfully"},
            status=status.HTTP_201_CREATED
        )

    elif request.method == 'DELETE':
        order_id = request.data.get("orderId")
        if not order_id:
            return Response({"error": "orderId required"}, status=status.HTTP_400_BAD_REQUEST)

        # Remove orders with matching orderId
        orders = [order for order in orders if order.get("orderId") != order_id]
        return Response(
            {"status": f"Order {order_id} deleted successfully"},
            status=status.HTTP_200_OK
        )
@api_view(['GET', 'DELETE'])
def order_detail(request, orderId):
    global orders

    # Find the order
    order = next((o for o in orders if o.get("orderId") == orderId), None)

    if not order:
        return Response({"error": f"Order {orderId} not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(order, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        orders = [o for o in orders if o.get("orderId") != orderId]
        return Response({"status": f"Order {orderId} deleted successfully"}, status=status.HTTP_200_OK)
