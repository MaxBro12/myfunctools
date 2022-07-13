import random
import copy


# ! Списки
# ? Перекрутка списка
def list_rewind(list_of_val: list, rewind_val: int) -> list:
    return list_of_val[rewind_val:] + list_of_val[:rewind_val]


# ? Поворот матрицы
def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]


# ? Возврат значения в пределах максимального или минимального
def clamp(value, Min, Max):
    return max(min(value, Max), Min)


# ? Возвращает значение из массива, на основе порядкого индекса
def massive_value_backer(massive, index: int):
    return massive[index // 3][index % 3]


# ? Возвращает индексы из массива, на основе порядкого индекса
def massive_index_backer(massive, index: int):
    return index // len(massive), index % massive[0]


# ? Возвращает индекс самого большого значения в списке
def max_value_index(list_of_val: list):
    j = index = 0
    for i in range(len(list_of_val)):
        if j < list_of_val[i]:
            j = list_of_val[i]
            index = i
    return index


# ? Возвращает индекс самого маленького значения в списке
def min_value_index(list_of_val: list):
    j = index = 0
    for i in range(len(list_of_val)):
        if j > list_of_val[i]:
            j = list_of_val[i]
            index = i
    return index


# ? Перевод массива в список
def massive_to_list(massive):
    answer = []
    for i in massive:
        for j in i:
            answer.append(j)
    return answer


# ? Перевод списка в массив
def list_to_massive(list_of_val: list, x: int, y: int):
    answer = []
    for i in range(1, y + 1):
        ans_list = list_of_val[i * x - x:i * x]
        answer.append(ans_list)
    return answer


# ! Методы поиска
# ? Бинарный поиск совпадений 
def matches_b(list_of_val: list):
    a = set(list_of_val)
    if len(a) < len(list_of_val):
        return False
    return True


# ? Полноценный поиск совпадений в списке
def matches_f(list_of_val: list):
    list_of_matches = []
    for i in list_of_val:
        if i in list_of_matches: continue
        if list_of_val.count(i) > 1: list_of_matches.append(i)
    if len(list_of_matches) > 0:
        return list_of_matches
    return False


# ! Векторы
# ? Вектор с 2мя координатами
class Vec2:
    def __init__(self, x='0', y=0):
        if type(x) == tuple or type(x) == list:
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = int(x)
            self.y = y
        self.__x_norm = 0
        self.__y_norm = 0

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @property
    def norm(self):
        self.__x_norm = self.x / self.length()
        self.__y_norm = self.y / self.length()
        return self.__x_norm, self.__y_norm

    def __add__(self, other):
        if type(other) == Vec3:
            return self.x + other.x, self.y + other.y
        elif type(other) == tuple or type(other) == list:
            return self.x + other[0], self.y + other[1]
        else:
            return self.x + other, self.y + other

    def __sub__(self, other):
        if type(other) == Vec3:
            return self.x - other.x, self.y - other.y
        elif type(other) == tuple or type(other) == list:
            return self.x - other[0], self.y - other[1]
        else:
            return self.x - other, self.y - other

    def __mul__(self, other):
        if type(other) == Vec3:
            return self.x * other.x, self.y * other.y
        elif type(other) == tuple or type(other) == list:
            return self.x * other[0], self.y * other[1]
        else:
            return self.x * other, self.y * other

    def __div__(self, other):
        if type(other) == Vec3:
            return self.x / other.x, self.y / other.y
        elif type(other) == tuple or type(other) == list:
            return self.x / other[0], self.y / other[1]
        else:
            return self.x / other, self.y / other

    def __str__(self):
        return self.x, self.y


# ? Вектор с 3мя координатами
class Vec3:
    def __init__(self, x='0', y=0, z=0):
        if type(x) == tuple or type(x) == list:
            self.x = x[0]
            self.y = x[1]
            self.z = x[2]
        else:
            self.x = int(x)
            self.y = y
            self.z = z
        self.__x_norm = 0
        self.__y_norm = 0
        self.__z_norm = 0

    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    @property
    def norm(self):
        self.__x_norm = self.x / self.length()
        self.__y_norm = self.y / self.length()
        self.__z_norm = self.z / self.length()
        return self.__x_norm, self.__y_norm, self.__z_norm

    def __add__(self, other):
        if type(other) == Vec3:
            return self.x + other.x, self.y + other.y, self.z + other.z
        elif type(other) == tuple or type(other) == list:
            return self.x + other[0], self.y + other[1], self.z + other[2]
        else:
            return self.x + other, self.y + other, self.z + other

    def __sub__(self, other):
        if type(other) == Vec3:
            return self.x - other.x, self.y - other.y, self.z - other.z
        elif type(other) == tuple or type(other) == list:
            return self.x - other[0], self.y - other[1], self.z - other[2]
        else:
            return self.x - other, self.y - other, self.z - other

    def __mul__(self, other):
        if type(other) == Vec3:
            return self.x * other.x, self.y * other.y, self.z * other.z
        elif type(other) == tuple or type(other) == list:
            return self.x * other[0], self.y * other[1], self.z * other[2]
        else:
            return self.x * other, self.y * other, self.z * other

    def __div__(self, other):
        if type(other) == Vec3:
            return self.x / other.x, self.y / other.y, self.z / other.z
        elif type(other) == tuple or type(other) == list:
            return self.x / other[0], self.y / other[1], self.z / other[2]
        else:
            return self.x / other, self.y / other, self.z / other

    def __str__(self):
        return self.x, self.y, self.z


# ? Функция расчета нормализированного вектора 2
def norm2(vec2):
    m = length3(vec2)
    return vec2.x / m, vec2.y / m


# ? Функция расчета нормализированного вектора 3
def norm3(vec3):
    m = length3(vec3)
    return vec3.x / m, vec3.y / m, vec3.z / m


# ? Функция расчета длинны вектора 2
def length2(vec2):
    return (vec2.x**2 + vec2.y**2)**0.5


# ? Функция расчета длинны вектора 3
def length3(vec3):
    return (vec3.x**2 + vec3.y**2 + vec3.z**2)**0.5


# ? Функция расчета сколярного произведения вектора 2
def dot2(a, b):
    return a.x * b.x + a.y * b.y


# ? Функция расчета сколярного произведения вектора 3
def dot3(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z


# ! СТРУКТУРЫ ДАННЫХ
# ? Стек - Stack
class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if len(self.__stack) < 1:
            return None
        return self.__stack.pop()

    @property
    def stack(self):
        return self.__stack

    @property
    def size(self):
        return len(self.__stack)

    def __len__(self):
        return len(self.__stack)


# ? Очередь - Queue
class Queue:
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        if len(self.__queue) == 0:
            return None
        return self.queue.pop(0)

    @property
    def queue(self):
        return self.__queue

    @property
    def size(self):
        return len(self.__queue)

    def __len__(self):
        return len(self.__queue)


# ? Очередь с приоритетом - Priority Queue
class PQueueNode:
    def __init__(self, data, priority: int):
        self.data = data
        self.priority = priority


class PQueue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item, priority: int):
        item = PQueueNode(item, priority)
        self.__queue.append(item)
        self.__queue.sort(key=lambda x: x.priority, reverse=True)

    def dequeue(self):
        if len(self.__queue) == 0:
            return None
        return self.queue.pop(0)

    @property
    def queue(self):
        return self.__queue

    @property
    def size(self):
        return len(self.__queue)

    def __len__(self):
        return len(self.__queue)


# ? Связные Списки - Linked lists
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.__list = []

    def append(self, item: LinkedListNode):
        self.__list[-1].next = item
        self.__list.append(item)

    @property
    def list(self):
        return self.__list

    @property
    def tail(self):
        return self.__list[-1]

    @property
    def size(self):
        return len(self.__list)

    def __len__(self):
        return len(self.__list)


# ? Циркулярно Связанные Списки - Circularly Linked Lists
class CircListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircList:
    def __init__(self, head):
        self.head = head
        self.__list = []

    def append(self, item: CircListNode):
        self.__list[-1].next = item
        item.next = self.__list[0]
        self.__list.append(item)

    @property
    def list(self):
        return self.__list

    @property
    def tail(self):
        return self.__list[-1]

    @property
    def size(self):
        return len(self.__list)

    def __len__(self):
        return len(self.__list)


# ? Бинарное дерево - Binary Tree
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = data
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = data
            else:
                self.right.insert(data)
        else:
            return False

    def traversePreOrder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.data, end=' ')
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.data, end=' ')


