from faker import Faker
import re

fake = Faker()


lorem = "ontrary to popular belief, " \
"Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin " \
"literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor " \
"at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, " \
"from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered " \
"the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" " \
"(The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, " \
"very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", " \
"comes from a line in section 1.10.32."


x = re.search("[Ll]orem", lorem)

if x:
    print("Match found")
else:
    print("No match found")

print(re.findall(r"Ext\w*m.s", lorem))

# <_>
# 
# Person Class
# -name: string
# -address: string
# -email: string
# <<create>>+__init__(name: string, address: string, email: string)
# +__str__(): string
# +get_name(): string

class Person:
    def __init__(self, *name: str, address, **email: str):
        self.name = name
        self.address = address
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nEmail: {self.email}\n"
    
    def get_name(self):
        return self.name

# person = Person(fake.name(), fake.address(), fake.email())

# Tuple - is TWO or MORE values!

person = Person(
    fake.name(), fake.name(), fake.name(),\
    address=fake.address(),\
    email=fake.email()
    )

print(person)
print("Person's Name:", person.get_name())


print(fake.address())
print(fake.currency_code())

# <_>


