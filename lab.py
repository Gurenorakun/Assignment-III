class BMI:
    def __init__(self, weight_kg, height_m):
        self._weight_kg = weight_kg
        self._height_m = height_m

    @property
    def weight(self):
        return self._weight_kg

    @property
    def height(self):
        return self._height_m

    def BMI_Value(self):
        return self._weight_kg / (self._height_m ** 2)

    def __eq__(self, other):
        if isinstance(other, BMI):
            return (self._weight_kg, self._height_m) == (other.weight, other.height)
        return False

def main():
    berat1 = float(input ("Orang 1 (Berat dalam kg): "))
    tinggi1 = float(input ("Orang 1 (tinggi dalam meter): "))
    berat2 = float(input ("Orang 2 (Berat dalam kg): "))
    tinggi2 = float(input ("Orang 2 (tinggi dalam meter): "))
    person1 = BMI(berat1, tinggi1)  
    person2 = BMI(berat2, tinggi2)

    print("BMI Orang 1:", person1.BMI_Value())
    print("BMI Orang 2:", person2.BMI_Value())

    if person1 == person2:
        print("Orang 1 dan Orang 2 mempunyai berat badan dan tinggi yang sama.")
    else:
        print("Orang 1 dan Orang 2 mempunyai berat badan atau tinggi yang berbeda.")

if __name__ == "__main__":
    main()