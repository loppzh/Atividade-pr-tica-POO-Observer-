from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, valor1, valor2):
        pass

class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = []
        self._valor1 = 0
        self._valor2 = 0

    def register_observer(self, observer: Observer):
        print(">> Sujeito: Observador registrado.")
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        print(">> Sujeito: Observador removido.")
        self._observers.remove(observer)

    def notify_observers(self):
        print(">> Sujeito: Notificando observadores...")
        for observer in self._observers:
            observer.update(self._valor1, self._valor2)

    def set_valores(self, valor1: int, valor2: int):
        print(f"\n>> Sujeito: Valores alterados para ({valor1}, {valor2})")
        self._valor1 = valor1
        self._valor2 = valor2
        self.notify_observers()

    def get_valores(self):
        return self._valor1, self._valor2

class DivObserver(Observer):
    def update(self, valor1: int, valor2: int):
        if valor2 != 0:
            resultado = valor1 // valor2
            print(f"  -> DivObserver: A divisão inteira de {valor1} por {valor2} é {resultado}.")
        else:
            print("  -> DivObserver: Divisão por zero não é permitida.")

class ModObserver(Observer):
    def update(self, valor1: int, valor2: int):
        if valor2 != 0:
            resultado = valor1 % valor2
            print(f"  -> ModObserver: O resto da divisão de {valor1} por {valor2} é {resultado}.")
        else:
            print("  -> ModObserver: Divisão por zero não é permitida.")

class MultObserver(Observer):
    def update(self, valor1: int, valor2: int):
        resultado = valor1 * valor2
        print(f"  -> MultObserver: A multiplicação de {valor1} por {valor2} é {resultado}.")

if __name__ == "__main__":
    print("--- INÍCIO - PARTE 1: OPERAÇÕES MATEMÁTICAS ---")
    sujeito = ConcreteSubject()
    obs_div = DivObserver()
    obs_mod = ModObserver()
    obs_mult = MultObserver()
    sujeito.register_observer(obs_div)
    sujeito.register_observer(obs_mod)
    sujeito.register_observer(obs_mult)
    sujeito.set_valores(10, 3)
    sujeito.set_valores(25, 5)
    sujeito.remove_observer(obs_mod)
    sujeito.set_valores(100, 10)
    print("--- FIM - PARTE 1 ---")
