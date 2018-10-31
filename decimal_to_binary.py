import pandas as pd

def main():
    bias = ["0000", "0001", "0010", "0011",
        "0100", "0101", "0110", "0111",
        "1000", "1001", "1010", "1011",
        "1100", "1101", "1110", "1111"]

    decimal_num = float(input("Enter a decimal number: "))
    
    whole, frac = decimal_as_binary(decimal_num)
    print_mantissa(whole, frac, bias)

def whole_to_binary(whole_part):
    binary = ""

    while(whole_part != 0):
        remainder = str(whole_part%2)
        whole_part = int(whole_part/2)
        binary = remainder + binary
    
    return binary

def frac_to_binary(frac_part):
    binary = ""

    for i in range(0,8):
        frac_part = frac_part * 2
        if frac_part >= 1.0:
            frac_part = frac_part - 1.0
            binary = binary + '1'
        else:
            binary = binary + '0'
        
        if frac_part == 1.0:
            break
    
    return binary

def decimal_as_binary(decimal_number):
    whole = int(decimal_number)
    frac = decimal_number - whole

    return whole_to_binary(whole), frac_to_binary(frac)

def print_mantissa(whole, frac, bias_scale):
    bias = 7
    sign = 0
    
    whole = whole[1:]
    exponent = len(whole)
    mantissa = whole + frac

    if exponent == 0:
        mantissa_exp = bias
    elif exponent > 0:
        mantissa_exp = bias + exponent
    else:
        mantissa_exp = bias - exponent
    
    expression = {'Sign':[sign], 'Exponent':[bias_scale[mantissa_exp]], 'Mantissa':[mantissa]}
    mantissa_df = pd.DataFrame(expression)[['Sign', 'Exponent', 'Mantissa']]
    print(mantissa_df)
    # mantissa_df.to_excel('mantissa.xlsx', index=False)

main()