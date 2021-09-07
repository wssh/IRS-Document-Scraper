import requests
from bs4 import BeautifulSoup


def scrape_irs(searchVal, result):
    max_year = "0"
    min_year = "3000"
    form_number = ""
    form_title = ""

    searchValue = searchVal[0]         # we always get the 1st value of the arr, since it will have the search term

    URL = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html?sortColumn=sortOrder&indexOfFirstRow=0&value=" \
          + searchValue + "&criteria=formNumber&resultsPerPage=200&isDescending=false"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    if soup.find("p", id="errorText"):  # when an invalid search input is given, i.e: no form exists with the search
        # form_number = "invalid input" # the page will display a paragraph with an error text
        # form_title = "invalid input"  # if we see this, then we know we have an invalid input, so we skip it and do
        # max_year = "invalid input"    # nothing
        # min_year = "invalid input"
        # data = {'form_number': form_number, 'form_title': form_title, 'min_year': min_year, 'max_year': max_year}
        # result.append(data)           # should we append invalid input data? probably not. this was here for testing.
        print("invalid input")
    else:
        formNumbers = soup.find_all("td", class_="LeftCellSpacer")
        for formNumber in formNumbers:
            formparent = formNumber.findParent("tr")
            formnum = formparent.find(class_="LeftCellSpacer").text.strip()
            formtitle = formparent.find(class_="MiddleCellSpacer").text.strip()
            formyear = formparent.find(class_="EndCellSpacer").text.strip()

            # we are removing spaces and making the input and form num all lower case, then rejoining them to normalize
            # the input and search result. this is done in case we get an input like 'formw-2' instead of 'Form W-2'
            # not required according to my recruiter, so we're doing all this extra string manipulation "just in case"
            if ''.join(formnum.split()).lower() == ''.join(searchValue.split()).lower():
                if form_number == "":       # we only update the the form_num once to keep the latest name for it
                    form_number = formnum
                if form_title == "":        # we do the same with the form title.
                    form_title = formtitle
                if max_year < formyear:
                    max_year = formyear
                if min_year > formyear:
                    min_year = formyear
        data = {'form_number': form_number, 'form_title': form_title, 'min_year': min_year, 'max_year': max_year}
        result.append(data)



