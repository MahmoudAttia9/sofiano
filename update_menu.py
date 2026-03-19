import re

html_path = "index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_menu_str = """                'special-coffee': [
                    { name_en: 'Turkish Coffee', name_ar: 'قهوة تركي', price_s: 30, price_d: 35 },
                    { name_en: 'Turkish Mahwaj', name_ar: 'قهوة محوج', price_s: 35, price_d: 40 },
                    { name_en: 'Turkish Dark Roast', name_ar: 'قهوة غامق', price_s: 35, price_d: 40 },
                    { name_en: 'Sofiano Coffee', name_ar: 'قهوة سفيانو', price_s: 35, price_d: 40 },
                    { name_en: 'Special Coffee', name_ar: 'قهوة سبشيال', price_s: 35, price_d: 40 },
                    { name_en: 'Habashi Coffee', name_ar: 'قهوة حبشي', price_s: 35, price_d: 40 },
                    { name_en: 'Brazilian Coffee', name_ar: 'قهوة برازيلي', price_s: 35, price_d: 40 },
                    { name_en: 'Indian Coffee', name_ar: 'قهوة هندي', price_s: 35, price_d: 40 },
                    { name_en: 'Ameed Coffee', name_ar: 'قهوة عميد', price_s: 40, price_d: 45 },
                    { name_en: 'Brazilian Dark Coffee', name_ar: 'قهوة برازيلي غامق', price_s: 40, price_d: 45 },
                    { name_en: 'Black Bull Coffee', name_ar: 'قهوة بلاك بول', price_s: 40, price_d: 45 },
                    { name_en: 'Colombian Coffee', name_ar: 'قهوة كولمبي', price_s: 40, price_d: 45 },
                    { name_en: 'Colombian Dark Coffee', name_ar: 'قهوة كولمبي غامق', price_s: 45, price_d: 50 },
                    { name_en: 'Yemeni Coffee', name_ar: 'قهوة يمني', price_s: 50, price_d: 55 },
                    { name_en: 'Arees Coffee', name_ar: 'قهوة العريس', price_s: 50, price_d: 55 },
                    { name_en: 'French Coffee', name_ar: 'قهوة فرنساوي', price_s: 50, price_d: null },
                    { name_en: 'Flavor Coffee', name_ar: 'قهوة فليفر', price_s: 60, price_d: null, description: 'بندق - فانيليا - شيكولاتة - كارميل - مانجو - توت - شيشه تفاح - فراولة' }
                ],
                'coffee': [
                    { name_en: 'Espresso', name_ar: 'اسبريسو', price_s: 45, price_d: 55 },
                    { name_en: 'Americano', name_ar: 'أمريكانو', price_s: 55, price_d: null },
                    { name_en: 'Macchiato', name_ar: 'ميكاتو', price_s: 50, price_d: 60 },
                    { name_en: 'American Coffee', name_ar: 'أمريكان كوفي', price_s: null, price_d: 70 },
                    { name_en: 'Latte', name_ar: 'لاتيه', price_s: 55, price_d: null },
                    { name_en: 'Cortado', name_ar: 'كورتاتو', price_s: 75, price_d: null },
                    { name_en: 'Caramel Macchiato', name_ar: 'كارميل ميكاتو', price_s: 90, price_d: null },
                    { name_en: 'Espresso Affogato', name_ar: 'سبريسو أفوجاتو', price_s: null, price_d: 60 },
                    { name_en: 'Cappuccino', name_ar: 'كابتشينو', price_s: null, price_d: 70 },
                    { name_en: 'Flat White', name_ar: 'فلات وايت', price_s: null, price_d: 65 },
                    { name_en: 'Bonbon Coffee', name_ar: 'بنبون كوفي', price_s: null, price_d: 80 },
                    { name_en: 'Mocha', name_ar: 'موكا', price_s: null, price_d: 65 },
                    { name_en: 'Nutella Latte', name_ar: 'لاتيه نوتيلا', price_s: null, price_d: 65 },
                    { name_en: 'Spanish Latte', name_ar: 'سبانش لاتيه', price_s: null, price_d: 80 },
                    { name_en: 'Choco Chips', name_ar: 'شيكوشيبس', price_s: null, price_d: 85 },
                    { name_en: 'Espresso Coffee Pan', name_ar: 'اسبريسو كوفي بان', price_s: null, price_d: 80 },
                    { name_en: 'Lotus Coffee', name_ar: 'لوتس كوفي', price_s: null, price_d: 75 },
                    { name_en: 'Piccolo', name_ar: 'بيكولو', price_s: null, price_d: 70 },
                    { name_en: 'Pistachio Coffee', name_ar: 'بيستاشيو كوفي', price_s: null, price_d: 100 },
                    { name_en: 'Caramel Coffee', name_ar: 'كراميل كوفي', price_s: null, price_d: 75 },
                    { name_en: 'Nutella Coffee', name_ar: 'نوتيلا كوفي', price_s: null, price_d: 80 },
                    { name_en: 'Coolant', name_ar: 'كولونت', price_s: null, price_d: 85 },
                    { name_en: 'After White', name_ar: 'أفتر وايت', price_s: null, price_d: 80 }
                ],
                'hot-drinks': [
                    { name_en: 'Tea', name_ar: 'شاي', price_s: 25, price_d: null },
                    { name_en: 'Teapot', name_ar: 'شاي براد', price_s: 35, price_d: null },
                    { name_en: 'Green Tea', name_ar: 'شاي أخضر', price_s: 30, price_d: null },
                    { name_en: 'Tea Flavor', name_ar: 'شاي فليفر', price_s: 35, price_d: null },
                    { name_en: 'Milk Tea', name_ar: 'شاي بلبن', price_s: 30, price_d: null },
                    { name_en: 'Karak Tea', name_ar: 'شاي كرك', price_s: 45, price_d: null },
                    { name_en: 'Herbs', name_ar: 'أعشاب', price_s: 20, price_d: null, description: 'كركديه - نعناع - ينسون - زنجبيل - تيلبو' },
                    { name_en: 'Herbs Cocktail', name_ar: 'كوكتيل أعشاب', price_s: 45, price_d: null },
                    { name_en: 'Nescafe Classic', name_ar: 'نسكافية كلاسيك', price_s: 55, price_d: null },
                    { name_en: 'Nescafe Gold', name_ar: 'نسكافية جولد', price_s: 55, price_d: null },
                    { name_en: 'Hot Cider', name_ar: 'هوت سيدر', price_s: 60, price_d: null },
                    { name_en: 'Hot Chocolate', name_ar: 'هوت شوكليت', price_s: 60, price_d: null },
                    { name_en: 'Sahlab Classic', name_ar: 'سحلب كلاسيك', price_s: 55, price_d: null },
                    { name_en: 'Sahlab Nuts', name_ar: 'سحلب مكسرات', price_s: 65, price_d: null },
                    { name_en: 'Sahlab Flavor', name_ar: 'سحلب فليفر', price_s: 75, price_d: null },
                    { name_en: 'Sahlab Fruits', name_ar: 'سحلب فواكه', price_s: 75, price_d: null },
                    { name_en: 'Sahlab Hazelnut', name_ar: 'سحلب بندق', price_s: 85, price_d: null },
                    { name_en: 'Sahlab Pistachio', name_ar: 'سحلب بيستاشيو', price_s: 90, price_d: null },
                    { name_en: 'Vitamin C', name_ar: 'فيتامين سي', price_s: 45, price_d: null },
                    { name_en: 'Hot Chocolate Oreo', name_ar: 'هوت شوكليت أوريو', price_s: 65, price_d: null },
                    { name_en: 'Hot Chocolate Lotus', name_ar: 'هوت شوكليت لوتس', price_s: 65, price_d: null },
                    { name_en: 'Hot Chocolate Marshmallow', name_ar: 'هوت شوكليت مارشيمليو', price_s: 75, price_d: null }
                ],
                'mocktail': [
                    { name_en: 'Classic Mojito', name_ar: 'كلاسيك موهيتو', price_s: 80, price_d: null, description: 'سيرب موهيتو - نعناع - سفن - ليمون' },
                    { name_en: 'Flavor Mojito', name_ar: 'موهيتو فليفر', price_s: 85, price_d: null, description: 'سيرب موهيتو - نعناع - توبينج - سفن - ليمون' },
                    { name_en: 'Sunshine', name_ar: 'صن شاين', price_s: 80, price_d: null, description: 'سيرب ومان - برتقال - سفن' },
                    { name_en: 'Green Mint', name_ar: 'جرين مينت', price_s: 80, price_d: null, description: 'سيرب نعناع - سفن' },
                    { name_en: 'Hawai Mojito', name_ar: 'هواي موهيتو', price_s: 80, price_d: null, description: 'توبينج أناناس - بلوكراساو - عصير أناناس - سفن' },
                    { name_en: 'Hammer Head', name_ar: 'هامر هيد', price_s: 140, price_d: null, description: 'دابل سبريسو - ريدبول' },
                    { name_en: 'Sofiano Explosion Mix', name_ar: 'سفيانو أكسلوجين ميكس', price_s: 155, price_d: null, description: 'قطع بطيخ - قطع فراوله - راسبيري - ريدبول' },
                    { name_en: 'Jamaica', name_ar: 'جامايكا', price_s: 95, price_d: null },
                    { name_en: 'Cherry Cola', name_ar: 'شيري كولا', price_s: 80, price_d: null },
                    { name_en: 'Red Bloody Here', name_ar: 'ريد بلدي هير', price_s: 90, price_d: null },
                    { name_en: 'Mountain View', name_ar: 'مواتنتج فيو', price_s: 95, price_d: null }
                ],
                'ice-coffee': [
                    { name_en: 'Ice Americano', name_ar: 'أيس أمريكانو', price_s: 60, price_d: null },
                    { name_en: 'Ice Latte', name_ar: 'أيس لاتيه', price_s: 65, price_d: null },
                    { name_en: 'Lotus Latte', name_ar: 'لوتس لاتيه', price_s: 75, price_d: null },
                    { name_en: 'Ice Macchiato', name_ar: 'أيس ميكاتو', price_s: 70, price_d: null },
                    { name_en: 'Ice Cappuccino', name_ar: 'أيس كابتشينو', price_s: 75, price_d: null },
                    { name_en: 'Ice Caramel Macchiato', name_ar: 'أيس كراميل ميكاتو', price_s: 90, price_d: null },
                    { name_en: 'Ice Mocha', name_ar: 'أيس موكا', price_s: 80, price_d: null },
                    { name_en: 'Ice White Mocha', name_ar: 'أيس وايت موكا', price_s: 95, price_d: null },
                    { name_en: 'Ice Spanish Latte', name_ar: 'أيس سبانش لاتيه', price_s: 90, price_d: null },
                    { name_en: 'Ice Darlosky Latte', name_ar: 'أيس دارلوسكاي لاتيه', price_s: 85, price_d: null },
                    { name_en: 'Blue Ice Latte', name_ar: 'بلو أيس لاتيه', price_s: 85, price_d: null },
                    { name_en: 'Ice Chicken Esprelio', name_ar: 'أيس تشيكن اسبرليو', price_s: 95, price_d: null },
                    { name_en: 'Ice Chicken Avocado Coffee', name_ar: 'أيس تشيكن أفوكاتو كوفي', price_s: 95, price_d: null },
                    { name_en: 'Matcha', name_ar: 'ماتشا', price_s: 130, price_d: null }
                ],
                'frappe': [
                    { name_en: 'Frappe Coffee', name_ar: 'فرابيه كوفي', price_s: 95, price_d: null },
                    { name_en: 'Double Frappe Coffee', name_ar: 'فرابيه دابل كوفي', price_s: 115, price_d: null },
                    { name_en: 'Nutella Frappe', name_ar: 'نوتيلا فرابيه', price_s: 105, price_d: null },
                    { name_en: 'Chocolate Frappe', name_ar: 'شوكليت فرابيه', price_s: 105, price_d: null },
                    { name_en: 'Caramel Frappe', name_ar: 'كراميل فرابيه', price_s: 105, price_d: null },
                    { name_en: 'Pistachio Frappe', name_ar: 'بستاشيو فرابيه', price_s: 140, price_d: null },
                    { name_en: 'Sofiano Frappe', name_ar: 'سفيانو فرابيه', price_s: 150, price_d: null }
                ],
                'milkshake': [
                    { name_en: 'Milk Vanilla', name_ar: 'ميلك فانيلتيا', price_s: 85, price_d: null },
                    { name_en: 'Milk Chocolate', name_ar: 'ميلك شوكليت', price_s: 85, price_d: null },
                    { name_en: 'Milk Caramel', name_ar: 'ميلك كراميل', price_s: 85, price_d: null },
                    { name_en: 'Milk Strawberry', name_ar: 'ميلك فراوله', price_s: 95, price_d: null },
                    { name_en: 'Milk Blueberry', name_ar: 'ميلك بلوبيري', price_s: 95, price_d: null },
                    { name_en: 'Milk Mango', name_ar: 'ميلك مانجو', price_s: 95, price_d: null },
                    { name_en: 'Milk Nutella', name_ar: 'ميلك نوتيلا', price_s: 105, price_d: null },
                    { name_en: 'Milk Oreo', name_ar: 'ميلك أوريو', price_s: 105, price_d: null },
                    { name_en: 'Milk Digestive Caramel', name_ar: 'ميلك داي جستيف كراميل', price_s: 110, price_d: null },
                    { name_en: 'Milk Mix Berry', name_ar: 'ميلك ميكس بيري', price_s: 100, price_d: null },
                    { name_en: 'Milk Overdose', name_ar: 'ميلك اوفر دوز', price_s: 155, price_d: null },
                    { name_en: 'Milk Lotus', name_ar: 'ميلك لوتس', price_s: 105, price_d: null }
                ],
                'fresh-juice': [
                    { name_en: 'Mango', name_ar: 'مانجو', price_s: 65, price_d: null },
                    { name_en: 'Guava', name_ar: 'جوافة', price_s: 50, price_d: null },
                    { name_en: 'Guava Milk', name_ar: 'جوافة حليب', price_s: 60, price_d: null },
                    { name_en: 'Strawberry', name_ar: 'فراوله', price_s: 55, price_d: null },
                    { name_en: 'Strawberry Milk', name_ar: 'فراوله حليب', price_s: 65, price_d: null },
                    { name_en: 'Watermelon', name_ar: 'بطيخ', price_s: 55, price_d: null },
                    { name_en: 'Lemon', name_ar: 'ليمون', price_s: 40, price_d: null },
                    { name_en: 'Lemon Mint', name_ar: 'ليمون نعناع', price_s: 50, price_d: null },
                    { name_en: 'Cantaloupe', name_ar: 'كانتلوب', price_s: 50, price_d: null },
                    { name_en: 'Dates Milk', name_ar: 'بلح حليب', price_s: 55, price_d: null },
                    { name_en: 'Dates Nuts', name_ar: 'بلح مكسرات', price_s: 75, price_d: null },
                    { name_en: 'Banana Milk', name_ar: 'موز حليب', price_s: 50, price_d: null },
                    { name_en: 'Kiwi', name_ar: 'كيوي', price_s: 90, price_d: null },
                    { name_en: 'Avocado', name_ar: 'أفوكادو', price_s: 100, price_d: null },
                    { name_en: 'Avocado Nuts', name_ar: 'أفوكادو مكسرات', price_s: 125, price_d: null }
                ],
                'smoothie': [
                    { name_en: 'Ice Chocolate', name_ar: 'أيس شوكليت', price_s: 60, price_d: null },
                    { name_en: 'Strawberry Smoothie', name_ar: 'سموزي فراوله', price_s: 65, price_d: null },
                    { name_en: 'Watermelon Smoothie', name_ar: 'سموزي بطيخ', price_s: 65, price_d: null },
                    { name_en: 'Passion Fruit Smoothie', name_ar: 'سموزي باشون فروت', price_s: 65, price_d: null },
                    { name_en: 'Fresh Smoothie', name_ar: 'سموزي فريش', price_s: 65, price_d: null },
                    { name_en: 'Mango Smoothie', name_ar: 'سموزي مانجو', price_s: 70, price_d: null },
                    { name_en: 'Tropical Mix Smoothie', name_ar: 'سموزي ترويبكال ميكس', price_s: 75, price_d: null },
                    { name_en: 'Kiwi Smoothie', name_ar: 'سموزي كيوي', price_s: 90, price_d: null },
                    { name_en: 'Torpedo Smoothie', name_ar: 'سموزي توربيدو', price_s: 80, price_d: null },
                    { name_en: 'Blue Banana Smoothie', name_ar: 'سموزي بلوبنانا', price_s: 80, price_d: null }
                ],
                'cocktail': [
                    { name_en: 'Pina Colada', name_ar: 'بيناكولادا', price_s: 75, price_d: null, description: 'أناناس - جوافه - لن' },
                    { name_en: 'Yogurt Honey', name_ar: 'يويورت هاني', price_s: 60, price_d: null },
                    { name_en: 'Beat the Heat', name_ar: 'بيت ذا هيت', price_s: 75, price_d: null, description: 'بطيخ - فراوله - ليمون' },
                    { name_en: 'Palarma', name_ar: 'بالارما', price_s: 75, price_d: null, description: 'جوافه - نعناع - ليمون - سفن' },
                    { name_en: 'Energy Power', name_ar: 'إنرجي باور', price_s: 95, price_d: null, description: 'بلح - موز' },
                    { name_en: 'Florida', name_ar: 'فلوريدا', price_s: 85, price_d: null, description: 'مانجو - جوافه - فراوله' },
                    { name_en: 'Kiwi Stro', name_ar: 'كيوي ستيرو', price_s: 95, price_d: null, description: 'فراوله - كيوي' },
                    { name_en: 'Yogurt Mango', name_ar: 'يوجرت مانجو', price_s: 85, price_d: null },
                    { name_en: 'New Day', name_ar: 'نيو داي', price_s: 95, price_d: null, description: 'مانجو - بلوبيري - نعناع' },
                    { name_en: 'Sofiano Special Cocktail', name_ar: 'سفيانو سبيشيال كوكتيل', price_s: 125, price_d: null, description: 'مانجو - فوخ - أيس كريم فانيليا' },
                    { name_en: 'Fruit Salt', name_ar: 'فروت سالت', price_s: 85, price_d: null }
                ],
                'dessert': [
                    { name_en: 'Cheese Pate', name_ar: 'باتيه جبنة', price_s: 45, price_d: null },
                    { name_en: 'Croissant', name_ar: 'كرواسون', price_s: 50, price_d: null },
                    { name_en: 'Cheese Croissant', name_ar: 'كرواسون جبنة', price_s: 65, price_d: null },
                    { name_en: 'Brownies Cake', name_ar: 'براونيز كيك', price_s: 55, price_d: null },
                    { name_en: 'San Sebastian Cheesecake', name_ar: 'تشيز كيك سان سيبستان', price_s: 55, price_d: null },
                    { name_en: 'American Cheesecake', name_ar: 'تشيز كيك أمريكان', price_s: 55, price_d: null },
                    { name_en: 'Molten Cake', name_ar: 'مولتن كيك', price_s: 95, price_d: null },
                    { name_en: 'Madness', name_ar: 'مادنس', price_s: 75, price_d: null },
                    { name_en: 'Fudge', name_ar: 'فادج', price_s: 70, price_d: null },
                    { name_en: 'Red Velvet', name_ar: 'ريد فيلفت', price_s: 65, price_d: null },
                    { name_en: 'Om Ali', name_ar: 'أم علي', price_s: 70, price_d: null }
                ],
                'soft-drink': [
                    { name_en: 'Water', name_ar: 'مياه', price_s: 10, price_d: null },
                    { name_en: 'Pepsi', name_ar: 'بيبسي', price_s: 30, price_d: null },
                    { name_en: '7UP', name_ar: 'سفن', price_s: 30, price_d: null },
                    { name_en: 'Schweppes', name_ar: 'شويبس', price_s: 35, price_d: null },
                    { name_en: 'Birell', name_ar: 'بريل', price_s: 35, price_d: null },
                    { name_en: 'Fayrouz', name_ar: 'فيروز', price_s: 35, price_d: null },
                    { name_en: 'Red Bull', name_ar: 'ريد بول', price_s: 75, price_d: null }
                ],
                'extra': [
                    { name_en: 'Ice Cream', name_ar: 'أيس كريم', price_s: 25, price_d: null },
                    { name_en: 'Pistachio Sauce', name_ar: 'صوص بيستاشيو', price_s: 30, price_d: null },
                    { name_en: 'Cheddar Cheese', name_ar: 'جبنة شيدر', price_s: 25, price_d: null },
                    { name_en: 'Sauce', name_ar: 'صوص', price_s: 15, price_d: null },
                    { name_en: 'Milk', name_ar: 'حليب', price_s: 25, price_d: null },
                    { name_en: 'Nuts', name_ar: 'مكسرات', price_s: 30, price_d: null }
                ]"""

start_marker = "                'special-coffee': ["
end_marker = "                ]\n            }\n        };"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_menu_str + "\n" + content[end_idx:]
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Mune data updated successfully.")
else:
    print("Could not find markers.", start_idx, end_idx)
