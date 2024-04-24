intro = """CREATION OF DATAFRAME 
            Import pandas
            1.Dataframe Can be Created Empty.
            2.Created From List.
            3.Created from Tuples
            4.Created From Pandas Series
"""

 
import pandas as pd

def program0():
    print(intro)


def program1():
    print("Creation of Empty Data Frame")
    df = pd.DataFrame()
    print("DataFrame:",df)
    print("***********************")
    print()

    """
    OUTPUT Creation of Empty Data Frame
                DataFrame: Empty DataFrame
                Columns: []
                Index: []
    """



def program2():
    print("Creation of Data Frame from List")
    new_list = ["car","bike","train","auto","aeroplane"]
    df = pd.DataFrame(new_list)
    print("DataFrame:",df)
    print("***********************")
    print()

    """
    OUTPUT DataFrame:            0
                        0        car
                        1       bike
                        2      train
                        3       auto
                        4  aeroplane
    """



def program3():
    print("Creation of Data Frame from List with Column name")
    new_list = ["car","bike","train","auto","aeroplane"]
    df = pd.DataFrame(new_list,columns=["Vehicles"])
    print("DataFrame:",df)
    print("***********************")
    print()

    """
    OUTPUT DataFrame:     Vehicles
                    0        car
                    1       bike
                    2      train
                    3       auto
                    4  aeroplane
    """



def program4():
    print("Creation of Data Frame from Nested List")
    new_list = [ ["car",10], ["bike",100],["cycle",150] , ["train",230] ]
    
    df = pd.DataFrame(new_list)
    print("DataFrame:",df)
    print("***********************")
    print()

    """
    OUTPUT
            DataFrame:        0    1
                        0    car   10
                        1   bike  100
                        2  cycle  150
                        3  train  230
    """




def program5():
    print("Creation of Data Frame from Nested List")
    new_list = [ ["car",10,"40kmph"], ["bike",100,"80kmph"],["cycle",150,"50kmph"] , ["train",230,"100kmph"] ]
    
    df = pd.DataFrame(new_list)
    print("DataFrame:",df)
    print("***********************")
    print()

    """
    OUTPUT
            DataFrame:        0    1        2
                            0    car   10   40kmph
                            1   bike  100   80kmph
                            2  cycle  150   50kmph
                            3  train  230  100kmph
    """



def program6():
    print("Creation of Data Frame from Dictionary")
    new_dictionary = {
                        "NAME":["Tom","Jerry","Donald Duck","Mickey Mouse"],
                        "AGE" : [15,25,35,45],
                        "LOCATION":["Chennai","Thirchy","Madurai","Salem"]
                    }
    
    df = pd.DataFrame(new_dictionary)
    print("DataFrame:",df)
    print("***********************")
    print()

    """
    OUTPUT DataFrame:            NAME  AGE LOCATION
                    0           Tom   15  Chennai
                    1         Jerry   25  Thirchy
                    2   Donald Duck   35  Madurai
                    3  Mickey Mouse   45    Salem
    """







def program7():
    print("Creation of Data Frame from Dictionary")
    new_dict = {
        "Idly": [25],
        "Dosa": [50],
        "poori": [40],
        "Idiyappam": [60],
        "Pongal": [45]
    }
    
    df = pd.DataFrame(new_dict)
    print("DataFrame:", df)
    print("***********************")
    print()
    """
    OUTPUT 
    Creation of Data Frame from Dictionary
        DataFrame:    Idly  Dosa  poori  Idiyappam  Pongal
                  0    25    50     40         60      45
    """






def program8():
    print("Creation of Data Frame from Series1")
    new_dataset = {
                "Tiffen":pd.Series([15,25,35],index=["a","b","c"]), 
                "Lunch":pd.Series([100,150,200,250],index=["a","b","c","d"]), 
                }
    
    df = pd.DataFrame(new_dataset)
    print("DataFrame:", df)
    print("***********************")
    print()
    """
    OUTPUT 
        DataFrame:      Tiffen  Lunch
                    a    15.0    100
                    b    25.0    150
                    c    35.0    200
                    d     NaN    250
    
    """


#program8()




def program9():
    print("Creation of Data Frame from Series2")
    new_dataset = {
                "Tiffen":pd.Series([15,25,35],index=["a","b","c"]), 
                "Lunch":pd.Series([100,150,200,250],index=["a","x","y","z"]), 
                }
    
    df = pd.DataFrame(new_dataset)
    print("DataFrame:", df)
    print("***********************")
    print()
    """
    OUTPUT 
      Creation of Data Frame from Series2
        DataFrame:      Tiffen  Lunch
                    a    15.0  100.0
                    b    25.0    NaN
                    c    35.0    NaN
                    x     NaN  150.0
                    y     NaN  200.0
                    z     NaN  250.0  
    """


## FOR LOOP List Method Function Call
programs = [program1,program2,program3,program4,program5,program6,program7,program8,program9]
for program in programs:
    program()
