import pandas as pd
import numpy as np

#6
df = pd.read_csv("tested.csv")
print("#6")
print("Данные загружены")

#7
n = int(input("Enter number of rows: "))
print("#7")
print(df.head(n))

#8
print("#8")
print(df.tail(5))

#9
print("#9")
dfb=df.shape
print(df.shape[0], df.shape[1])

#10
print("#10")
print(list(df.columns))

#11
print("#11")
print(df.dtypes)

#12
numeric = ["Age", "SibSp", "Parch", "Fare"]
categorical = ["Survived", "Pclass", "Sex", "Embarked"]
print("#12")
print("Числовые: ", numeric)
print("Категориальные: ", categorical)

#13
print("#13")
print(df[numeric].agg(["mean", "median", "min", "max", "std"]))

#14
print("#14")
print(df["Pclass"].value_counts())

#15
print("#15")
print(len(df["Embarked"].unique()))

#Вопрос
print("#Вопрос")
print("Pclass - это неизмеряемая величина: арифметика над ней бессмысленна. Числа здесь - метки групп. Поэтому признак категориальный, а не числовой")

#16
m = df.isna().sum()
print("#16")
print(m)

#17
p = m.sum() / len(df) * 100
print("#17")
print(p)

#18
print("#18")
print(m.idxmax(), m.max())

#19
print("#19")
print(df["Age"].agg(["mean", "median", "min", "max", "std", "count"]))
before = df["Age"].agg(["mean", "median", "min", "max", "std", "count"])

#20
m_age = df["Age"].median()
df["Age"] = df["Age"].fillna(m_age)
print("#20")
print("Заполнено")

#21
print("#21")
print(df["Age"].agg(["mean", "median", "min", "max", "std", "count"]))

#22
print("#22")
after = df["Age"].agg(["mean", "median", "min", "max", "std", "count"])

table = pd.DataFrame({
    "До обработки": before,
    "После обработки": after
})

table.index = [
    "Среднее арифметическое",
    "Медиана",
    "Минимальный возраст",
    "Максимальный возраст",
    "Стандартное отклонение",
    "Количество известных значений"
]

print(table)

#23
print("#23")
df = df.dropna(subset=["Embarked"])
print("Строки с отсутствующим Embarked удалены")

#24
print("#24")
p = df["Cabin"].isna().mean()
print("Доля пропусков в Cabin", p)
if p > 0.5:
    df = df.drop(columns=["Cabin"])
    print("Столбец Cabin удален")
else:
    print("Столбец Cabin сохранен")

#25
print("#25")
print(df.isna().sum())

#26
print("#26")
dfa=df.shape
print("Размерность ДО (строк-столбцов):", dfb)
print("Размерность ПОСЛЕ (строк-столбцов):", dfa)

#27
print("#27")
print("Медиана более устойчива к выбросам, нежели чем среднее")

#28
print("#28")
print("Изменились: количество известных значений, среднее арифметическое и стандартное отклонение. Остались неизменными: медиана, минимальное и максимальное значения.")

#29
print("#29")
print("Заполняя пропуски одним и тем же значением, мы искусственно уменьшаем общий разброс, из-за чего стандартное отклонение может уменьшиться")

#30
print("#30")
print("Нет, исходное распределение не сохраняется. В точке медианы образуется неестественный пик, что искажает форму распределения")

#31
print("#31")
survived_arr = df["Survived"].to_numpy()
sex_arr = df["Sex"].to_numpy()
age_arr = df["Age"].to_numpy()
fare_arr = df["Fare"].to_numpy()
total_survived = np.mean(survived_arr) * 100
print("Общий процент выживших", total_survived)

#32
print("#32")
male_mask = (sex_arr == "male")
female_mask = (sex_arr == "female")
male_survived = np.mean(survived_arr[male_mask]) * 100
female_survived = np.mean(survived_arr[female_mask]) * 100
print("Процент выживших мужчин", male_survived)
print("Процент выживших женщин", female_survived)

#33
print("#33")
male_mean_age = np.mean(age_arr[male_mask])
female_mean_age = np.mean(age_arr[female_mask])
print("Средний возраст мужчин", male_mean_age)
print("Средний возраст женщин", female_mean_age)

#34
print("#34")
survived_mask = (survived_arr == 1)
dead_mask = (survived_arr == 0)

male_survived_ages = age_arr[male_mask & survived_mask]
mean_male_survived = np.mean(male_survived_ages) if len(male_survived_ages) > 0 else 0

