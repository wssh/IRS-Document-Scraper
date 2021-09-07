import requests
from bs4 import BeautifulSoup

def download_irs(searchVal, minYear, ran):
    years = set()
    for x in range(ran+1):
        years.add(minYear+x)

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
            formyear = formparent.find(class_="EndCellSpacer").text.strip()

            if ''.join(formnum.split()).lower() == ''.join(searchValue.split()).lower() \
                    and int(formyear) in years:
                        formDownload = formparent.find("a", href=True).get("href")
                        response = requests.get(formDownload)
                        fileName = formnum + " - " + formyear + ".pdf"
                        fileDir = "download/" + fileName
                        with open(fileDir, "wb") as outputFile:
                            outputFile.write(response.content)
                            outputFile.close()