# ? Хеш Таблица - Hash Table
class HashTable:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__slots = [None] * self.__capacity

    def hashfunction(self, key: int):
        return key % self.__capacity

    def insert(self, key: int, data):
        self.__slots[self.hashfunction(key)] = data

    def remove(self, key: int):
        self.__slots[self.hashfunction(key)] = None

    @property
    def filling_percentage(self):
        return list(map(lambda x: x is None, self.__slots)).count(True) / self.__capacity * 100

    @property
    def capacity(self):
        return self.__capacity

    @property
    def slots(self):
        return self.__slots


# ? Ненаправленные Графы - Undirected Graphs
class Graphs:
    def __init__(self, data, connections: list):
        self.data = data
        self.connections = connections


# ! Нейросети
# ? Нейрон
class Neuron:
    def __init__(self, weight: list = None, bias: float or int = 0, mutation_chance: int = 0, mutation_step: int = 0,
                 neuron=None):
        if neuron is None:
            if weight is None:
                weight = [i for i in range(1)]
            self.weight = copy.copy(weight)
            self.bias = copy.copy(bias)
            self.mutation_chance = copy.copy(mutation_chance)
            self.mutation_step = copy.copy(mutation_step)
        else:
            self.weight = copy.copy(neuron.weight)
            self.bias = copy.copy(neuron.bias)
            self.mutation_chance = copy.copy(neuron.mutation_chance)
            self.mutation_step = copy.copy(neuron.mutation_step)

    @staticmethod
    def sigmoid(val):
        return 1 / (1 + (2.718281828459045 ** - val))

    def feedforward(self, inputs: list):
        base_val = 0
        for i in range(len(inputs)):
            base_val += inputs[i] * self.weight[i]
        return self.sigmoid(base_val + self.bias)

    @property
    def tuning(self):
        return self.weight, self.bias, self.mutation_chance, self.mutation_step

    @property
    def console_log(self):
        return f'{self}\nWeight: {self.weight}\nBias: {self.bias}\nMutation chance: {self.mutation_chance} % \n' \
               f'Mutation step: {self.mutation_step}\n'

    def mutation(self):
        mutated = False
        for i in range(len(self.weight)):
            if self.random_int(0, 100) <= self.mutation_chance:
                self.weight[i] += self.random_int(-self.mutation_step, self.mutation_step) * self.weight[i] / 100
                mutated = True
        if self.random_int(0, 100) <= self.mutation_chance:
            self.bias += self.random_int(-self.mutation_step, self.mutation_step) * self.bias / 100
            mutated = True
        return mutated

    def __and__(self, other):
        new_weights = []
        for i in range(len(self.weight)):
            new_weights.append((self.weight[i] + other.weight[i]) / 2)
        return Neuron(new_weights, (self.bias + other.bias) / 2, self.mutation_chance, self.mutation_step)

    @staticmethod
    def random_int(a: int = 0, b: int = 1):
        val = random.randint(a, b)
        return val


