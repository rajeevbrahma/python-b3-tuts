# walmart
# entry time
# exit time
# purchased_items_tuple
# purchased or not
# duratino
# preferred payment method
# lane activity - [sports,cosmetics,kids,utilities,.......]
daily_customer_activity_report_log = [
    {
        "entry_time":"9:00",                    #|
        "exit_time":None,                       #|
        "purchased_items":None,                 #|
        "duration":0.0,                         #|   - 0
        "preferred_payment_method":None,        #|
        "lane_activity":None,                   #|        
        "lanes":None,                           #|        
        "is_purchased":False                    #|
    }

]

print (daily_customer_activity_report_log)
lane_activity = [
    'sports',
    'cosmetics',
    'sports',
    'uitilities',
    'sports',
    'furniture',
    'cosmetics',
    'sports',
    'furniture'
]
lanes = set(lane_activity)

daily_customer_activity_report_log[0]["lane_activity"] = lane_activity
daily_customer_activity_report_log[0]["lanes"] = lanes

daily_customer_activity_report_log[0]["preferred_payment_method"] = ('Cash','Credit')
daily_customer_activity_report_log[0]["purchased_items"] = {
    "chair":2,   # key - item, value - quantity of the item
    "Sofa":1,
    "Table":2,
    "kitchen_utitilites_groceries":[
        {'bread':1,'milk':2}, # - 0
        ['spoons','fork'],     # - 1 
#            0       1
    ],
}
daily_customer_activity_report_log[0]["is_purchased"] = True
daily_customer_activity_report_log[0]["exit_time"] = "10:00"
daily_customer_activity_report_log[0]["duration"] = 60


print (daily_customer_activity_report_log[0]["purchased_items"]["kitchen_utitilites_groceries"][1][1])

# print (daily_customer_activity_report_log)

