import numpy as np
import matplotlib.pyplot as plt

def trimf(x, params):
    a, b, c = params
    return np.maximum(0, np.minimum((x - a) / np.maximum(1e-10, b - a), (c - x) / np.maximum(1e-10, c - b)))

def main():
    x = np.linspace(-np.pi, np.pi, 200)

    # Eksperymenty: różne parametry funkcji trójkątnych
    small_deviation_1 = np.maximum(trimf(x, [-np.pi, -np.pi, -np.pi/6]), trimf(x, [0, np.pi/6, np.pi]))
    small_deviation_2 = np.maximum(trimf(x, [-np.pi, -np.pi/2, -np.pi/6]), trimf(x, [0, np.pi/4, np.pi/2]))
    
    medium_deviation = trimf(x, [-np.pi/6, 0, np.pi/6])
    large_deviation = np.maximum(trimf(x, [-np.pi/3, -np.pi/6, 0]), trimf(x, [np.pi/6, np.pi/3, np.pi/2]))

    approximated_sin_1 = np.zeros_like(x)
    approximated_sin_2 = np.zeros_like(x)

    for i in range(len(x)):
        # Aktywacja dla pierwszego zestawu parametrów
        activation_small_1 = np.minimum(small_deviation_1[i], np.sin(x[i]))
        activation_medium = np.minimum(medium_deviation[i], np.sin(x[i]))
        activation_large = np.minimum(large_deviation[i], np.sin(x[i]))

        aggregated_1 = np.max([activation_small_1, activation_medium, activation_large])
        if aggregated_1 != 0:
            approximated_sin_1[i] = np.sum(x * aggregated_1) / np.sum(aggregated_1)
        else:
            approximated_sin_1[i] = 0

        # Aktywacja dla drugiego zestawu parametrów
        activation_small_2 = np.minimum(small_deviation_2[i], np.sin(x[i]))
        aggregated_2 = np.max([activation_small_2, activation_medium, activation_large])
        if aggregated_2 != 0:
            approximated_sin_2[i] = np.sum(x * aggregated_2) / np.sum(aggregated_2)
        else:
            approximated_sin_2[i] = 0

    # Wykres wyników aproksymacji
    plt.subplot(2, 1, 1)
    plt.plot(x, np.sin(x), 'b', x, approximated_sin_1, 'r', x, approximated_sin_2, 'g', linewidth=2)
    plt.title('Aproksymacja funkcji sinus dla różnych parametrów')
    plt.legend(['sin(x)', 'Parametry 1', 'Parametry 2'], loc='upper right')

    # Wykres zbiorów rozmytych
    plt.subplot(2, 1, 2)
    plt.plot(x, small_deviation_1, 'r', x, small_deviation_2, 'g', x, medium_deviation, 'b', x, large_deviation, 'orange', linewidth=2)
    plt.title('Zbiory rozmyte dla różnych parametrów')
    plt.legend(['Małe odchylenie 1', 'Małe odchylenie 2', 'Średnie odchylenie', 'Duże odchylenie'], loc='upper right')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
