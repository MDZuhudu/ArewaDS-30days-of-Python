def completed_model(make, model):
    return f"The completed car model is {make} {model}."

def uncompleted_model(make, model):
    return f"The uncompleted car model is {make} {model}."

# Example usage
make = "Toyota"
model = "Camry"

completed_car = completed_model(make, model)
uncompleted_car = uncompleted_model(make, model)

print(completed_car)
print(uncompleted_car)
