from database import Database

db = Database()


def test():
    # db.create_table_users()
    # users = db.select_all_users()
    # print(f"qo'shilmasdan oldin: {users=}")
    # db.add_user(1, "qwerty", "buxoro", "online", "back_end", "998913349948")
    # db.add_user(12, "werty", "buxoro", "online", "back_end", "998913349948")
    # db.add_user(13, "qerty", "buxoro", "online", "back_end", "998913349948")
    #db.add_user(14, "qwrty", "buxoro", "online", "back_end", "998913349948")
    # db.add_user(16, "qwety", "buxoro", "online", "back_end", "998913349948")
    # db.add_user(21, "qwery", "buxoro", "online", "back_end", "998913349948")
    # db.add_user(11, "qwert", "buxoro", "online", "back_end", "998913349948")
    # print(f"qo'shgandandan keyin: {users=}")
    user = db.select_user(allname="qwrty", id=14)
    print(f"Anavi odam: {user}")


def test1():
    q=123
    print("qwerty")
    # db.create_table_users()
    db.add_user(id=q, allname="qwert", areaname="buxoro", coursetype="online", coursegroup="back_end", phonenumber="998913349948")
    print(db.select_all_users())

# def update():
#     db.update_coursegroup()



test()
# test1()
