import pandas as pd


def get_client_numbers():
    # Замените 'your_file.xlsx' на путь к вашему Excel-файлу
    file_path = 'Clients_2024.10.29.xlsx'

    # Считываем данные из Excel файла
    df = pd.read_excel(file_path)

    # Извлекаем данные из столбца B
    # Столбцы в pandas нумеруются с 0, поэтому B - это столбец с индексом 1
    column_b_data = df.iloc[:, 1].tolist()

    # Выводим результат
    print("Успешно записали всю базу клиентов")

    return column_b_data

