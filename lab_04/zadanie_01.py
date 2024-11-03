import numpy as np
import matplotlib.pyplot as plt

class CreditScoreController:
    def __init__(self):
        pass

    def evaluate(self, income, credit_history_score):
        score1 = min(income, credit_history_score)  # reguła 1: minimalna ocena na podstawie niższej zmiennej
        score2 = max(income, credit_history_score)  # reguła 2: maksymalna ocena na podstawie wyższej zmiennej
        score3 = 0.7 * income + 0.3 * credit_history_score  # reguła 3: ocena ważona dochodów i historii kredytowej

        # srednia wazona
        credit_score = (score1 + score2 + score3) / 3

        return credit_score

    def plot_membership_functions(self):
        income_range = np.linspace(0, 10, 100)
        credit_history_range = np.linspace(0, 10, 100)

        # Funkcje przynależności dla dochodu
        membership_income = np.minimum(income_range, 10 - income_range)
        
        # Funkcje przynależności dla historii kredytowej
        membership_credit_history = 1 - np.abs(credit_history_range - 5) / 5

        # Rysowanie wykresów funkcji przynależności
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.plot(income_range, membership_income, label='Dochód')
        plt.title('Funkcja przynależności - Dochód')
        plt.xlabel('Dochód')
        plt.ylabel('Przynależność')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(credit_history_range, membership_credit_history, label='Historia kredytowa')
        plt.title('Funkcja przynależności - Historia kredytowa')
        plt.xlabel('Historia kredytowa')
        plt.ylabel('Przynależność')
        plt.legend()

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    credit_score_controller = CreditScoreController()

    # Rysowanie funkcji przynależności
    credit_score_controller.plot_membership_functions()

    # Przykładowe dane wejściowe
    income_input = 8.0  # np. dochód na poziomie 8 w skali 0-10
    credit_history_input = 6.5  # punkty historii kredytowej na poziomie 6.5

    # Ocena zdolności kredytowej
    credit_score = credit_score_controller.evaluate(income_input, credit_history_input)

    # Wyświetlanie wyników
    print(f"Dochód: {income_input}")
    print(f"Historia kredytowa: {credit_history_input}")
    print(f"Oszacowana zdolność kredytowa: {credit_score}")
