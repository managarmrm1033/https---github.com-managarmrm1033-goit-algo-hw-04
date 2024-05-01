from pathlib import Path

def total_salary(path):
    total_salary = 0
    num_developers = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1
                
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Сталася помилка при обробці файлу:", e)
    
    if num_developers > 0:
        average_salary = total_salary / num_developers
    else:
        average_salary = 0
    
    return total_salary, average_salary

total, average = total_salary("D:\домашня робота номер 4\salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
