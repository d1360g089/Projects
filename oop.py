

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.model}, {self.year}")

    @property
    def model(self):
        return self._model 
    
    @model.setter
    def model(self, model):
        if not model:
            raise ValueError("Missing Model")
        self._model = model
    
def main():
    try:
        my_car = Car(input("Model: ", input("Year: ")))
        print(my_car)
    except ValueError:
        pass


if __name__ == "__main__":
    main()
    
