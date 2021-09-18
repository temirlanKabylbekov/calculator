from flask import Flask, render_template, request

from calculator import REGION_TO_TAX_MAP, InvalidCalculatorParamsError, calculate

app = Flask(__name__, template_folder=".")


ERROR_MESSAGE = "Проверьте входные данные ⚠️"
SUCCESS_MESSAGE = "{} 👈 Цена со скидкой и налогом для товара стоимостью {} в количестве {} для региона {}"


@app.route("/", methods=["post", "get"])
def index():
    message = None

    if request.method == "POST":
        region = request.form.get("region")
        product_price = request.form.get("product_price")
        products_count = request.form.get("products_count")

        try:
            price = calculate(float(product_price) * int(products_count), region)
            message = SUCCESS_MESSAGE.format(price, product_price, products_count, region)
        except (InvalidCalculatorParamsError, ValueError):
            message = ERROR_MESSAGE

    return render_template("index.html", message=message, regions=REGION_TO_TAX_MAP.keys())
