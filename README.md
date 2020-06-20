## sudoku

Моя примитивная реализация алгоритма игры. Здесь выполняется весь цикл: 
1. Заполнение игрового поля цифрами (9х9 ячеек): `fill_game_field()`
2. "Перемешивание" строк и столбцов поля: `mix_game_field()`
3. Скрытие N-го количества ячеек (в зависимости от сложности): `hide_cells_in_game_field('hard')`
4. Решение игры, то есть нахождение правильных значений для скрытых ячеек: `solve_game_field()`

Изначально был интерес сделать именно алгоритм решателя игры, но попутно получилось и остальное).  
В общем работает, но есть ещё что доделывать, доводить до ума, совершенствовать... Когда-нибудь возможно я этим займусь)

Во время разработки был использован материал этой статьи с Хабра: [Алгоритм генерации судоку](https://habr.com/ru/post/192102/)  
А вообще есть интерес сделать что-то вроде этого: [Решение судоку с помощью веб-камеры в реальном времени](https://habr.com/ru/post/126373/)