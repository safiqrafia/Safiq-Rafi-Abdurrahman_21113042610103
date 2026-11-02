# 1. import module_name
import exercise8_16_function

exercise8_16_function.ucapkan_salam("Safiq")


# 2. from module_name import function_name
from exercise8_16_function import ucapkan_salam

ucapkan_salam("Safiq")


# 3. from module_name import function_name as fn
from exercise8_16_function import ucapkan_salam as fn

fn("Safiq")


# 4. import module_name as mn
import exercise8_16_function as mn

mn.ucapkan_salam("Safiq")


# 5. from module_name import *
from exercise8_16_function import *

ucapkan_salam("Safiq")