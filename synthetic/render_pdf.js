const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:900,height:1100},deviceScaleFactor:2});
for(const id of ['INV-2026-0412','LC-10937','ATL-5521']){await p.goto('file://'+process.cwd()+'/'+id+'.html');
await p.pdf({path:id+'.pdf',width:'794px',height:'1050px',printBackground:true,pageRanges:'1'});
await p.locator('.page').screenshot({path:id+'.png'});}
await b.close();})();
