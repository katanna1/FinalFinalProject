from . import orders, order_details, customers, reviews, payments, promotions, menu_items

def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customers.router)
    app.include_router(reviews.router)
    app.include_router(payments.router)
    app.include_router(promotions.router)
    app.include_router(menu_items.router)