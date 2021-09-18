What Is This?
-------------

Калькулятор расчет цены товара с учетом прогрессивной скидки и налога для региона

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
