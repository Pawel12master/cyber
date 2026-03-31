Skrypt porównujący hash MD5 z hashami słów ze słownika. Skrypt powinien: • przyjąć hash MD5 jako argument • czytać słowa z wordlisty • hashować każde słowo (md5sum) • porównać z podanym hashem • wypisać hasło jeśli znalezione


MEMORY:
- lista slow wyglada tak ("xyz" "abc" "pas") a nie jak w python
- czytajac liste slow for word in "${WORD_LIST[@]}" nalezy wyciac potencjalne slowa z znakow \n itp  za pomoca cut -d ' ' -f1