# ? Нейроная сеть
class Neural_Network:
    def __init__(self, number_of_inputs: int = 2, hidden_layers_count: int = 0, hidden_layer_sizes: list = None,
                 output_layer_size: int = 1, tuning_for_Neuron: list = None, neural_network=None):
        if neural_network is None:
            if tuning_for_Neuron is None:
                tuning_for_Neuron = [1, 0, 0]

            input_weights = [1 for i in range(number_of_inputs)]

            self.layers = []
            for i in range(hidden_layers_count):
                if i == 0:
                    layer = []
                    for j in range(hidden_layer_sizes[i]):
                        layer.append(Neuron(input_weights, tuning_for_Neuron[0], tuning_for_Neuron[1],
                                            tuning_for_Neuron[2]))
                    self.layers.append(layer)
                if i > 0:
                    layer = []
                    for j in range(hidden_layer_sizes[i]):
                        layer.append(Neuron([1 for i in range(len(self.layers[i - 1]))], tuning_for_Neuron[0], tuning_for_Neuron[1],
                                            tuning_for_Neuron[2]))
                    self.layers.append(layer)
            if hidden_layers_count == 0:
                layer = []
                for j in range(output_layer_size):
                    layer.append(
                        Neuron(input_weights, tuning_for_Neuron[0], tuning_for_Neuron[1],
                               tuning_for_Neuron[2]))
                self.layers.append(layer)
            else:
                layer = []
                for j in range(output_layer_size):
                    layer.append(
                        Neuron([1 for i in range(len(self.layers[len(self.layers) - 1]))], tuning_for_Neuron[0], tuning_for_Neuron[1],
                               tuning_for_Neuron[2]))
                self.layers.append(layer)
            self.inputs_cont = number_of_inputs
            self.hidden_layers_count = hidden_layers_count
            self.output_count = output_layer_size
            self.neuron_base_bias = tuning_for_Neuron[0]
            self.neuron_base_mut_c = tuning_for_Neuron[1]
            self.neuron_base_mut_s = tuning_for_Neuron[2]
        else:
            self.layers = []
            for i in neural_network.layers:
                s_layer = []
                for j in i:
                    s_layer.append(Neuron(neuron=j))
                self.layers.append(s_layer)
            self.inputs_cont = neural_network.inputs_cont
            self.hidden_layers_count = neural_network.hidden_layers_count
            self.output_count = neural_network.output_count
            self.neuron_base_bias = neural_network.neuron_base_bias
            self.neuron_base_mut_c = neural_network.neuron_base_mut_c
            self.neuron_base_mut_s = neural_network.neuron_base_mut_s

    @property
    def console_log(self):
        log = f'\t____Neural Network____\n{self}\nInputs len: {self.inputs_cont}\nHidden layers: {self.hidden_layers_count}\nOutput len: {self.output_count}\n\n'
        if self.hidden_layers_count != 0:
            for i in range(self.hidden_layers_count):
                log += f'\tHidden layer {i}:\n'
                for j in self.layers[i]:
                    log += j.console_log + '\n'
        log += '\tOutput layer:\n'
        for i in self.layers[len(self.layers) - 1]:
            log += i.console_log + '\n'
        return log

    def feedforward(self, inputs):
        FAQ = []
        for i in range(len(self.layers)):
            if i == 0:
                inp_ans = []
                for j in self.layers[i]:
                    inp_ans.append(j.feedforward(inputs))
                FAQ = inp_ans
            else:
                ans = []
                for j in self.layers[i]:
                    ans.append(j.feedforward(FAQ))
                FAQ = ans
        return FAQ

    def mutation(self):
        for layer in range(len(self.layers)):
            for n in range(len(self.layers[layer])):
                self.layers[layer][n].mutation()

    def __and__(self, other):
        new = Neural_Network(self.inputs_cont, self.hidden_layers_count,
                             [len(self.layers[i]) for i in range(len(self.layers) - 1)],
                             len(self.layers[len(self.layers) - 1]),
                             [self.neuron_base_bias, self.neuron_base_mut_c, self.neuron_base_mut_s])
        for i in range(len(self.layers)):
            for j in range((len(self.layers[i]))):
                new.layers[i][j] = self.layers[i][j] & other.layers[i][j]
        return new

    def save(self):
        file = open('Network.ini', 'w')
        try:
            save = str(self.inputs_cont) + '\n'
            save += str(self.hidden_layers_count) + '\n'
            save += str(self.output_count) + '\n'
            save += str(self.neuron_base_bias) + '\n'
            save += str(self.neuron_base_mut_c) + '\n'
            save += str(self.neuron_base_mut_s) + '\n'
            for i in self.layers:
                s_line = ''
                for j in i:
                    s_line += str(j.weight) + ' ' + str(j.bias)
                s_line += '\n'
                save += s_line
            file.write(save)
        finally:
            file.close()

    def load(self):
        file = open('Network.ini', 'r')
        try:
            text = file.readlines()
            for i in range(len(text)):
                text[i] = text[i].replace('\n', '')
            self.inputs_cont = int(text[0])
            self.hidden_layers_count = int(text[1])
            self.output_count = int(text[2])
            self.neuron_base_bias = int(text[3])
            self.neuron_base_mut_c = int(text[4])
            self.neuron_base_mut_s = int(text[5])
            self.layers = []
            for i in range(6, len(text)):
                layer = []
                text[i] = text[i].replace(',','')
                text[i] = text[i].split('[')
                for j in range(len(text[i])):
                    text[i][j] = text[i][j].replace(']', '')
                    text[i][j] = text[i][j].split(' ')
                    
                    if j != 0:
                        weights = []
                        bias_l = 0
                        bias_l = float(text[i][j][len(text[i][j]) -1])
                        for n in range(len(text[i][j]) - 1):
                            weights.append(float(text[i][j][n]))
                        layer.append(Neuron(weights, bias_l, self.neuron_base_mut_c, self.neuron_base_mut_s))
                self.layers.append(layer)
        finally:
            file.close()

    def randomise(self, Min: int, Max: int):
        for layer in self.layers:
            for neuron in layer:
                for i in range(len(neuron.weight)):
                    a = random.randint(Min, Max)
                    neuron.weight[i] = a


