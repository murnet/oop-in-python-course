# This file demonstrates how a client could create an order. It's now much simpler.
from ..naive_solution.order_request import OrderRequest
from order_service import OrderService

# Clients can now create orders without needing any knowledge of the underlying implementation details. All of this has been abstracted away, and life is now simple.
order_request = OrderRequest()
order_service = OrderService()
order_service.create_order(order_request)
