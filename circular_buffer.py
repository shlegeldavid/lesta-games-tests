from collections import deque


class CircularBuffer:
    def __init__(self, size):
        self.buffer=[None] * size
        self.max_size=size
        self.head = 0
        self.tail = 0
        self.full = False


    def enqueue(self, item):
        if self.full:
            raise OverflowError('Buffer is full')
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        if self.tail == self.head:
            self.full = True


    def dequeue(self):
        if self.is_empty():
            raise IndexError('Buffer is empty')
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.full = False
        return item


    def is_empty(self):
        return not self.full and self.head == self.tail


    def is_full(self):
        return self.full


    def __repr__(self):
        return f'CircularBuffer({self.buffer})'


class CircularBufferDeque:
    def __init__(self, size):
        self.buffer = deque(maxlen = size)
    

    def enqueue(self, item):
        self.buffer.append(item)


    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()


    def is_empty(self):
        return len(self.buffer) == 0


    def is_full(self):
        return len(self.buffer) == self.buffer.maxlen


    def __repr__(self):
        return f'CircularBufferDeque({list(self.buffer)})'


#В первом случае circular buffer реализуется с помощью списка.
#Реализация списком имеет плюсы:
    #Код простой и читаемый.
    #В случае пустоты/полноты списка вызываются ошибки - это дает полный контроль над буфером.
#Минусы:
    #Приходится тратить ресурсы на вычисление индексов.
    #Размер зафиксирован таким образом, что даже неиспользуемые ячейки буфера занимают память.


#Во втором случае реализация происходит засчет встроенного метода deque.
#Реализация deque имеет плюсы:
    #Автоматическое удаление старых элементов.
    #Простота - это встроенная библиотека python, дополнительная реализация не требуется.
#Минусы:
    #Неожиданное поведение - удаление старых элементов автоматически может привести к ошибкам.
    #Создается дополнительных уровень абстракции, что может быть избыточно (это скорее и не минус, и не плюс)


#Быстродействие:Оба алгоритма выполняют вставку и чтение за O(1), но реализация списком все равно немного медленее
# из-за дополнительных операций вычисления индексов.