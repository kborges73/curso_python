from abc import ABC, abstractmethod
class MidiaPlayerMixin(ABC):

    @abstractmethod
    def play(self, midia):
        pass

    def pause(self):
        print("Mídia pausada.")

    def stop(self):
        print("Mídia parada.")