class Neuron_P:
    def __init__(self,
                 number_of_inputs: int = 2,
                 weight: list = None,
                 bias: bool = True,
                 mutation_chance: int = 0,
                 mutation_step: int = 0,
                 neuron=None):
        if neuron is None:
            if weight is None:
                weight = [1 for _ in range(number_of_inputs)]
            self.weight = copy.copy(weight)
            if bias is True:
                self.bias = 1
            else:
                self.bias = 0
            self.inputs = []
            self.mutation_chance = copy.copy(mutation_chance)
            self.mutation_step = copy.copy(mutation_step)
        else:
            self.weight = copy.copy(neuron.weight)
            self.bias = neuron.bias
            self.mutation_chance = copy.copy(neuron.mutation_chance)
            self.mutation_step = copy.copy(neuron.mutation_step)

    def set_inputs(self, inputs: list):
        self.inputs = inputs
        if self.bias == 1:
            self.inputs.append(self.bias)

    def mutation(self):
        for i in range(len(self.weight)):
            if self.random_int(0, 100) <= self.mutation_chance:
                self.weight[i] += self.random_int(-self.mutation_step, self.mutation_step) * self.weight[i] / 100

    @property
    def feedforward(self):
        ans = 0
        for i in range(len(self.weight)):
            if type(self.inputs[i]) is Neuron_P:
                ans += self.inputs[i].feedforward * self.weight[i]
            else:
                ans += self.inputs[i] * self.weight[i]
        return self.sigmoid(ans)

    @property
    def tuning(self):
        return self.inputs, self.weight, self.bias, self.mutation_chance, self.mutation_step

    @property
    def console_log(self):
        return f'{self}\nInputs: {self.inputs}\nWeight: {self.weight}\nBias:' \
               f'{self.bias}\nMutation chance: {self.mutation_chance} % \n' \
               f'Mutation step: {self.mutation_step}\n'

    @staticmethod
    def random_int(min_value, max_value):
        return random.randint(min_value, max_value)

    @staticmethod
    def sigmoid(val):
        return 1 / (1 + (2.7182818284590452353602874713527 ** - val))

    @staticmethod
    def threshold(input_val, min_val):
        if input_val > min_val:
            return 1
        return 0


