import numpy as np
import matplotlib.pyplot as plt

def trimf(x, params):
    a, b, c = params
    return np.maximum(0, np.minimum((x - a) / np.maximum(1e-10, b - a), (c - x) / np.maximum(1e-10, c - b)))

def main():
    x = np.linspace(-np.pi, np.pi, 200)
    plt.figure(figsize=(15, 6))
    
    # Pierwotne
    small_deviation = np.maximum(trimf(x, [-np.pi, -np.pi, -np.pi/6]), trimf(x, [0, np.pi/6, np.pi]))
    medium_deviation = trimf(x, [-np.pi/6, 0, np.pi/6])
    large_deviation = np.maximum(trimf(x, [-np.pi/3, -np.pi/6, 0]), trimf(x, [np.pi/6, np.pi/3, np.pi/2]))

    approximated_sin1 = np.zeros_like(x)
    for i in range(len(x)):
        activation_small = np.minimum(small_deviation[i], np.sin(x[i]))
        activation_medium = np.minimum(medium_deviation[i], np.sin(x[i]))
        activation_large = np.minimum(large_deviation[i], np.sin(x[i]))
        
        aggregated = np.max([activation_small, activation_medium, activation_large])
        
        if aggregated != 0:
            approximated_sin1[i] = np.sum(x * aggregated) / np.sum(aggregated)
        else:
            approximated_sin1[i] = 0

    # Dodane
    small_deviation2 = trimf(x, [-np.pi, -np.pi, -2*np.pi/3])
    medium_small_deviation2 = trimf(x, [-2*np.pi/3, -np.pi/3, 0])
    medium_deviation2 = trimf(x, [-np.pi/3, 0, np.pi/3])
    medium_large_deviation2 = trimf(x, [0, np.pi/3, 2*np.pi/3])
    large_deviation2 = trimf(x, [2*np.pi/3, np.pi, np.pi])

    approximated_sin2 = np.zeros_like(x)
    for i in range(len(x)):
        activation1 = np.minimum(small_deviation2[i], np.sin(x[i]))
        activation2 = np.minimum(medium_small_deviation2[i], np.sin(x[i]))
        activation3 = np.minimum(medium_deviation2[i], np.sin(x[i]))
        activation4 = np.minimum(medium_large_deviation2[i], np.sin(x[i]))
        activation5 = np.minimum(large_deviation2[i], np.sin(x[i]))
        
        aggregated = np.max([activation1, activation2, activation3, activation4, activation5])
        
        if aggregated != 0:
            approximated_sin2[i] = np.sum(x * aggregated) / np.sum(aggregated)
        else:
            approximated_sin2[i] = 0

    plt.subplot(2, 1, 1)
    plt.plot(x, np.sin(x), 'b', label='sin(x)', linewidth=2)
    plt.plot(x, approximated_sin1, 'r', label='3 reguły', linewidth=2)
    plt.plot(x, approximated_sin2, 'g', label='5 reguł', linewidth=2)
    plt.title('Porównanie aproksymacji')
    plt.legend(loc='upper right')

    plt.subplot(2, 1, 2)

    plt.plot(x, small_deviation, 'r--', linewidth=1, alpha=0.5)
    plt.plot(x, medium_deviation, 'r--', linewidth=1, alpha=0.5)
    plt.plot(x, large_deviation, 'r--', linewidth=1, alpha=0.5)

    plt.plot(x, small_deviation2, 'g', linewidth=1)
    plt.plot(x, medium_small_deviation2, 'g', linewidth=1)
    plt.plot(x, medium_deviation2, 'g', linewidth=1)
    plt.plot(x, medium_large_deviation2, 'g', linewidth=1)
    plt.plot(x, large_deviation2, 'g', linewidth=1)
    plt.title('Zbiory rozmyte (czerwony - 3 reguły, zielony - 5 reguł)')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()