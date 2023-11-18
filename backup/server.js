const { chromium } = require("playwright");
const express = require("express");
const axios = require("axios");
const app = express();

let g = 0;
(async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext();
  const page = await context.newPage();
  // await page.goto("https://www.dailyfx.com/eur-usd");
  // locator = page.locator('//*[@id="dfx-topRatesPanel"]/div[1]/div[1]/a/div[2]/div');
  await page.goto("https://www.dailyfx.com/forex-rates#currencies");
  locator = page.locator('//*[@id="currencies"]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[1]');
  const page2 = await context.newPage();
  await page2.goto("https://olymptrade.com/login");

  const buy =()=>{page2.click('.deal-button_up')}
  const sell =()=>{page2.click('.deal-button_down')}
  loop = async () => {
    while (true) {
      g = await locator.getAttribute("data-value");
      await new Promise((resolve) => setTimeout(resolve, 600));
    }
  };
  loop();
  app.get("/request", async (req, res) => {
    res.send(g.toString());
  });

  app.get("/response/:id", (req, res) => {
    const id = req.params.id;
    if (id == "buy") {
      buy();
    } else if (id == "sell") {
      sell();
    }
    res.sendStatus(200);
  });
  app.listen(3000, (data) => console.log("Server running on port 3000", data));
})();
