# main.py
from data_input import get_input_data
from calculator import calculate_equipment

def main():
    # Ввод данных
    data = get_input_data()
    
    # Расчёт
    results = calculate_equipment(data)
    
    # Вывод результатов
    print("\n=== Результаты расчётов ===")
    print(f"Производительность линии пельменей (P_тлп): {results['P_tlp']:.2f} т/ч")
    print(f"Количество пельменных автоматов (n_па): {results['n_pa']} шт.")
    print(f"Производительность линии теста (P_тлт): {results['P_tlt']:.2f} т/ч")
    print(f"Количество тестомесильных машин (n_тм): {results['n_tm']} шт.")
    print(f"Производительность линии фарша (P_тлф): {results['P_tlf']:.2f} т/ч")
    print(f"Количество куттеров (n_к): {results['n_k']} шт.")

if __name__ == "__main__":
    main()