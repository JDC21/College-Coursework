window.onload = function Pokemon() {
	
// Get All Card Elements

const cards = document.getElementsByClassName('card')

// Add the class to all elements

for (let i = 0;i < cards.length;i++)
	
	cards[i].classList.add('shadow')

// Add the link to Pokemon Website

const link = document.createElement('a')

link.setAttribute('href', 'https://pokemon.com') // set the href

link.innerText = "Pokemon Website" // set link text

document.body.appendChild(link) // add the link to body

}