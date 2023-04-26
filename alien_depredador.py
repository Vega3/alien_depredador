import random


class Nodo:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def set_next(self, nodo):
        self.next = nodo

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def __str__(self):
        return str(self.value)


nodo1 = Nodo(1)
nodo2 = Nodo(6)
nodo3 = Nodo(7)
nodo4 = Nodo(8)


class Lista_enlazada:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.size = 0
        self.tail = tail

    def set_head_nodo(self, head):
        head.next = self.head
        self.head = head
        self.size += 1
        self.set_tail_automatico()

    def set_head_value(self, value):
        print(f"set_head_value(self, {value})")
        nuevo_nodo = Nodo(value)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo
        self.size += 1
        self.set_tail_automatico()

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def set_tail_automatico(self):
        if self.head is None:
            self.tail = None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            self.tail = current

    def append(self, value):
        # print(f"append(self, {value})")
        nuevo_nodo = Nodo(value)
        if self.size == 0:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            self.tail.next = nuevo_nodo
            self.tail = nuevo_nodo

        self.size += 1

    def borrar_cola(self):
        if self.size == 0:
            return "La lista está vacía"

        elif self.size == 1:
            del_el = self.head
            self.tail = None
            self.head = None
            self.size -= 1
            return del_el

        self.size -= 1
        current_node = self.head
        while current_node.get_next() is not None:
            if current_node.get_next() == self.tail:
                self.tail = current_node
                del_el = current_node.get_next()
                current_node.set_next(None)
                self.set_tail_automatico()
                return del_el
            current_node = current_node.get_next()

    def get_nodo_posicion_X(self, x):
        contador = 0
        if self.get_head() is None:
            return "La lista está vacía"

        current = self.head
        if contador == x:
            return current.value
        while current.next is not None:
            current = current.next
            contador += 1
            if contador == x:
                return current.value

        return "elemento fuera de rango"

    def insert(self, value, x=0):
        nuevo_nodo = Nodo(value)
        # print(f"insert(self, {x}, {nuevo_nodo.value})")
        if x == 0:
            self.set_head_nodo(nuevo_nodo)
            return ""
        contador = 1
        current = self.head
        while current.next is not None:
            current = current.next
            contador += 1
            if contador == x:
                nuevo_nodo.next = current.next
                current.next = nuevo_nodo
        return ""

    def pop(self, posicion=0):
        if self.size == 0:
            return "La lista está vacía"
        elif self.size < posicion:
            return "posicion fuera de rango"
        elif posicion == 0:
            a = self.head
            self.head = self.head.next
            return a
        else:
            contador = 1
            current = self.head
            while contador != posicion and current.next.next is not None:
                current = current.next
                contador += 1
            borrar = current.next
            current.next = borrar.next
            return borrar



