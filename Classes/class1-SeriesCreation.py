"""Creation of Pandas Series"""
import pandas as pd
   
### Program1: 
def program1():
    number = [10,20,30,40,50]
    new_data1 = pd.Series(data=number)
    print("new_data1:",new_data1)
    print()
    ### OUTPUTS
    """ newdata1 Output
            new_data1 
            0    10 
            1    20
            2    30
            3    40
            4    50
            dtype: int64    ### Type is Integer as Orginal Dataset Looks
    """ 
 

### PROGRAM 2:

def program2():
    number = [10,20,30.6,40,50]  ##dataset float
    new_data2 = pd.Series(data=number)
    print("new_data2:",new_data2)
    print()
    
    """OUTPUT
        new_data2:  0    10.0
                    1    20.0
                    2    30.6
                    3    40.0
                    4    50.0
                    dtype: float64       ## Float
    """
#program2()

  

def program3():
    number = [10,20,30,40,50]
    new_data3 = pd.Series(data=number,index=range(1,6))
    print("new_data3:",new_data3)
    print()
    
    """OUTPUT
        new_data3:  1    10
                    2    20
                    3    30
                    4    40
                    5    50
                    dtype: int64
    """
#program3()




def program4():
    number = [10,20,30,40,50]
    new_data4 = pd.Series(data=number,index=range(1,6),dtype='float')
    print("new_data4:",new_data4)
    print()
    
    """OUTPUT
        new_data4: 1    10.0
                    2    20.0
                    3    30.0
                    4    40.0
                    5    50.0
                    dtype: float64
    """
#program4()




def program5():
    number = [10,20,30,40,50]
    new_data5 = pd.Series(data=number,index=range(1,6),dtype='string')
    print("new_data5:",new_data5)
    print()
    
    """OUTPUT
        new_data5: 1    10
                    2    20
                    3    30
                    4    40
                    5    50
                    dtype: string   ### Type String
    """
#program5()



def program6():
    number = {'a':100,'b':200,'c':250,'d':300}
    new_data6 = pd.Series(data=number)
    print("TRYING WITH DICTIONARY")
    print("new_data6:",new_data6)
    print()
    
    """OUTPUT
        TRYING WITH DICTIONARY
        new_data6:  a    100
                    b    200
                    c    250
                    d    300
                    dtype: int64
    """
#program6()


def program7():
    number = {'a':100,'b':200,'c':250,'d':300}
    new_data6 = pd.Series(data=number,index=range(10,14))  ## Index acts as Key,to return values.
    print("TRYING WITH DICTIONARY 2")
    print("new_data7:",new_data6)
    print()
    
    """OUTPUT
        TRYING WITH DICTIONARY 2
            new_data7:  10   NaN
                        11   NaN
                        12   NaN
                        13   NaN
                        dtype: float64
    """
#program7()


def program8():
    number = {'a':100,'b':200,'c':250,'d':300}
    new_data8 = pd.Series(data=number,index=['a','b','c','s',5])  ## Index acts as Key,to return values.
    print("TRYING WITH DICTIONARY 3")
    print("new_data8:",new_data8)
    print()
    
    """OUTPUT
        TRYING WITH DICTIONARY 3
            new_data8:  a    100.0
                        b    200.0
                        c    250.0
                        s      NaN
                        5      NaN
            dtype: float64
    """
#program8()


def program9():
    number = 100
    new_data9 = pd.Series(data=number)  
    print("TRYING WITH Scalar values ")
    print("new_data9:",new_data9)
    print()
    
    """OUTPUT
        TRYING WITH Scalar values 
            new_data9: 0    100
            dtype: int64
    """
#program9()



def program10():
    number = 100
    new_data10 = pd.Series(data=number,index=[10,20,30])  
    print("TRYING WITH Scalar values2 ")
    print("new_data10:",new_data10)
    print()

    
    """OUTPUT
        TRYING WITH Scalar values2 
        new_data10: 10    100
                    20    100
                    30    100
                    dtype: int64 
    """
#program10()


### FOR LOOP List Method Function Call
# programs = [program1,program2,program3,program4,program5,program6,program7,program8,program9, program10]
# for program in programs:
#     program()

### For Loop Range Call
for number in range(1, 11):
    code = 'program' + str(number) + '()'
    eval(code)