class Neural_Network_P:
    def __init__(self,
                 number_of_inputs: int = 2,
                 layer_sizes: list = None,
                 tuning_for_neuron: list = None,
                 neural_network=None):
        if tuning_for_neuron is None:
            tuning_for_neuron = [True, 0, 0]
        self.layers = []
        self.tunes = tuning_for_neuron
        if neural_network is None:
            for i in range(len(layer_sizes)):
                layer = []
                for j in range(layer_sizes[i]):
                    if i == 0:
                        weights = [1 for _ in range(number_of_inputs + 1)]
                        layer.append(Neuron_P(number_of_inputs,
                                              weights,
                                              tuning_for_neuron[0],
                                              tuning_for_neuron[1],
                                              tuning_for_neuron[2]))
                    else:
                        inputs = len(self.layers[i - 1])
                        weights = [1 for _ in range(len(self.layers[i - 1]) + 1)]
                        layer.append(Neuron_P(inputs,
                                              weights,
                                              tuning_for_neuron[0],
                                              tuning_for_neuron[1],
                                              tuning_for_neuron[2]))
                        layer[j].set_inputs(self.layers[i - 1])
                self.layers.append(layer)
        else:
            self.layers = copy.copy(neural_network.layers)
            self.tunes = copy.copy(neural_network.tunes)

    def feedforward(self):
        FAQ = []
        # for layer in self.layers:
        #     ans = []
        #     for neuron in layer:
        #         ans.append(neuron.feedforward)
        #     FAQ = ans
        for neuron in self.layers[len(self.layers) - 1]:
            FAQ = neuron.feedforward()

        return FAQ

    def mutation(self):
        for layer in range(len(self.layers)):
            for n in range(len(self.layers[layer])):
                self.layers[layer][n].mutation()
