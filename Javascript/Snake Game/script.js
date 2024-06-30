// Obtener el canvas y el contexto de dibujo 2D
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Obtener el div de fin de juego y el botón de reinicio
const gameOverDiv = document.getElementById('gameOver');
const restartButton = document.getElementById('restartButton');

// Definir la escala de los bloques y calcular las filas y columnas
const scale = 20;
const rows = canvas.height / scale;
const columns = canvas.width / scale;

let snake;  // Variable para la serpiente
let fruit;  // Variable para la fruta
let gameInterval;  // Variable para el intervalo del juego

// Configuración inicial del juego
function setup() {
    snake = new Snake();  // Crear una nueva serpiente
    fruit = new Fruit();  // Crear una nueva fruta
    fruit.pickLocation();  // Elegir una ubicación al azar para la fruta

    gameOverDiv.style.display = 'none';  // Ocultar el mensaje de fin de juego
    canvas.style.display = 'block';  // Mostrar el canvas

    // Iniciar el bucle del juego con un intervalo de tiempo
    gameInterval = window.setInterval(() => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);  // Limpiar el canvas
        fruit.draw();  // Dibujar la fruta
        snake.update();  // Actualizar la posición de la serpiente
        snake.draw();  // Dibujar la serpiente

        if (snake.eat(fruit)) {  // Verificar si la serpiente come la fruta
            fruit.pickLocation();  // Elegir una nueva ubicación para la fruta
        }

        snake.checkCollision();  // Verificar si la serpiente colisiona consigo misma
        if (snake.checkWallCollision()) {  // Verificar si la serpiente colisiona con una pared
            endGame();  // Terminar el juego
        }
    }, 250);  // Intervalo de 250 milisegundos
}

// Función para terminar el juego
function endGame() {
    clearInterval(gameInterval);  // Detener el intervalo del juego
    canvas.style.display = 'none';  // Ocultar el canvas
    gameOverDiv.style.display = 'flex';  // Mostrar el mensaje de fin de juego
}

// Función para reiniciar el juego
function restartGame() {
    setup();  // Llamar a la función de configuración inicial
}

// Agregar un event listener para los eventos de teclado
window.addEventListener('keydown', (e) => {
    const direction = e.key.replace('Arrow', '');  // Obtener la dirección de la tecla presionada
    snake.changeDirection(direction);  // Cambiar la dirección de la serpiente
});

// Agregar un event listener para el botón de reinicio
restartButton.addEventListener('click', restartGame);

// Clase para la serpiente
function Snake() {
    this.x = 0;  // Posición inicial en x
    this.y = 0;  // Posición inicial en y
    this.xSpeed = scale * 1;  // Velocidad en x
    this.ySpeed = 0;  // Velocidad en y
    this.total = 0;  // Tamaño inicial de la serpiente
    this.tail = [];  // Arreglo para almacenar las partes de la cola

    // Dibujar la serpiente
    this.draw = function() {
        ctx.fillStyle = "#FFF";  // Color blanco

        for (let i = 0; i < this.tail.length; i++) {  // Dibujar cada parte de la cola
            ctx.fillRect(this.tail[i].x, this.tail[i].y, scale, scale);
        }

        ctx.fillRect(this.x, this.y, scale, scale);  // Dibujar la cabeza de la serpiente
    };

    // Actualizar la posición de la serpiente
    this.update = function() {
        for (let i = 0; i < this.tail.length - 1; i++) {  // Mover las partes de la cola
            this.tail[i] = this.tail[i + 1];
        }

        this.tail[this.total - 1] = { x: this.x, y: this.y };  // Actualizar la última parte de la cola

        this.x += this.xSpeed;  // Mover la serpiente en x
        this.y += this.ySpeed;  // Mover la serpiente en y
    };

    // Cambiar la dirección de la serpiente
    this.changeDirection = function(direction) {
        switch (direction) {
            case 'Up':
                if (this.ySpeed === 0) {  // Verificar que no se esté moviendo verticalmente
                    this.xSpeed = 0;
                    this.ySpeed = -scale * 1;  // Cambiar la velocidad en y
                }
                break;
            case 'Down':
                if (this.ySpeed === 0) {  // Verificar que no se esté moviendo verticalmente
                    this.xSpeed = 0;
                    this.ySpeed = scale * 1;  // Cambiar la velocidad en y
                }
                break;
            case 'Left':
                if (this.xSpeed === 0) {  // Verificar que no se esté moviendo horizontalmente
                    this.xSpeed = -scale * 1;  // Cambiar la velocidad en x
                    this.ySpeed = 0;
                }
                break;
            case 'Right':
                if (this.xSpeed === 0) {  // Verificar que no se esté moviendo horizontalmente
                    this.xSpeed = scale * 1;  // Cambiar la velocidad en x
                    this.ySpeed = 0;
                }
                break;
        }
    };

    // Verificar si la serpiente come la fruta
    this.eat = function(fruit) {
        if (this.x === fruit.x && this.y === fruit.y) {  // Comparar las posiciones
            this.total++;  // Aumentar el tamaño de la serpiente
            return true;
        }

        return false;
    };

    // Verificar si la serpiente colisiona consigo misma
    this.checkCollision = function() {
        for (let i = 0; i < this.tail.length; i++) {  // Comparar la posición de la cabeza con cada parte de la cola
            if (this.x === this.tail[i].x && this.y === this.tail[i].y) {
                this.total = 0;  // Reiniciar el tamaño de la serpiente
                this.tail = [];  // Vaciar la cola
            }
        }
    };

    // Verificar si la serpiente colisiona con una pared
    this.checkWallCollision = function() {
        return this.x >= canvas.width || this.y >= canvas.height || this.x < 0 || this.y < 0;
    };
}

// Clase para la fruta
function Fruit() {
    this.x;  // Posición en x
    this.y;  // Posición en y

    // Elegir una ubicación al azar para la fruta
    this.pickLocation = function() {
        this.x = Math.floor(Math.random() * rows) * scale;
        this.y = Math.floor(Math.random() * columns) * scale;
    };

    // Dibujar la fruta
    this.draw = function() {
        ctx.fillStyle = "#4cafab";  // Color verde
        ctx.fillRect(this.x, this.y, scale, scale);  // Dibujar la fruta
    };
}

// Inicializar el juego
setup();
