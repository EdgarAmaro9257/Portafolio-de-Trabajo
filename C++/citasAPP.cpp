#include <iostream>
#include <vector>
#include <string>

// Clase User que representa un perfil de usuario
class User {
public:
    User(const std::string& username, const std::string& bio)
        : username(username), bio(bio), likes(0) {}

    // Métodos para obtener información del usuario
    std::string getUsername() const { return username; }
    std::string getBio() const { return bio; }
    int getLikes() const { return likes; }

    // Método para agregar un "me gusta" al usuario
    void addLike() { ++likes; }

private:
    std::string username;  // Nombre de usuario
    std::string bio;       // Biografía del usuario
    int likes;             // Cantidad de "me gusta" recibidos
};

// Clase DatingApp que gestiona la aplicación de citas
class DatingApp {
public:
    // Método para registrar un nuevo usuario
    void registerUser(const User& user) {
        users.push_back(user);
    }

    // Método para mostrar todos los perfiles de usuario
    void showProfiles() const {
        std::cout << "User Profiles:\n";
        for (size_t i = 0; i < users.size(); ++i) {
            std::cout << i + 1 << ". " << users[i].getUsername() << " - " << users[i].getBio()
                      << " (" << users[i].getLikes() << " likes)\n";
        }
    }

    // Método para dar "me gusta" a un usuario por su índice
    void likeUser(size_t index) {
        if (index > 0 && index <= users.size()) {
            users[index - 1].addLike();
            std::cout << "You liked " << users[index - 1].getUsername() << "!\n";
        } else {
            std::cout << "Invalid user index.\n";
        }
    }

private:
    std::vector<User> users;  // Vector que almacena los perfiles de usuario
};

int main() {
    DatingApp app;

    int choice;
    std::string username, bio;
    size_t index;

    // Bucle principal para la interacción con el usuario
    do {
        std::cout << "\nDating App Menu\n";
        std::cout << "1. Register user\n";
        std::cout << "2. Show profiles\n";
        std::cout << "3. Like a user\n";
        std::cout << "4. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                // Registrar un nuevo usuario
                std::cout << "Enter username: ";
                std::cin.ignore(); // Limpiar el buffer
                std::getline(std::cin, username);
                std::cout << "Enter bio: ";
                std::getline(std::cin, bio);
                app.registerUser(User(username, bio));
                break;
            case 2:
                // Mostrar perfiles de usuario
                app.showProfiles();
                break;
            case 3:
                // Dar "me gusta" a un usuario
                std::cout << "Enter the index of the user you want to like: ";
                std::cin >> index;
                app.likeUser(index);
                break;
            case 4:
                // Salir del programa
                std::cout << "Thank you for using the Dating App!\n";
                break;
            default:
                std::cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 4);

    return 0;
}
