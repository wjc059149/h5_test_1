from framework.base_page import BasePage
import requests


sn = 'T203193B40683'
orderSn = BasePage.random_32(1)
amount = 0.01
shopOrderSn = BasePage.random_32(3)
Url = "http://api.sunmi.com/api/invoice/app/invoice/1.0/?service=/syncInvoiceOrder&14c4b06b824ec593239362517f538b29=8afe757107b215bb4799880a14b8d4a1&76a2173be6393254e72ffa4d6df1030a=6bf4947b8998e1f9030a719ac3305509"
r = BasePage.syncInvoiceOrder(amount,sn,shopOrderSn,orderSn,Url)
print(r)
url = "http://invoice.sunmi.com/?orderSn="+orderSn
print(url)