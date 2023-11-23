const { chromium } = require("playwright");
const express = require("express");
const axios = require("axios");
const app = express();

let eur_usd_v,gbp_usd_v = 0;
(async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext();
  const page = await context.newPage();
  const page1 = await context.newPage();
  // await page.goto("https://www.dailyfx.com/eur-usd");
  // eurusd_locator = page.eurusd_locator('//*[@id="dfx-topRatesPanel"]/div[1]/div[1]/a/div[2]/div');
  await page.goto("https://in.tradingview.com/symbols/EURUSD/");
  await page1.goto("https://in.tradingview.com/symbols/GBPUSD/");
  const eurusd_locator = page.locator('.last-JWoJqCpY.js-symbol-last');
  const gbpusd_locator = page1.locator('.last-JWoJqCpY.js-symbol-last');
  const page2 = await context.newPage();
  await page2.goto("https://olymptrade.com/login");
  const page3 = await context.newPage();
  await page3.goto("https://olymptrade.com/");
  const buy = (pag) => {
    pag.click(".deal-button_up");
  };
  const sell = (pag) => {
    pag.click(".deal-button_down");
  };
  loop = async () => {
    while (true) {
      eur_usd_v =await eurusd_locator.innerText()
      gbp_usd_v = await gbpusd_locator.innerText()
      await new Promise((resolve) => setTimeout(resolve, 600));
    }
  };
  loop();
  app.get("/request/:iq", async (req, res) => {
    const iq = req.params.iq;
    if (iq == "eurusd") {
      res.send(eur_usd_v.toString());
    }
    else if (iq=="gbpusd"){
      res.send(gbp_usd_v.toString());
    }
  });

  app.get("/eurusd/:id", (req, res) => {
    const id = req.params.id;
    if (id == "buy") {
      buy(page2);
    } else if (id == "sell") {
      sell(page2);
    }
    res.sendStatus(200);
  });
  app.get("/gbpusd/:id", (req, res) => {
    const id = req.params.id;
    if (id == "buy") {
      buy(page3);
    } else if (id == "sell") {
      sell(page3);
    }
    res.sendStatus(200);
  });
  app.listen(3000, (data) => console.log("Server running on port 3000", data));
})();
