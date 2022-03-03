console.log()
var currentPage = 1;
var btnMore = document.getElementById('nextPage')

function getPage() {

    fetch('/posts/page/' + (currentPage + 1))
        .then(async function(result) {
            if (result.status == 200) {
                currentPage++
            }
            var html = await result.text()
            btnMore.insertAdjacentHTML('beforebegin', html)
        })
        .catch(function(err) { console.log(err) })

}


getPage()