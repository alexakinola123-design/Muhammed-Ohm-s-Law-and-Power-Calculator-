# Ohm's Law and Power Calculator
# ND1 Mechatronics Engineering - YabaTech
# Author: Bello Muhammed

def calculate_voltage(current, resistance):
    """Calculate voltage using V = I * R"""
    return current * resistance

def calculate_current(voltage, resistance):
    """Calculate current using I = V / R"""
    if resistance == 0:
        return None  # Avoid division by zero
    return voltage / resistance

def calculate_resistance(voltage, current):
    """Calculate resistance using R = V / I"""
    if current == 0:
        return None  # Avoid division by zero
    return voltage / current

def calculate_power(voltage=None, current=None, resistance=None):
    """
    Calculate power. Tries P = V * I first.
    Falls back to P = I²R or P = V²/R when possible.
    """
    if voltage is not None and current is not None:
        return voltage * current
    if current is not None and resistance is not None:
        return (current ** 2) * resistance
    if voltage is not None and resistance is not None:
        if resistance == 0:
            return None
        return (voltage ** 2) / resistance
    return None

def get_float(prompt):
    """Safely get a positive float from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number (or zero where allowed).")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def show_history(history):
    """Display all previous calculations."""
    if not history:
        print("\nNo calculations in history yet.")
        return
    print("\n===== Calculation History =====")
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry}")
    print("===============================")

def main():
    history = []  # stores results of each calculation

    print("=" * 50)
    print("   OHM'S LAW & POWER CALCULATOR")
    print("   (with full related values + history)")
    print("=" * 50)

    while True:
        print("\nWhat would you like to calculate?")
        print("1. Voltage (V)")
        print("2. Current (I)")
        print("3. Resistance (R)")
        print("4. Power (P)")
        print("5. View calculation history")
        print("6. Clear history")
        print("7. Quit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "7":
            print("\nThank you for using the calculator. Goodbye!")
            break

        elif choice == "5":
            show_history(history)
            continue

        elif choice == "6":
            history.clear()
            print("History cleared.")
            continue

        elif choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please enter a number from 1 to 7.")
            continue

        # ---- Collect inputs based on choice ----
        voltage = current = resistance = power = None

        if choice == "1":  # Find Voltage
            current = get_float("Enter current (A): ")
            resistance = get_float("Enter resistance (Ω): ")
            voltage = calculate_voltage(current, resistance)
            power = calculate_power(voltage=voltage, current=current)

        elif choice == "2":  # Find Current
            voltage = get_float("Enter voltage (V): ")
            resistance = get_float("Enter resistance (Ω): ")
            current = calculate_current(voltage, resistance)
            if current is None:
                print("Error: Resistance cannot be zero.")
                continue
            power = calculate_power(voltage=voltage, current=current)

        elif choice == "3":  # Find Resistance
            voltage = get_float("Enter voltage (V): ")
            current = get_float("Enter current (A): ")
            resistance = calculate_resistance(voltage, current)
            if resistance is None:
                print("Error: Current cannot be zero.")
                continue
            power = calculate_power(voltage=voltage, current=current)

        elif choice == "4":  # Find Power
            print("You can enter any two known values.")
            print("Leave the unknown one blank (just press Enter).")
            v_str = input("Voltage (V) [Enter to skip]: ").strip()
            i_str = input("Current (A) [Enter to skip]: ").strip()
            r_str = input("Resistance (Ω) [Enter to skip]: ").strip()

            try:
                voltage = float(v_str) if v_str else None
                current = float(i_str) if i_str else None
                resistance = float(r_str) if r_str else None
            except ValueError:
                print("Invalid number entered.")
                continue

            power = calculate_power(voltage, current, resistance)
            if power is None:
                print("Not enough valid data to calculate power.")
                continue

            # Try to fill missing values for the full report
            if voltage is None and current is not None and resistance is not None:
                voltage = calculate_voltage(current, resistance)
            if current is None and voltage is not None and resistance is not None:
                current = calculate_current(voltage, resistance)
            if resistance is None and voltage is not None and current is not None:
                resistance = calculate_resistance(voltage, current)

        # ---- Display results ----
        print("\n----- Results -----")
        if voltage is not None:
            print(f"Voltage     : {voltage:.4f} V")
        if current is not None:
            print(f"Current     : {current:.4f} A")
        if resistance is not None:
            print(f"Resistance  : {resistance:.4f} Ω")
        if power is not None:
            print(f"Power       : {power:.4f} W")
        print("-------------------")

        # Save a short summary to history
        summary = (f"V={voltage:.2f}V, I={current:.2f}A, "
                   f"R={resistance:.2f}Ω, P={power:.2f}W" 
                   if all(x is not None for x in [voltage, current, resistance, power])
                   else f"Power = {power:.2f} W")
        history.append(summary)

if __name__ == "__main__":
    main()
