import express from "express";
import fetch from "node-fetch";

var app = express();
const host = "api.frankfurter.app";

app.get("/convert", (req, res, next) => {
  var test = [
    { amount: 15000.0, currency: "IDR" },
    { amount: 3.1, currency: "EUR" },
  ];
  var datas = [];
  test.forEach((element, index) => {
    return fetch(
      `https://${host}/latest?amount=${element.amount}&from=${element.currency}&to=USD`
    )
      .then((response) => response.json())
      .then(async (data) => {
        console.log(data);
        console.log(index);
        console.log(test.length);
        datas.push(data.rates.USD);
        if (index == test.length - 1) {
          res.send(datas);
        }
      })
      .catch((err) => console.log(err));
  });
});
app.listen(3000, () => {
  console.log("Server running on port 3000");
});
