from pathlib import Path

def main():
    RAW_DATA_PATH = Path(__file__).parent / "data" / "raw"

    print(RAW_DATA_PATH)
    
    
main()