
import re, string, unicodedata
def remove_URL():
    """Remove URLs from a sample string"""
    return re.sub(r"http\S+", "", sample)


if __name__ == "__main__":
    print(1)