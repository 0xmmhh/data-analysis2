import numpy as np
import matplotlib.pyplot as plt


# Funkcja do generowania funkcji przynależności trapezoidalnych

def trapezoidal(x, a, b, c, d):
    return np.maximum(0, np.minimum((x-a)/(b-a), np.minimum(1, (d-x)/(d-c))))

# Zakresy dla parametrów
x_temp = np.linspace(18, 29, 500)  # temperatura
x_size = np.linspace(10, 25, 500)  # wielkość pomieszczenia
x_power = np.linspace(0, 100, 500)  # moc klimatyzacji

# Funkcje przynależności dla temperatury
temp_low = trapezoidal(x_temp, 18, 18, 21, 23)
temp_medium = trapezoidal(x_temp, 21, 23, 25, 27)
temp_high = trapezoidal(x_temp, 25, 27, 29, 35)

# Funkcje przynależności dla wielkości pomieszczenia
size_small = trapezoidal(x_size, 10, 10, 13, 16)
size_medium = trapezoidal(x_size, 13, 16, 19, 22)
size_large = trapezoidal(x_size, 19, 22, 25, 35)

# Funkcje przynależności dla mocy klimatyzacji
power_low = trapezoidal(x_power, 0, 0, 20, 40)
power_medium = trapezoidal(x_power, 20, 40, 60, 80)
power_high = trapezoidal(x_power, 60, 80, 100, 100)

x = 21.5
y1 = 0
y2 = 1

x2 = 18
x3 = 10
y3 = 0.247
y4 = 0.738
y5 = 0.175
y6 = 0.835

# Wykresy dla temperatury
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(x_temp, temp_low, label='Niska (Low)')
plt.plot(x_temp, temp_medium, label='Średnia (Medium)')
plt.plot(x_temp, temp_high, label='Wysoka (High)')
plt.vlines(x=x, ymin=y1, ymax=y2, color='grey', linestyle='--', label='Vertical Line')
plt.hlines(y=y3, xmin=x2, xmax=x, color='grey', linestyle='--', label='Horizontal Line')
plt.hlines(y=y4, xmin=x2, xmax=x, color='grey', linestyle='--', label='Horizontal Line')
plt.title("Funkcje Rozmycia dla temperatury")
plt.xlabel("Temperatura [°C]")
plt.ylabel("Stopień Rozmycia")
# plt.legend()

# Wykresy dla wielkości pomieszczenia
plt.subplot(1, 3, 2)
plt.plot(x_size, size_small, label='Małe (Small)')
plt.plot(x_size, size_medium, label='Średnie (Medium)')
plt.plot(x_size, size_large, label='Duże (Large)')
plt.vlines(x=x, ymin=y1, ymax=y2, color='grey', linestyle='--', label='Vertical Line')
plt.hlines(y=y5, xmin=x3, xmax=x, color='grey', linestyle='--', label='Horizontal Line')
plt.hlines(y=y6, xmin=x3, xmax=x, color='grey', linestyle='--', label='Horizontal Line')
plt.title("Funkcje Rozmycia dla wielkości pomieszczenia")
plt.xlabel("Powierzchnia [m²]")
plt.ylabel("Stopień Rozmycia")
# plt.legend()

# Wykresy dla mocy klimatyzacji
plt.subplot(1, 3, 3)
plt.plot(x_power, power_low, label='Niska (Low)')
plt.plot(x_power, power_medium, label='Średnia (Medium)')
plt.plot(x_power, power_high, label='Wysoka (High)')
plt.hlines(y=y3, xmin=0, xmax=64.91, color='grey', linestyle='--', label='Horizontal Line')
plt.hlines(y=y3, xmin=64.91, xmax=100, color='black', linestyle='-', label='Horizontal Line')
plt.hlines(y=y4, xmin=0, xmax=34, color='grey', linestyle='--', label='Horizontal Line')
plt.hlines(y=y4, xmin=34, xmax=65, color='black', linestyle='-', label='Horizontal Line')
plt.title("Funkcje Rozmycia dla mocy klimatyzacji")
plt.xlabel("Moc [%]")
plt.ylabel("Stopień Rozmycia")
# plt.legend()

plt.tight_layout()
plt.show()