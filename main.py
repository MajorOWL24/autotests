import unittest
import app

num = "123"


class TestApp(unittest.TestCase):
    def test_getDoc(self):
        self.assertEqual(app.check_document_existance("11-2"), True)
        self.assertEqual(app.check_document_existance("123"), False)

    def test_addDoc(self):
        name = "Иванов Иван Иванович"
        self.assertEqual(app.check_document_existance(num), False)
        app.add_new_doc(num, "type1", name, "Моя полка")
        self.assertEqual(app.check_document_existance(num), True)
        self.assertEqual(app.get_doc_owner_name(num), name)

    def test_deleteDoc(self):
        self.assertEqual(app.check_document_existance(num), True)
        app.delete_doc(num)
        self.assertEqual(app.check_document_existance(num), False)


if __name__ == '__main__':
    unittest.main()
