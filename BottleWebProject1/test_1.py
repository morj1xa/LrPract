import unittest
from myform import mailCheck

class Test_test_1(unittest.TestCase):
    def testFalse(self):
        list_mail_uncor = ["", "1", "m1@", "@mail", "qwerty", "qwerty@gmail", ":@mail.ru", "@mail.ru", "fgjfgsdgmail.com", "fgjfgj  gmail.com",  "=@gmail.com", "mghmghm@gmail,com"]
        c = 0
        for i in range (0, len(list_mail_uncor)):
            if not mailCheck(list_mail_uncor[i]):
                c+=1
                
        self.assertEqual(12,c)
    

    def testTrue(self):
            list_mail_uncor = ["seva@gmail.com", "seva@mail.com", "qwerty@mail.ru", "morj@gmail.com", "morj@icloud.com", "gfgjft@yandex.com", "hght@inbox.com", "sev4ik@gmail.com"]
            c = 0
            for i in range (0, len(list_mail_uncor)):
                if mailCheck(list_mail_uncor[i]):
                    c+=1
                
            self.assertEqual(8,c)

if __name__ == '__main__':
    unittest.main()
