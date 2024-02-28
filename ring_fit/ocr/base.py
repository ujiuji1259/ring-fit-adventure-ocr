from abc import ABC, abstractmethod


class FitResultOcr(ABC):

    @abstractmethod
    def get_fit_result(self, image: bytes):
        raise NotImplementedError()
