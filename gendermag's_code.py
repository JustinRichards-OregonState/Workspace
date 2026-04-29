def cal(kilograms, meters):
    """Calculate the Body Mass Index (BMI) given weight and height. Takes two
    arguments weight in kilograms (kg) and height in meters(m). The function returns
    BMI of the weight and height as a float."""

    if meters <= 0:
        return 0.0
    return kilograms / (meters ** 2)

#input values
kilograms = 55
meters = 1.67

#calculates BMI
bmi = cal(kilograms, meters)


if meters <= 0 or kilograms <= 0:
    print(f"The BMI is: 0.00")
else:
    print(f"The BMI is: {bmi:.2f}")