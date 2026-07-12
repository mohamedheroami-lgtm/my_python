# نعمل متغير للادخال
ga = input ("Enter the name of a book you own :\n").lower()
# متغير الادخال الثاني
ha = input ("Enter the name of another book you own ( or press 'Enter' to skip : ").lower()
# نعمل قائمه المملوكات
ca =[]
#نضيف اول متغير
ca.append (ga)
#الجمله الشرطيه لتحديد هل المدخل عايز يضيف كتاب ثاني ولا لا
if ha:
    ca.append (ha)
    print(f"Your library is :  {ca}")
#شرط عشان اللوب ما يطلع    
else:
 print(f"Your library is : {ca}")
# صناعه ليست جديده للاماني 
la = []
#انشاء متغيرات
ya = input("Enter a name of a book that you wish to get in the future :\n").lower() 
ja = input("Enter a name of another book you want to have in the futuer (or click 'Enter' to skip) :\n").lower()
#اضافه الكتتب الى قائمه الامنيات
la.append (ya)
#وضع الشرط للتخيير بين التخطي بدون اضافه او الاضافه
if ja:
    la.append (ja)
    print (f"Your wish list is : {la}")
#المواصله 
else:
    print (f"Your wish list is : {la}")
#الكتب المكتسبه من قائمه الامنيات
va = input("Enter a name of your wish list that you had already aquired (or press 'Enter' to skip) :\n").lower()
#شرط وجود الكتاب في القائمه من اجل حذف
if va in la:
    ca.append (va)
    la.remove (va)
    print(f"Update library : {ca}")
    print(f"Your update wish list is : {la} ")
#في حاله عدم الوجود
else:
    print("ok")
#الكتب المتبرع بها
ea = input("Enter a name of a book you wish to adonate (or press 'Enter' to skip) :").lower()
#اذا كان متبرع به فيجب ازالته من المملوكات    
if ea in ca:
    if ea:
         ca.remove (ea)
         print(f"Your final library after donations is : {ca}")
# اذا لم يتبرع به     
else:
    print(f"Your final library after donations is : {ca}")
    
        
            
    