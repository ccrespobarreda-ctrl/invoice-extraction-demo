import json, sys
from data import INVOICES
def money(x): return f"{x:,.2f}"
out=[]
for inv in INVOICES:
    sub=round(sum(q*p for _,q,p in inv["lines"]),2); vat=round(sub*inv["vat_rate"],2)
    total=inv["stated_total"] or round(sub+vat,2)
    rows="".join(f"<tr><td>{d}</td><td class=r>{q}</td><td class=r>{money(p)}</td><td class=r>{money(q*p)}</td></tr>" for d,q,p in inv["lines"])
    v,b=inv["vendor"],inv["buyer"]
    html=f"""<!doctype html><html><head><meta charset=utf-8><style>
body{{margin:0;background:#e9ecef;font-family:"Liberation Sans",sans-serif;color:#1d2125}}
.page{{width:794px;min-height:1050px;margin:0 auto;background:#fff;padding:56px 60px;box-sizing:border-box;position:relative}}
.top{{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:4px solid {inv['color']};padding-bottom:22px}}
.logo{{font-size:24px;font-weight:700;color:{inv['color']}}} .small{{font-size:12.5px;line-height:1.55;color:#4a5158}}
h1{{margin:0;font-size:30px;letter-spacing:2px;color:{inv['color']};text-align:right}}
.meta td{{font-size:13px;padding:2px 0 2px 16px}} .meta td:first-child{{color:#6c757d}}
.parties{{display:flex;gap:40px;margin:30px 0}} .parties div{{flex:1}} .lab{{font-size:11px;text-transform:uppercase;letter-spacing:1px;color:#6c757d;margin-bottom:6px}}
table.items{{width:100%;border-collapse:collapse;font-size:13.5px}} .items th{{background:{inv['color']};color:#fff;text-align:left;padding:10px;font-weight:600}}
.items td{{padding:10px;border-bottom:1px solid #e3e6e8}} .r{{text-align:right}} .items th.r{{text-align:right}}
.totals{{margin-left:auto;width:300px;margin-top:20px;font-size:14px}} .totals td{{padding:6px 10px}} .grand td{{font-weight:700;font-size:17px;border-top:2px solid {inv['color']}}}
.foot{{position:absolute;bottom:40px;left:60px;right:60px;font-size:11px;color:#8a9096;border-top:1px solid #e3e6e8;padding-top:10px}}
</style></head><body><div class=page>
<div class=top><div><div class=logo>{v['name']}</div><div class=small>{'<br>'.join(v['addr'])}<br>VAT ID: {v['vat']}<br>{v['email']}</div></div>
<div><h1>INVOICE</h1><table class=meta>
<tr><td>Invoice no.</td><td id=f-id><b>{inv['id']}</b></td></tr>
<tr><td>Issue date</td><td id=f-issue>{inv['issue']}</td></tr>
<tr><td>Due date</td><td id=f-due>{inv['due']}</td></tr>
<tr><td>PO number</td><td id=f-po>{inv['po'] or '&nbsp;'}</td></tr></table></div></div>
<div class=parties><div><div class=lab>Bill to</div><b>{b['name']}</b><div class=small>{'<br>'.join(b['addr'])}<br>VAT ID: {b['vat']}</div></div>
<div><div class=lab>Payment</div><div class=small>Bank transfer · IBAN XX00 0000 0000 0000 0000<br>Terms: 30 days net</div></div></div>
<table class=items><tr><th>Description</th><th class=r>Qty</th><th class=r>Unit price</th><th class=r>Amount</th></tr>{rows}</table>
<table class=totals><tr><td>Subtotal</td><td class=r id=f-sub>{money(sub)}</td></tr>
<tr><td>VAT {int(inv['vat_rate']*100)}%</td><td class=r id=f-vat>{money(vat)}</td></tr>
<tr class=grand><td>Total ({inv['currency']})</td><td class=r id=f-total>{money(total)}</td></tr></table>
<div class=foot>SYNTHETIC SAMPLE INVOICE created for a portfolio demo. All companies, IDs and amounts are fictitious.</div>
</div></body></html>"""
    open(f"{inv['id']}.html","w").write(html)
