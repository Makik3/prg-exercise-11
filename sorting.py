import random
import matplotlib.pyplot as plt


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

values = random_numbers(10)  # 10 čísel v rozsahu 0–100
print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
print(small)

# Selection Sort patří mezi jednoduché nestabilní řadicí algoritmy. Jeho výhodou je nízká paměťová náročnost — pracuje přímo v původním seznamu, bez pomocných kopií.
def selection_sort(values):
    for j in range(len(values)):
        min_index = j
        min_value = values[min_index]
        for i in range(j + 1, len(values)):   # nulu už mám uloženou, začnu od jedničky
            if values[i] < min_value:
                min_index = i
                min_value = values[i]
        #print(min_index)       # výstup je cislo 7
        values[j], values[min_index] = values[min_index], values[j]
    return values
print(selection_sort(values))


def bubble_sort(seznam_cisel):
    plt.ion()
    plt.show()

    for j in range(len(seznam_cisel)):
        swapped = False
        for i in range(1, len(seznam_cisel)):
            index_highlight1 = i - 1
            index_highlight2 = i
            colors = ["steelblue"] * len(seznam_cisel)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(seznam_cisel)), seznam_cisel, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if seznam_cisel[i] < seznam_cisel[i-1]:
                seznam_cisel[i], seznam_cisel[i-1] = seznam_cisel[i-1], seznam_cisel[i]
                swapped = True
        if swapped == False:
            return seznam_cisel

    plt.ioff()
    plt.show()

print(bubble_sort([42, 7, 91, 15, 63, 8, 57, 73, 2, 100]))


if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20