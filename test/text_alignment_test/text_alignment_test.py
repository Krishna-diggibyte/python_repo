import unittest
from src.text_alignment.util import *

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual_input = print_pattern()
        expected_output = '''    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH
                     HHHHHHH 
                      HHHHH  
                       HHH   
                        H    
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
5
        '''

    def test2(self):
        actual_input = print_pattern()
        expected_output = '''  H  
 HHH 
HHHHH
 HHH         HHH        
 HHH         HHH        
 HHH         HHH        
 HHH         HHH        
 HHHHHHHHHHHHHHH  
 HHHHHHHHHHHHHHH  
 HHH         HHH        
 HHH         HHH        
 HHH         HHH        
 HHH         HHH        
            HHHHH
             HHH 
              H  
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
3
        '''

    def test3(self):
        actual_input = print_pattern()
        expected_output = '''      H      
     HHH     
    HHHHH    
   HHHHHHH   
  HHHHHHHHH  
 HHHHHHHHHHH 
HHHHHHHHHHHHH
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH    
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
   HHHHHHH                     HHHHHHH                  
                            HHHHHHHHHHHHH
                             HHHHHHHHHHH 
                              HHHHHHHHH  
                               HHHHHHH   
                                HHHHH    
                                 HHH     
                                  H      
'''
        self.assertEqual(actual_input, expected_output)
        '''
        sample input 
7
        '''

if __name__ == '__main__':
    unittest.main()
