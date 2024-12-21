import numpy as np
import matplotlib.pyplot as plt

class CreditRatingController:
    def __init__(self):
        pass

    def evaluate(self, income, credit_score):
        rating1 = min(income, credit_score) 
        rating2 = 0.7 * income + 0.3 * credit_score  
        rating3 = max(income, credit_score)  

        final_rating = (rating1 + rating2 + rating3) / 3
        return final_rating

    def plot_membership_functions(self):
        income_range = np.linspace(0, 10, 100)
        credit_score_range = np.linspace(0, 10, 100)

        membership_income = np.minimum(income_range/5, 2-income_range/5)
        membership_credit = 1 - np.abs(credit_score_range - 5) / 5

        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.plot(income_range, membership_income, label='Dochód')
        plt.title('Dochód')
        plt.xlabel('Dochód')
        plt.ylabel('Stopień przynależności')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(credit_score_range, membership_credit, label='Historia kredytowa')
        plt.title('Historia kredytowa')
        plt.xlabel('Punkty')
        plt.ylabel('Stopień przynależności')
        plt.legend()

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    controller = CreditRatingController()
    
    controller.plot_membership_functions()

    # Przyklad
    income_input = 7.5
    credit_score_input = 6.0

    rating = controller.evaluate(income_input, credit_score_input)

    print(f"Dochód: {income_input}")
    print(f"Historia kredytowa: {credit_score_input}")
    print(f"Ocena zdolności kredytowej: {rating:.2f}")