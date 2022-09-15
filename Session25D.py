# Decorator -> Which will manipulate the function's behavior at run time
# Create a Function which takes another function as input
def compute_taxes(func):

    def inner(amount, taxes):
        if amount > 0 and amount <= 2000:
            # Update taxes to 0.18
            taxes = 0.18
        elif amount > 2000:
            # Update taxes to 0.25
            taxes = 0.25
        else:
            print("This is an Invalid Amount")
            return

        # Return and Execute the function which was passed to compute_taxes
        # from inner function
        return func(amount, taxes)

    return inner


@compute_taxes          # -> compute_taxes(pay)
def pay(amount, taxes):
    return amount + (taxes*amount)


# result = compute_taxes(pay)
# result()

amount_to_pay = pay(2000, 0)
print("amount_to_pay is: \u20b9", amount_to_pay)