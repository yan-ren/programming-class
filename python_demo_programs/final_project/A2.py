def get_unique_input(msg):
    while True:
        values = list(map(float, input(msg).split()))

        if len(values) != 10:
            print('Not enough values')
            continue

        unique_values = []
        for val in values:
            if val not in unique_values:
                unique_values.append(val)

        while len(unique_values) < 10:
            missing = 10 - len(unique_values)
            print(f'{missing} duplicate(s) found')
            extra = float(input('Enter a replace value:'))
            if extra not in unique_values:
                unique_values.append(extra)
            else:
                print('Value already exists, Enter a unique value')

        return unique_values


import matplotlib.pyplot as plt

PLANCK_CONSTANT = 6.626e-34

def main():
    print("Choose two known variables from: 'wavelength', 'frequency', 'speed'")
    knowns = input("Enter the two known variables: ").lower().split()

    if len(knowns) != 2 or any(k not in ['wavelength', 'frequency', 'speed'] for k in knowns):
        print("Invalid input. Please choose exactly two from 'wavelength', 'frequency', 'speed'")
        return

    values = {}
    for var in knowns:
        values[var] = get_unique_input(f'Enter 10 unique values for {var}, separated by spaces:\n')

    # Calculate third property using loops
    if 'wavelength' in values and 'frequency' in values:
        speed_list = []
        for i in range(10):
            speed = values['frequency'][i] * values['wavelength'][i]
            speed_list.append(speed)
        values['speed'] = speed_list
    elif 'wavelength' in values and 'speed' in values:
        frequency_list = []
        for i in range(10):
            frequency = values['speed'][i] / values['wavelength'][i]
            frequency_list.append(frequency)
        values['frequency'] = frequency_list
    elif 'frequency' in values and 'speed' in values:
        wavelength_list = []
        for i in range(10):
            wavelength = values['speed'][i] / values['frequency'][i]
            wavelength_list.append(wavelength)
        values['wavelength'] = wavelength_list

    # Calculate energy using loop
    frequency = values['frequency']
    energy = []
    for f in frequency:
        e = PLANCK_CONSTANT * f
        energy.append(e)

    # First plot: known variables
    x = values[knowns[0]]
    y = values[knowns[1]]

    # Determine units for x-axis
    if knowns[0] == 'frequency':
        x_unit = 'Hz'
    elif knowns[0] == 'speed':
        x_unit = 'm/s'
    else:
        x_unit = 'm'

    # Determine units for y-axis
    if knowns[1] == 'frequency':
        y_unit = 'Hz'
    elif knowns[1] == 'speed':
        y_unit = 'm/s'
    else:
        y_unit = 'm'

    # Plot
    plt.scatter(x, y, color='blue', label='Wave Data')
    plt.xlabel(f"{knowns[0].capitalize()} ({x_unit})")
    plt.ylabel(f"{knowns[1].capitalize()} ({y_unit})")
    plt.title("Wave Concept Scatter Plot")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Second plot: Energy vs Frequency
    plt.scatter(frequency, energy, color='red', label='Energy vs Frequency')
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Energy (J)")
    plt.title("Wave Energy vs Frequency")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

