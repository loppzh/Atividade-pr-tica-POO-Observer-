from abc import ABC, abstractmethod

class IObservable(ABC):
    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class IObserver(ABC):
    @abstractmethod
    def update(self, subject: IObservable):
        pass

class Reuters(IObservable):
    def __init__(self):
        self._subscribers = []
        self.latest_news = ""

    def subscribe(self, observer: IObserver):
        print(f">> Reuters: Canal '{observer.name}' se inscreveu para receber notícias.")
        self._subscribers.append(observer)

    def unsubscribe(self, observer: IObserver):
        print(f">> Reuters: Canal '{observer.name}' cancelou a inscrição.")
        self._subscribers.remove(observer)

    def notify(self):
        print(">> Reuters: NOTÍCIA URGENTE! Notificando todos os canais...")
        for subscriber in self._subscribers:
            subscriber.update(self)

    def publish_breaking_news(self, news: str):
        self.latest_news = news
        print(f"\n>> Reuters: Publicando nova notícia: '{news}'")
        self.notify()

class NewsChannel(IObserver):
    def __init__(self, name: str):
        self.name = name
        self.latest_news = ""

    def update(self, subject: Reuters):
        self.latest_news = subject.latest_news
        print(f"  -> [{self.name}] URGENTE: 'Repórter ao vivo com a última notícia: {self.latest_news}'")

if __name__ == "__main__":
    print("\n--- INÍCIO - PARTE 2: AGÊNCIA DE NOTÍCIAS ---")
    reuters = Reuters()
    cnn = NewsChannel("CNN Brasil")
    fox_news = NewsChannel("Fox News")
    globo_news = NewsChannel("GloboNews")
    reuters.subscribe(cnn)
    reuters.subscribe(fox_news)
    reuters.publish_breaking_news("Mercado de ações atinge recorde histórico!")
    reuters.subscribe(globo_news)
    reuters.publish_breaking_news("Nova tecnologia de baterias promete revolucionar o mercado de elétricos.")
    reuters.unsubscribe(fox_news)
    reuters.publish_breaking_news("Fim do expediente na agência Reuters.")
    print("--- FIM - PARTE 2 ---")
