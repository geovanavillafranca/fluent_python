invoice = """
1909   Pimoroni Pibrella        $18.90
1920   6mm Tactitle Switch      $7.00
2022   Panavise Jr.             $28.78
1909   Pimoroni Pibrella        $18.90
1920   6mm Tactitle Switch      $7.00
2022   Panavise Jr.             $28.78
"""
DESCRIPTION = slice(6, 38)
UNITE_PRICE = slice(38,40)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNITE_PRICE], item[DESCRIPTION])

'''
  6mm Tactitle Switch      $7.00
  Panavise Jr.             $28.78
  Pimoroni Pibrella        $18.90
  6mm Tactitle Switch      $7.00 
  Panavise Jr.             $28.78
'''