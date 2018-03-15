import unittest
from ..modules.hello_module import ModuleClass

class Tests(unittest.TestCase):
    def test_module_class_default_method(self):
        self.assertEqual(ModuleClass.default(), "Hello World from Module")

if __name__ == '__main__':
    unittest.main()