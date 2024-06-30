#include <iostream>
#include <vector>
#include <string>

// Clase Car que representa un coche
class Car {
public:
    // Constructor para inicializar un coche con su modelo y precio por día
    Car(const std::string& model, double pricePerDay)
        : model(model), pricePerDay(pricePerDay), isRented(false) {}

    // Métodos para obtener el modelo, precio por día y estado de renta del coche
    std::string getModel() const { return model; }
    double getPricePerDay() const { return pricePerDay; }
    bool isCarRented() const { return isRented; }

    // Métodos para rentar y devolver el coche
    void rent() { isRented = true; }
    void returnCar() { isRented = false; }

private:
    std::string model;       // Modelo del coche
    double pricePerDay;      // Precio por día de renta
    bool isRented;           // Indica si el coche está rentado
};

// Clase CarRentalSystem que gestiona el sistema de renta de coches
class CarRentalSystem {
public:
    // Método para agregar un coche al sistema
    void addCar(const Car& car) {
        cars.push_back(car);
    }

    // Método para mostrar los coches disponibles para rentar
    void showAvailableCars() const {
        std::cout << "Available cars:\n";
        for (std::vector<Car>::const_iterator it = cars.begin(); it != cars.end(); ++it) {
            if (!it->isCarRented()) {
                std::cout << "Model: " << it->getModel() << ", Price per day: $" << it->getPricePerDay() << '\n';
            }
        }
    }

    // Método para rentar un coche por su modelo
    void rentCar(const std::string& model) {
        for (std::vector<Car>::iterator it = cars.begin(); it != cars.end(); ++it) {
            if (it->getModel() == model && !it->isCarRented()) {
                it->rent();
                std::cout << "You have successfully rented the " << model << ".\n";
                return;
            }
        }
        std::cout << "Sorry, the car model is either not available or already rented.\n";
    }

    // Método para devolver un coche por su modelo
    void returnCar(const std::string& model) {
        for (std::vector<Car>::iterator it = cars.begin(); it != cars.end(); ++it) {
            if (it->getModel() == model && it->isCarRented()) {
                it->returnCar();
                std::cout << "You have successfully returned the " << model << ".\n";
                return;
            }
        }
        std::cout << "Sorry, the car model is not currently rented or does not exist in our inventory.\n";
    }

private:
    std::vector<Car> cars;   // Vector que almacena los coches en el sistema
};

int main() {
    CarRentalSystem rentalSystem;

    // Agregar algunos coches al sistema
    rentalSystem.addCar(Car("Toyota Camry", 30.0));
    rentalSystem.addCar(Car("Honda Accord", 35.0));
    rentalSystem.addCar(Car("Tesla Model S", 100.0));

    int choice;
    std::string model;

    // Bucle principal para la interacción con el usuario
    do {
        std::cout << "\nCar Rental System\n";
        std::cout << "1. Show available cars\n";
        std::cout << "2. Rent a car\n";
        std::cout << "3. Return a car\n";
        std::cout << "4. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                // Mostrar coches disponibles
                rentalSystem.showAvailableCars();
                break;
            case 2:
                // Rentar un coche
                std::cout << "Enter the model you want to rent: ";
                std::cin.ignore(); // Limpiar el buffer
                std::getline(std::cin, model);
                rentalSystem.rentCar(model);
                break;
            case 3:
                // Devolver un coche
                std::cout << "Enter the model you want to return: ";
                std::cin.ignore(); // Limpiar el buffer
                std::getline(std::cin, model);
                rentalSystem.returnCar(model);
                break;
            case 4:
                // Salir del programa
                std::cout << "Thank you for using the Car Rental System!\n";
                break;
            default:
                std::cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 4);

    return 0;
}

