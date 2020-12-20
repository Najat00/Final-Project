from FINAL_PROJECT import parse_args 
import pytest

def test_parse_args_regular():
    argslist = ["csv_name.csv"]
    args = parse_args(argslist)
    assert args.filename == "csv_name.csv"   
    
def test_parse_args_errorr():
    argslist = []
    with pytest.raises(ValueError) as err:
        parse_args(argslist)
    assert str(err.value) == "no arguments"  

    