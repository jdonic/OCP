#feaa400a-d304-4f55-b045-51b1daec8e0c


from database import DatabaseHandler

db = DatabaseHandler()
offer = db.get_offer_by_id("feaa400a-d304-4f55-b045-51b1daec8e0c")
print(offer)