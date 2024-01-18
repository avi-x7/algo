const { chromium } = require("playwright");
const express = require("express");
const axios = require("axios");
const app = express();

 const symbols= ['AUDCAD','GBPJPY','USDJPY','EURAUD','EURCAD','EURGBP']
 var percent= {}
 var cr_env=[]
 var pr_env=[]
 var cel=2
let eur_usd_v,gbp_usd_v = 0;
( async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext();
  const page = await context.newPage();   //tradingview-eurusd
  const page1 = await context.newPage();  //tradingview-gbpusd
  const page2 = await context.newPage();  //olymp-eurusd
  const page3 = await context.newPage();  //olymp-gbpusd
  const page6 = await context.newPage();  //olymp trade v1
  const page7 = await context.newPage();  // olymp trade v2
  const page4 = await context.newPage();   //tradingview-v1
  const page5 = await context.newPage();  //tradingview-v2
  await page.goto("https://in.tradingview.com/symbols/EURUSD/");
  await page1.goto("https://in.tradingview.com/symbols/GBPUSD/");
  await page2.goto("https://olymptrade.com/login");
  await page3.goto("https://olymptrade.com/");
  await page6.goto("https://olymptrade.com/"); 
  await page7.goto("https://olymptrade.com/"); 
  await page4.goto(`https://in.tradingview.com/symbols/GBPJPY`);
  await page5.goto(`https://in.tradingview.com/symbols/GBPJPY`);
  const eurusd_locator = page.locator('.last-JWoJqCpY.js-symbol-last');
  const gbpusd_locator = page1.locator('.last-JWoJqCpY.js-symbol-last');
  const v1_locator=page4.locator('.last-JWoJqCpY.js-symbol-last');
  const v2_locator=page5.locator('.last-JWoJqCpY.js-symbol-last');
  // const random_locator = page4.locator('.last-JWoJqCpY.js-symbol-last');

// Functions
  const buy = (pag) => {
    pag.click(".deal-button_up");
  };
  const sell = (pag) => {
    pag.click(".deal-button_down");
  };

  //function to update the percent
  const get_percent=(_symb)=>{
    const plocator=page3.locator(`._3oqFbWYK_Q4O[data-ticker=${_symb}] ._44tV67dU25 .ltr`);
    let pvalue=plocator.innerText();
    let main_value=pvalue.slice(0,-1);
    return main_value;
  }
  const update_percent=()=>{ 
    for (let a=0 ;a<=5;a++){
      percent[symbols[a]]=get_percent(symbols[a])
    }

  }

  // creating / updating envs

  //creating / updating pages
const upcreate=()=>{

}
//removing which is less than 77
  const rm=()=>{
    let r=0
    while (r<cel){
      if ((percent[cr_env[r]]) < 77){
        cr_env.splice(r,1)
        r+=1
      }
      else{
        r+=1
      }
    }
    
  }
  const checkup_env=()=>{
    let b=cr_env.length;let c=0;
    while ((b < cel) && (c < symbols.length)){
      if ((percent[symbols[c]]) > 76){
        cr_env.push(symbols[c]);
        b+=1;
        c+=1;
      }
      else{
        c+=1;
      }
    } 
  }



  // checking current envs
  const env_manage=()=>{
    pr_env=cr_env
    if (cr_env.length==cel){
      if ((percent[cr_env[0]]) > 76 < (percent[cr_env[1]])){
        return true
      }
      else{
        rm()
        checkup_env()
      }
    }
    else {
      rm()
      checkup_env()
    }
  }





// eurusd-gbpusd loop
  loop = async () => {
    while (true) {
      eur_usd_v =await eurusd_locator.innerText()
      gbp_usd_v = await gbpusd_locator.innerText()
      // random_v =await random_locator.innerText()
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
    // else if (iq=="random"){
    //   res.send(random_v.toString());
    // }
  });


  //buy-sell api calls
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


  // app.get("/random/:id", (req, res) => {
  //   const id = req.params.id;
  //   if (id == "buy") {
  //     buy(page5);
  //   } else if (id == "sell") {
  //     sell(page5);
  //   }
  //   res.sendStatus(200);
  // });
  app.listen(3000, (data) => console.log("Server running on port 3000", data));
})();
