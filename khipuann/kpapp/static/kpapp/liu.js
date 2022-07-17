const kiatko = document.getElementById('kiatko');
const thesi = document.getElementById('thesi');

for(const b of document.querySelectorAll('button[name="btn"]')){
	b.addEventListener('click', function(){
		console.log('Click btn:', b.value);//kiatko.value += b.value;
		// kiatko.setSelectionRange(caret, caret);
		tshahJi(b.value);
	})
}

function tshahJi(ji) {
		console.log('selectionEnd', kiatko.selectionEnd)
		const kuji = kiatko.value;
		const insertTokenAt = kiatko.selectionEnd;
		const sinui = insertTokenAt + ji.length;
		kiatko.value = (
			kuji.slice( 0, insertTokenAt ) +
			ji +
			kuji.slice( insertTokenAt )
		);
		kiatko.selectionStart = sinui;
		kiatko.selectionEnd = sinui;
		kiatko.focus();
}
function khok(){
	navigator.clipboard.writeText(kiatko.value).then(function() {
	  thesi.innerText = 'Copying to clipboard was successful!';
	  thesi.classList.remove('d-none');
	  setTimeout(function(){
	    thesi.innerText = '';
	    thesi.classList.add('d-none');
	  }, 5000);
	}, function(err) {
	  console.error('Could not copy text: ', err);
	});
}