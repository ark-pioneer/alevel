# # abstract
# # virtual
# # instance/static

# # access modifiers
# # private/public/protected (can be inherited)

# class Animal():
#     def hello(self):
#         self.bye()

#     private def bye(self):
#         return "byebye"
    
#     protected def soLongAndThanksForAllTheFish(self):
#         return "byebye"
    

# a = Animal()
# a.bye()
       
# class Llama(Animal):
#     static {
#         def hello(): 
#             return xyz
#     }
#     static def hello():
#         return "BONJOUR"

# # l = Llama()
# # l2 = Llama()
# # l3 = Llama()
# # l.hello()
# # l2.hello()
# # l3.hello()

# print(Llama.hello())

# class Vehicle():
#     # private
#     colour = ""

#     def getColour(): # getting the private data field
#         return colour

#     def setColour(newColour): # updating the private data field
#         colour = newColour


Member = Class
    public
        procedure addNewMember
        procedure amendMemberDetails
        procedure showMemberDetails

    private
        membership_number: integer
        firstname: String
        lastname: String
        telephone_number: String
end


# 5)
# StockItem = Class
#     public
#         procedure setLoan
#         procedure displayDetails

#     private
#         Title: String
#         OnLoan: Boolean
#         DateAcquired: Date

# Book = Class(StockItem)
#     public
#         procedure displayDetails(override)
#     private
#         author: String
#         ISBN: String

# CD = Class(StockItem)
#     public
#         procedure displayDetails(override)
#     private
#         artist: String
#         playing_time: integer
