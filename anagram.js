function main () {
	const input = ['code', 'doce', 'anagram', 'aanagmr', 'xesqued', 'xesque', 'quesxe', 'eodc', 'dcoe']
	const expectedOutput = ['code', 'anagram', 'xesque']
	const actualOutput = anagram(input)
	console.log('input:', input)
	console.log('expectedOutput:', expectedOutput)
	console.log('actualOutput:', actualOutput)
}

function anagram (words) {
	const anagrams = []
	words.forEach(wordForOrder => {
		const ordenedWord = wordForOrder.split('').sort().join()
		words.forEach(wordForComparison => {
			const newWordForComparison = wordForComparison.split('').sort().join()
			if (ordenedWord === newWordForComparison) {
				anagrams.push(wordForOrder)
				return
			}
		})
		flag = false
	})
	return anagrams
}

main()
