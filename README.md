What Is This?
-------------

Калькулятор расчет цены товара с учетом прогрессивной скидки и налога для региона
https://toms-calculator.herokuapp.com/

How It Works?
-------------

https://www.loom.com/share/483b2b08e27048d6945bb80433692abb


Testing
-------
```
python test_calculator.py
```

Development
-------
Запуск сервера:
```
   docker build -t calculator .
   docker run -p 5000:5000 calculator
```
Линтеры:
```
   isort *.py
   flake *.py
```
