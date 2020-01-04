import unittest
from hashing import HashTable


class TestHashTable(unittest.TestCase):
    
    def test_ReSize(self):
        Htest=HashTable()
        Htest[54]="cat"
        Htest[26]="dog"
        Htest[93]="lion"
        Htest[17]="tiger"
        Htest[77]="bird"
        Htest[31]="cow"
        Htest[44]="goat"
        Htest[55]="pig"
        Htest[20]="chicken"
        Htest[14]="R"
        Htest[15]="G"
        Htest[10]="B"
        Htest[11]="L"
        Htest[12]="Q"
        Htest[13]="S"
        self.assertEqual(Htest.size, 22, "The answer should be 22 after resizing from double")
        
    def test_CorrectPosition(self):
        Htest2=HashTable()
        Htest2[56]="cat"
        self.assertEqual(Htest2.slots[1], 56, "The answer should be 56 from hashing")
            
    def test_CorrectPositionAfterResize(self):
        Htest3=HashTable()
        Htest3[54]="cat"
        Htest3[26]="dog"
        Htest3[93]="lion"
        Htest3[17]="tiger"
        Htest3[77]="bird"
        Htest3[31]="cow"
        Htest3[44]="goat"
        Htest3[55]="pig"
        Htest3[20]="chicken"
        Htest3[14]="R"
        Htest3[15]="G"
        Htest3[10]="B"
        Htest3[11]="L"
        Htest3[12]="Q"
        Htest3[13]="S"
        self.assertEqual(Htest3.data[0], "goat", "The answer should be goat from rehashing after resizing")

    def test_Rehash(self):
        Htest4=HashTable()
        Htest4[11]="cat"
        Htest4[22]="dog"
        self.assertEqual(Htest4.data[1], "dog", "The answer should be dog from rehashing")
     
    def test_RehashAfterResize(self):
        Htest5=HashTable()
        Htest5[11]="cat"
        Htest5[22]="dog"
        Htest5[93]="lion"
        Htest5[17]="tiger"
        Htest5[77]="bird"
        Htest5[31]="cow"
        Htest5[44]="goat"
        Htest5[55]="pig"
        Htest5[20]="chicken"
        Htest5[14]="R"
        Htest5[15]="G"
        Htest5[10]="B"
        Htest5[11]="L"
        Htest5[12]="Q"
        Htest5[13]="S"
        self.assertEqual(Htest5.data[0], "dog", "The answer should be dog from rehashing after ")
        
    
    
    
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    
