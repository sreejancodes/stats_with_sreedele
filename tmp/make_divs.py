import pandas as pd

countries_file = pd.read_csv("countries.txt", sep="\t")

def retrieve_div_string(row):
    country = row.Country 
    code = row.Code.lower()

    div_content = f"""
    <div class="grid">
                <label for="rating{country}"><span class="fi fi-{code}"></span> {country}</label>
                <input type="number" id="rating{country}" name="rating{country}" min="0" max="10" step="0.01" required>
            </div>
    """
    print(div_content.strip())
    #return div_content.strip()

countries_file.apply(lambda row: retrieve_div_string(row) , axis=1)

