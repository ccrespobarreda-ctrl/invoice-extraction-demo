# 100% synthetic invoices. Companies, people, IDs and addresses are invented.
INVOICES = [
  dict(id="INV-2026-0412", issue="2026-09-03", due="2026-10-03", currency="EUR", po="PO-77810",
       vendor=dict(name="Northwind Office Supplies S.L.", vat="ESB00000001", addr=["Calle Ficticia 12", "28001 Madrid, Spain"], email="billing@northwind-demo.example"),
       buyer=dict(name="Brightline Studio Ltd.", vat="GB000000001", addr=["14 Sample Street", "London EC1A 1AA, UK"]),
       lines=[("Ergonomic office chair", 6, 189.00), ("Standing desk 140x70", 3, 349.00), ("Monitor arm, dual", 6, 64.50), ("Delivery and assembly", 1, 120.00)],
       vat_rate=0.21, stated_total=None, color="#1f4e79"),
  dict(id="LC-10937", issue="2026-09-15", due="2026-10-15", currency="EUR", po="PO-77902",
       vendor=dict(name="Lumen Cloud Services GmbH", vat="DE000000002", addr=["Beispielweg 5", "10115 Berlin, Germany"], email="invoices@lumen-demo.example"),
       buyer=dict(name="Brightline Studio Ltd.", vat="GB000000001", addr=["14 Sample Street", "London EC1A 1AA, UK"]),
       lines=[("Managed Kubernetes cluster (Sep)", 1, 840.00), ("Object storage 2.4 TB", 1, 96.00), ("Premium support plan", 1, 250.00)],
       vat_rate=0.19, stated_total=None, color="#5b3f8c"),
  dict(id="ATL-5521", issue="2026-09-28", due="2026-09-20", currency="EUR", po=None,
       vendor=dict(name="Atlas Freight B.V.", vat="NL000000003B01", addr=["Voorbeeldstraat 88", "1011 AB Amsterdam, NL"], email="ar@atlas-demo.example"),
       buyer=dict(name="Brightline Studio Ltd.", vat="GB000000001", addr=["14 Sample Street", "London EC1A 1AA, UK"]),
       lines=[("Pallet transport Madrid-London", 4, 410.00), ("Customs clearance", 1, 260.00), ("Fuel surcharge", 1, 550.00)],
       vat_rate=0.21, stated_total=2994.50, color="#8a5a00"),
]
