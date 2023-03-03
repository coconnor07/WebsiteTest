function sendRequest(message) {
    axios.post('/api/submit', { message: message })
        .then(response => {
            console.log(response.data);
            document.getElementsByClassName("text")[0].textContent = response.data.message;
        })
        .catch(error => {
            console.error(error);
        });
}

function setWordOfTheDay()
{
    var input = document.getElementsByClassName("inputBox");
    var word = input[0].value;
    var definition = input[1].value;

    axios.post('/api/submit/setword', { word: word, definition: definition })
        .then(response => {
            console.log(response.data);
            document.getElementsByClassName("status")[0].textContent = response.data.status;
        })
        .catch(error => {
            console.error(error);
        });
}

function getWordOfTheDay()
{
    axios.post('/api/submit/getword', { message: "get word" })
        .then(response => {
            console.log(response.data);
            document.getElementsByClassName("word")[0].textContent = response.data.word;
            document.getElementsByClassName("definition")[0].textContent = response.data.definition;
        })
        .catch(error => {
            console.error(error);
        });
}

try {
    var title = document.getElementsByClassName("text")[0];
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0');
    var yyyy = today.getFullYear();

    today = mm + '/' + dd + '/' + yyyy;
    title.textContent = today;
}
catch
{
    console.log("nothing to see here");
}