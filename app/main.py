from consumer import KafkaMessageConsumer
from database import DatabaseHandler
from msg_handler import MessageHandler

import config

tmp1 = {'metadata': {'type': 'offer'}, 'payload': {'id': '631aa5a8-9b5d-4ae2-945a-00a0a539b101', 'name': 'LEGO Harry Potter - Roxfort (71043)', 'description': 'Üdvözlünk az egyedülálló LEGO® Harry Potter™ 71043 Roxfort kastélyban! Építsd meg és állítsd ki ezt a részletesen kidolgozott mini LEGO® Harry Potter TM Roxfort kastély modellt, mely több mint 6000 elemből áll! Fedezd fel a rendkívül részletesen kidolgozott kamrákat, tornyokat és tantermeket, valamint számos rejtett funkciót és a Harry Potter filmek jeleneteit is! Népesítsd be a kastélyt 27 mikrofigurával, melyek között Harry, Hermione és Ron figurája is szerepel, továbbá rengeteg jellegzetes kiegészítő és tárgy lenyűgöző választéka is vár rád! A varázslatos építési élményt pedig kiegészítheted Hagrid kunyhójával és a Fúriafűzzel.\n\n\n\nÍgy is ismerheti: Harry Potter Roxfort 71043, HarryPotterRoxfort71043, Harry Potter Roxfort (71043), HarryPotter-Roxfort71043, Harry Potter - Roxfort ( 71043)', 'category': 'LEGO', 'parameters': {'minimum age': 17, 'set': 'Harry Potter', 'number of pieces': 6020}}}
tmp2 = {'metadata': {'type': 'offer'}, 'payload': {'id': '38495bd1-afe9-4cd0-bf9d-eca162e75542', 'name': 'LEGO Harry Potter - Roxfort (71043)', 'description': 'Üdvözlünk az egyedülálló LEGO® Harry Potter™ 71043 Roxfort kastélyban! Építsd meg és állítsd ki ezt a részletesen kidolgozott mini LEGO® Harry Potter TM Roxfort kastély modellt, mely több mint 6000 elemből áll! Fedezd fel a rendkívül részletesen kidolgozott kamrákat, tornyokat és tantermeket, valamint számos rejtett funkciót és a Harry Potter filmek jeleneteit is! Népesítsd be a kastélyt 27 mikrofigurával, melyek között Harry, Hermione és Ron figurája is szerepel, továbbá rengeteg jellegzetes kiegészítő és tárgy lenyűgöző választéka is vár rád! A varázslatos építési élményt pedig kiegészítheted Hagrid kunyhójával és a Fúriafűzzel.\n\n\n\nÍgy is ismerheti: Harry Potter Roxfort 71043, HarryPotterRoxfort71043, Harry Potter Roxfort (71043), HarryPotter-Roxfort71043, Harry Potter - Roxfort ( 71043)', 'category': 'LEGO', 'parameters': {'minimum age': 17, 'set': 'Harry Poter', 'number of pieces': 6020}}}
tmp3 = {'metadata': {'type': 'category'}, 'payload': {'name': 'LEGO'}}

def main():
        
        consumer = KafkaMessageConsumer()
        db = DatabaseHandler()
        parser = MessageHandler(db)
        db.create_tables()
        
        parser.handle_message(tmp3)
        parser.handle_message(tmp1)
        parser.handle_message(tmp2)

        for message in consumer.receive_messages(config.KAFKA_TOPIC):
                parser.handle_message(message)

                products = db.get_products()
                print(products)
                print(len(products))


if __name__ == '__main__':
        main()