class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        self.alien = alien
        self.depredador = depredador
        self.pos_alien = [0, 0]
        self.pos_depre = [0, 0]
        for i in range(rows):
            row = Lista_enlazada()
            for j in range(cols):
                num = random.randint(1, 2)
                if num == 1:
                    row.append(" + ")
                else:
                    row.append(" - ")
            self.matrix.append(row)
        num1 = random.randint(0, self.rows - 1)
        num2 = random.randint(0, self.cols - 1)
        self.matrix[num1].insert(depredador.emoji, num2)
        self.pos_depre = [num1, num2]

    def get(self, row, col):
        return self.matrix[row].head.value

    def set(self, row, col, value):
        node = self.matrix[row].head
        for i in range(col):
            node = node.next
        node.value = value

    def display(self):
        for i in range(self.rows):
            current_node = self.matrix[i].head
            for j in range(self.cols):
                print(current_node.value, end=" ")
                current_node = current_node.next
            print()

    def posicion_alien(self):
        fila = int(input("ingrese la fila del alien: "))
        columna = int(input("ingrese la columna del alien: "))
        self.matrix[fila].insert(alien.emoji, columna)
        self.pos_alien = [fila, columna]
        print("")
        self.vida(fila, columna)

    def mover_alien(self):
        movimiento = str(input(
            "pulse W para mover arriba, A para mover a la izquierda, S para mover abajo, D para mover a la derecha: "))
        if movimiento == "w":
            new_row = self.pos_alien[0] - 1
            new_col = self.pos_alien[1]
            self.matrix[self.pos_alien[0]].pop(self.pos_alien[1])
            self.matrix[self.pos_alien[0]].insert("   ", self.pos_alien[1])
            self.matrix[self.pos_alien[0] - 1].insert(alien.emoji, self.pos_alien[1])
            self.pos_alien = [self.pos_alien[0] - 1, self.pos_alien[1]]
        elif movimiento == "a":
            new_row = self.pos_alien[0]
            new_col = self.pos_alien[1] - 1
            self.matrix[self.pos_alien[0]].pop(self.pos_alien[1] - 1)
            self.matrix[self.pos_alien[0]].insert(alien.emoji, self.pos_alien[1] - 1)
            self.matrix[self.pos_alien[0]].pop(self.pos_alien[1])
            self.matrix[self.pos_alien[0]].insert("   ", self.pos_alien[1])
            self.pos_alien = [new_col, new_col]
        elif movimiento == "s":
            new_row = self.pos_alien[0] + 1
            new_col = self.pos_alien[1]
            self.matrix[self.pos_alien[0]].pop(self.pos_alien[1])
            self.matrix[self.pos_alien[0]].insert("   ", self.pos_alien[1])
            self.matrix[self.pos_alien[0] + 1].insert(alien.emoji, self.pos_alien[1])
            self.pos_alien = [self.pos_alien[0] + 1, self.pos_alien[1]]
        elif movimiento == "d":
            new_row = self.pos_alien[0]
            new_col = self.pos_alien[1] + 1
            self.vida(new_row, new_col)
            self.matrix[self.pos_alien[0]].pop(self.pos_alien[1])
            self.matrix[self.pos_alien[0]].insert("   ", self.pos_alien[1])
            self.matrix[self.pos_alien[0]].insert(alien.emoji, self.pos_alien[1] + 1)
            self.pos_alien = [self.pos_alien[0], self.pos_alien[1] + 1]
        print("")
        self.mover_depredador()
        self.vida(self.pos_alien[0], self.pos_alien[1])
        print(matrix.display())

    def mover_depredador(self):
        num1 = random.randint(0, self.rows - 1)
        num2 = random.randint(0, self.cols - 1)
        if num1 == self.pos_alien[0] and num2 == self.pos_alien[1]:
            print("misma posicion")
            self.matrix[self.pos_alien[0]].pop(self.pos_alien[1])
            self.matrix[num1].insert(alien.emoji + depredador.emoji, num2)
        self.matrix[self.pos_depre[0]].pop(self.pos_depre[1])
        self.matrix[self.pos_depre[0]].insert("   ", self.pos_depre[1])
        self.matrix[0].insert(depredador.emoji, num2)
        self.pos_depre = [num1, num2]
        if self.matrix[num1].get_nodo_posicion_X(num2) == " - ":
            self.depredador.vida -= 10

    def rellenar(self):
        num = random.randint(1, 2)
        if num == 1:
            self.matrix[self.pos_alien[0]].insert("   ", self.pos_alien[1])
        else:
            self.matrix[self.pos_alien[0]].insert("   ", self.pos_alien[1])

    def vida(self, row, col):
        if self.pos_depre == self.alien:
            self.alien.vida -= 25
        if self.matrix[row].get_nodo_posicion_X(col) == " - ":
            self.alien.vida -= 10
        print(f"Alien: \u2764\uFE0F: {self.alien.vida} \U0001F4CC: {self.pos_alien}, ---------- Depredador: "
              f"\u2764\uFE0F: {self.depredador.vida} \U0001F4CC: {self.pos_depre}")
        if self.alien.vida <= 0:
            print("---------------------------------------------JUEGO TERMINADO, EL DEPREDADOR "
                  "GANÓ------------------------------")
        if self.depredador.vida <= 0:
            print("---------------------------------------------JUEGO TERMINADO, EL ALIEN "
                  "GANÓ------------------------------------")


class Alien:
    def __init__(self):
        self.emoji = f" \U0001F47D"
        self.vida = 50


class Depredador:
    def __init__(self):
        self.emoji = f" \U0001F916"
        self.vida = 50


depredador = Depredador()
alien = Alien()


matrix = Matrix(10, 10)
matrix.posicion_alien()
print(matrix.display())
while matrix.alien.vida > 0 or matrix.depredador.vida > 0:
    matrix.mover_alien()
    if alien.vida <= 0 or depredador.vida <= 0:
        break