male_dead_ages = age_arr[male_mask & dead_mask]
mean_male_dead = np.mean(male_dead_ages) if len(male_dead_ages) > 0 else 0

female_survived_ages = age_arr[female_mask & survived_mask]
mean_female_survived = np.mean(female_survived_ages) if len(female_survived_ages) > 0 else 0

female_dead_ages = age_arr[female_mask & dead_mask]
mean_female_dead = np.mean(female_dead_ages) if len(female_dead_ages) > 0 else 0

print("Средний возраст выживших мужчин", mean_male_survived)
print("Средний возраст погибших мужчин", mean_male_dead)
print("Средний возраст выживших женщин", mean_female_survived)
print("Средний возраст погибших женщин", mean_female_dead)


#35
print("#35")
print("Минимальная стоимость", np.nanmin(fare_arr))
print("Максимальная стоимость", np.nanmax(fare_arr))
print("Средняя стоимость", np.nanmean(fare_arr))

#36
print("#36")
print("Стандартное отклонение возраста", np.std(age_arr))

#Контрольный вопрос IV
print("#Контрольный вопрос IV")
print("Женщины имели крайне более высокий процент выживаемости по сравнению с мужчинами. Cредний возраст мужчин на корабле был немного ниже, чем у женщин")

#Задание 1
print("#Задание 1")
t1 = df[(df["Sex"] == "male") & (df["Age"] > 30) & (df["Pclass"] == 1)]
print("Количество пассажиров", len(t1))
print(t1.head(10))

#Задание 2
print("#Задание 2")
t2 = df[((df["Age"] < 18) | (df["Sex"] == "female")) & (df["Survived"] == 1)]
print("Количество", len(t2))

#Задание 3
print("#Задание 3")
mean_fare = df[df["Pclass"] == 3]["Fare"].mean()
t3 = df[(df["Pclass"] == 3) & (df["Fare"] > mean_fare)]
print(t3)

#Задание 4
print("#Задание 4")
t4 = df[(df["Age"] >= 20) & (df["Age"] <= 40) & (df["Embarked"] == "S")]
print(t4)

#Контрольный вопрос V
print("#Контрольный вопрос V")
print("Логическое И требует одновременного выполнения всех условий для строки, а ИЛИ отбирает строку, если выполняется хотя бы одно из условий")

#37
print("#37")
group_class_sex = df.groupby(["Pclass", "Sex"]).agg(
    Количество=("PassengerId", "count"),
    Средний_возраст=("Age", "mean"),
    Доля_выживших_процент=("Survived", lambda x: x.mean() * 100),
    Средняя_цена_билета=("Fare", "mean")
)
print(group_class_sex)

#38
print("#38")
group_embarked = df.groupby("Embarked").agg(
    Количество=("PassengerId", "count"),
    Процент_выживших=("Survived", lambda x: x.mean() * 100)
)
print(group_embarked)

#39
print("#39")
best_pclass = df.groupby("Pclass")["Survived"].mean().idxmax()
print("Класс с наибольшей долей выживших", best_pclass)

#Контрольный вопрос VI
print("#Контрольный вопрос VI")
print("Фильтрация отсекает ненужные строки по условию, уменьшая размер таблицы. Группировка же объединяет строки в группы для вычисления по ним собирательных статистик")

#40
df.to_csv("titanic_processed.csv", index=False)
print("#40")
print("Обработанный DataFrame сохранен в titanic_processed.csv")

#41
group_class_sex.to_csv("titanic_statistics.csv")
print("#41")
print("Результаты группировки успешно сохранены в titanic_statistics.csv")

#42
df_check = pd.read_csv("titanic_processed.csv")
print("#42")
print("Файл повторно загружен. Размерность таблицы", df_check.shape)

#43
print("#43")
print("Наибольшее количество пропусков содержал признак Cabin, также пропуски присутствовали в признаках Age и Fare")

#44
print("#44")
print("Удаление столбца Cabin уменьшило количество столбцов признаков, а заполнение признака Age медианой привело к искусственному стягиванию среднего арифметического к медиане и заметному снижению стандартного отклонения из-за уменьшения общего разброс данных")

#45
print("#45")
print("Выживаемость женщин оказалась абсолютной (100%), в то время как среди мужчин выживших не оказалось совсем, что является особенностью данного датасета")

#46
print("#46")
print("Наибольшая доля выживших зафиксирована у пассажиров первого класса")

#47
print("#47")
print("Наиболее полезными оказались фильтрация данных по условиям, группировка через groupby и расчеты в массивах NumPy")

