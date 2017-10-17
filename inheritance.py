class A:
    def __init__(self):
        super().__init__()
        print('stuff1')
class B:
    def __init__(self):
        super().__init__()
        print('stuff2')
class C(B,A):
    def __init__(self):
        super().__init__()
        print('stuff3')

C();
    
